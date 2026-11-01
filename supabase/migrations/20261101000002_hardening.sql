-- Endurecimento de segurança (recomendações do advisor do Supabase)
alter function public.set_updated_at() set search_path = public;

-- Funções de gatilho: nunca chamáveis por RPC
revoke execute on function public.handle_new_user() from public, anon, authenticated;
revoke execute on function public.guard_publish() from public, anon, authenticated;

-- Funções auxiliares usadas pelas políticas RLS: só utilizadores autenticados
revoke execute on function public.has_role(uuid, public.app_role) from public, anon;
revoke execute on function public.is_admin() from public, anon;
revoke execute on function public.is_teacher() from public, anon;
revoke execute on function public.is_teacher_of(uuid) from public, anon;
grant execute on function public.has_role(uuid, public.app_role) to authenticated;
grant execute on function public.is_admin() to authenticated;
grant execute on function public.is_teacher() to authenticated;
grant execute on function public.is_teacher_of(uuid) to authenticated;
