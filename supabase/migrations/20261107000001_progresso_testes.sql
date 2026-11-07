-- Progresso por aula e testes por disciplina/nível (nota 0–20, corrigida no servidor).
create table if not exists public.lesson_progress (
  user_id uuid not null references auth.users (id) on delete cascade,
  lesson_id uuid not null references public.lessons (id) on delete cascade,
  completed boolean not null default false,
  seconds int not null default 0 check (seconds >= 0),
  first_seen_at timestamptz not null default now(),
  last_seen_at timestamptz not null default now(),
  primary key (user_id, lesson_id)
);
alter table public.lesson_progress enable row level security;
drop policy if exists lesson_progress_read on public.lesson_progress;
create policy lesson_progress_read on public.lesson_progress for select to authenticated using (user_id = auth.uid());

create table if not exists public.subject_tests (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  subject_id uuid references public.subjects (id) on delete cascade,
  level_id uuid references public.levels (id) on delete cascade,
  kind text not null check (kind in ('diagnostic','consolidation','final','exam')),
  correct int not null check (correct >= 0),
  total int not null check (total > 0),
  score numeric(4,1) not null check (score between 0 and 20),
  seconds int not null default 0 check (seconds >= 0),
  created_at timestamptz not null default now(),
  check (correct <= total),
  check ((subject_id is not null) <> (level_id is not null))
);
create index if not exists subject_tests_user_idx on public.subject_tests (user_id, created_at desc);
alter table public.subject_tests enable row level security;
drop policy if exists subject_tests_read on public.subject_tests;
create policy subject_tests_read on public.subject_tests for select to authenticated using (user_id = auth.uid());

-- Regista progresso numa aula (visita ou conclusão). Só toca nas linhas do próprio utilizador.
create or replace function public.mark_lesson(_slug text, _seconds int, _completed boolean)
returns void language plpgsql security definer set search_path = public as $$
declare lid uuid;
begin
  if auth.uid() is null then raise exception 'não autenticado'; end if;
  select id into lid from public.lessons where slug = _slug and status = 'published';
  if lid is null then raise exception 'aula inexistente'; end if;
  insert into public.lesson_progress (user_id, lesson_id, completed, seconds)
  values (auth.uid(), lid, coalesce(_completed,false), least(greatest(coalesce(_seconds,0),0), 7200))
  on conflict (user_id, lesson_id) do update
    set completed = public.lesson_progress.completed or excluded.completed,
        seconds = public.lesson_progress.seconds + excluded.seconds,
        last_seen_at = now();
end $$;
revoke all on function public.mark_lesson(text,int,boolean) from public, anon;
grant execute on function public.mark_lesson(text,int,boolean) to authenticated;

-- Regista um teste: a nota vem das tentativas já corrigidas pelo servidor (não do cliente).
-- _scope = slug da disciplina (diagnostic/consolidation/final) ou do nível (exam).
create or replace function public.record_test(_scope text, _kind text, _client_ids uuid[], _seconds int)
returns jsonb language plpgsql security definer set search_path = public as $$
declare sid uuid; lid uuid; tot int; ok int; sc numeric(4,1); rid uuid;
begin
  if auth.uid() is null then raise exception 'não autenticado'; end if;
  if _kind not in ('diagnostic','consolidation','final','exam') then raise exception 'tipo inválido'; end if;
  if _kind = 'exam' then
    select id into lid from public.levels where slug = _scope;
    if lid is null then raise exception 'nível inexistente'; end if;
  else
    select id into sid from public.subjects where slug = _scope;
    if sid is null then raise exception 'disciplina inexistente'; end if;
  end if;
  select count(distinct a.client_id), count(distinct a.client_id) filter (where a.is_correct)
    into tot, ok
  from public.attempts a
  join public.exercises e on e.id = a.exercise_id
  join public.topics t on t.id = e.topic_id
  join public.subjects s on s.id = t.subject_id
  where a.user_id = auth.uid() and a.client_id = any(_client_ids)
    and a.created_at > now() - interval '3 hours'
    and (sid is null or s.id = sid)
    and (lid is null or s.level_id = lid);
  if tot = 0 then raise exception 'sem respostas corrigidas'; end if;
  sc := round(ok::numeric / tot * 20, 1);
  insert into public.subject_tests (user_id, subject_id, level_id, kind, correct, total, score, seconds)
  values (auth.uid(), sid, lid, _kind, ok, tot, sc, least(greatest(coalesce(_seconds,0),0), 14400))
  returning id into rid;
  return jsonb_build_object('id', rid, 'correct', ok, 'total', tot, 'score', sc);
end $$;
revoke all on function public.record_test(text,text,uuid[],int) from public, anon;
grant execute on function public.record_test(text,text,uuid[],int) to authenticated;
