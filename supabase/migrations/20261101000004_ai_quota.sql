-- Quota diária atómica do professor IA (só a Edge Function, com service role, a chama)
create or replace function public.consume_ai_quota(_user uuid, _limit int)
returns boolean language plpgsql security definer set search_path = public as $$
declare c int;
begin
  insert into public.ai_usage (user_id, day, message_count)
  values (_user, current_date, 1)
  on conflict (user_id, day) do update
    set message_count = public.ai_usage.message_count + 1
    where public.ai_usage.message_count < _limit
  returning message_count into c;
  return c is not null;
end $$;

revoke execute on function public.consume_ai_quota(uuid, int) from public, anon, authenticated;
grant execute on function public.consume_ai_quota(uuid, int) to service_role;
