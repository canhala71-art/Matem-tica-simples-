-- MenteMat — esquema base, relações, índices e RLS
-- Princípios: recolha mínima de dados; respostas certas em tabela privada;
-- só o administrador publica; escritas sensíveis (tentativas, domínio, IA) só pelo servidor.

create extension if not exists pgcrypto;

-- ---------- Tipos ----------
create type public.app_role as enum ('student', 'teacher', 'admin');
create type public.content_status as enum ('draft', 'review', 'published');
create type public.exercise_type as enum
  ('multiple_choice', 'numeric', 'algebraic', 'true_false', 'written', 'word_problem');
create type public.block_kind as enum
  ('introduction', 'intuition', 'definition', 'formulas', 'worked_example',
   'guided_exercise', 'independent_exercise', 'challenge', 'assessment');
create type public.topic_kind as enum ('unit', 'chapter');

-- ---------- Utilitários ----------
create or replace function public.set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end $$;

-- ---------- Papéis ----------
create table public.roles (
  name public.app_role primary key,
  description text not null
);
insert into public.roles (name, description) values
  ('student', 'Estudante'),
  ('teacher', 'Professor'),
  ('admin', 'Administrador');

create table public.user_roles (
  user_id uuid not null references auth.users (id) on delete cascade,
  role public.app_role not null references public.roles (name),
  primary key (user_id, role)
);
create index user_roles_role_idx on public.user_roles (role);

create or replace function public.has_role(_user uuid, _role public.app_role)
returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.user_roles where user_id = _user and role = _role);
$$;

create or replace function public.is_admin()
returns boolean language sql stable security definer set search_path = public as $$
  select public.has_role(auth.uid(), 'admin');
$$;

create or replace function public.is_teacher()
returns boolean language sql stable security definer set search_path = public as $$
  select public.has_role(auth.uid(), 'teacher');
$$;

-- ---------- Perfis (recolha mínima) ----------
create table public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  display_name text not null default 'Estudante' check (char_length(display_name) <= 60),
  academic_level smallint check (academic_level between 1 and 6),
  is_minor boolean not null default false,           -- só sim/não, sem data de nascimento
  locale text not null default 'pt' check (locale in ('pt', 'en', 'fr', 'es')),
  preferences jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create trigger profiles_updated before update on public.profiles
  for each row execute function public.set_updated_at();

-- Todo o novo utilizador nasce estudante. O papel nunca vem do cliente.
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, is_minor)
  values (
    new.id,
    coalesce(nullif(left(new.raw_user_meta_data ->> 'display_name', 60), ''), 'Estudante'),
    coalesce((new.raw_user_meta_data ->> 'is_minor')::boolean, false)
  );
  insert into public.user_roles (user_id, role) values (new.id, 'student');
  return new;
end $$;

create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

create table public.teacher_students (
  teacher_id uuid not null references auth.users (id) on delete cascade,
  student_id uuid not null references auth.users (id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (teacher_id, student_id),
  check (teacher_id <> student_id)
);
create index teacher_students_student_idx on public.teacher_students (student_id);

create or replace function public.is_teacher_of(_student uuid)
returns boolean language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.teacher_students
    where teacher_id = auth.uid() and student_id = _student
  );
$$;

-- ---------- Conteúdo: Percurso → Nível → Disciplina → Unidade/Capítulo → Aula ----------
create table public.learning_paths (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  title text not null,
  description text,
  position int not null default 0,
  status public.content_status not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.levels (
  id uuid primary key default gen_random_uuid(),
  path_id uuid not null references public.learning_paths (id) on delete cascade,
  number smallint not null check (number between 1 and 6),
  slug text not null unique,
  title text not null,
  description text,
  position int not null default 0,
  status public.content_status not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (path_id, number)
);
create index levels_path_idx on public.levels (path_id);

create table public.subjects (
  id uuid primary key default gen_random_uuid(),
  level_id uuid not null references public.levels (id) on delete cascade,
  slug text not null unique,
  title text not null,
  description text,
  position int not null default 0,
  status public.content_status not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index subjects_level_idx on public.subjects (level_id);

-- topics cobre Unidade e Capítulo (capítulo aponta para a unidade em parent_id)
create table public.topics (
  id uuid primary key default gen_random_uuid(),
  subject_id uuid not null references public.subjects (id) on delete cascade,
  parent_id uuid references public.topics (id) on delete cascade,
  kind public.topic_kind not null default 'unit',
  slug text not null unique,
  title text not null,
  position int not null default 0,
  status public.content_status not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check ((kind = 'unit' and parent_id is null) or (kind = 'chapter' and parent_id is not null))
);
create index topics_subject_idx on public.topics (subject_id);
create index topics_parent_idx on public.topics (parent_id);

create table public.lessons (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references public.topics (id) on delete cascade,
  slug text not null unique,
  title text not null,
  summary text,
  position int not null default 0,
  estimated_minutes smallint check (estimated_minutes > 0),
  status public.content_status not null default 'draft',
  created_by uuid references auth.users (id) on delete set null,
  reviewed_by uuid references auth.users (id) on delete set null,
  published_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index lessons_topic_idx on public.lessons (topic_id);
create index lessons_status_idx on public.lessons (status);
create index lessons_created_by_idx on public.lessons (created_by);

create table public.lesson_blocks (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid not null references public.lessons (id) on delete cascade,
  kind public.block_kind not null,
  position int not null default 0,
  body text not null,                       -- Markdown com fórmulas KaTeX ($...$)
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index lesson_blocks_lesson_idx on public.lesson_blocks (lesson_id, position);

-- ---------- Exercícios ----------
create table public.exercises (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid references public.lessons (id) on delete set null,
  topic_id uuid not null references public.topics (id) on delete cascade,
  type public.exercise_type not null,
  difficulty smallint not null check (difficulty between 1 and 5),
  competency text not null,                 -- competência avaliada (ex.: 'fracoes.soma')
  statement text not null,                  -- enunciado (Markdown + KaTeX)
  options jsonb,                            -- só escolha múltipla; nunca indica a certa
  status public.content_status not null default 'draft',
  created_by uuid references auth.users (id) on delete set null,
  verified_with_sympy boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check (type <> 'multiple_choice' or options is not null)
);
create index exercises_topic_idx on public.exercises (topic_id);
create index exercises_lesson_idx on public.exercises (lesson_id);
create index exercises_competency_idx on public.exercises (competency);
create index exercises_status_idx on public.exercises (status);

-- Resposta certa, explicação e resolução: tabela privada (alunos nunca leem).
create table public.exercise_answers (
  exercise_id uuid primary key references public.exercises (id) on delete cascade,
  answer jsonb not null,
  tolerance numeric not null default 0 check (tolerance >= 0),
  explanation text not null,
  solution_steps jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now()
);

create table public.exam_papers (
  id uuid primary key default gen_random_uuid(),
  level_id uuid not null references public.levels (id) on delete cascade,
  title text not null,
  description text,
  duration_minutes smallint check (duration_minutes > 0),
  status public.content_status not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index exam_papers_level_idx on public.exam_papers (level_id);

create table public.questions (
  id uuid primary key default gen_random_uuid(),
  exam_paper_id uuid not null references public.exam_papers (id) on delete cascade,
  exercise_id uuid not null references public.exercises (id) on delete cascade,
  position int not null default 0,
  points numeric not null default 1 check (points > 0),
  unique (exam_paper_id, exercise_id)
);
create index questions_exam_idx on public.questions (exam_paper_id, position);
create index questions_exercise_idx on public.questions (exercise_id);

-- ---------- Progresso (escrita só pelo servidor) ----------
create table public.attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  exercise_id uuid not null references public.exercises (id) on delete cascade,
  client_id uuid not null,                  -- idempotência para sincronização offline
  answer jsonb not null,
  is_correct boolean not null,
  time_spent_seconds int check (time_spent_seconds >= 0),
  created_at timestamptz not null default now(),
  unique (user_id, client_id)
);
create index attempts_user_idx on public.attempts (user_id, created_at desc);
create index attempts_exercise_idx on public.attempts (exercise_id);

create table public.mastery (
  user_id uuid not null references auth.users (id) on delete cascade,
  competency text not null,
  attempts_count int not null default 0,
  correct_count int not null default 0,
  distinct_difficulties_correct smallint not null default 0,
  assessment_passed boolean not null default false,
  mastered boolean not null default false,
  updated_at timestamptz not null default now(),
  primary key (user_id, competency)
);

create table public.achievements (
  id uuid primary key default gen_random_uuid(),
  code text not null unique,
  title text not null,
  description text not null,
  points int not null default 0 check (points >= 0)
);

create table public.user_achievements (
  user_id uuid not null references auth.users (id) on delete cascade,
  achievement_id uuid not null references public.achievements (id) on delete cascade,
  earned_at timestamptz not null default now(),
  primary key (user_id, achievement_id)
);
create index user_achievements_ach_idx on public.user_achievements (achievement_id);

-- ---------- Professor IA ----------
create table public.ai_conversations (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  title text,
  created_at timestamptz not null default now()
);
create index ai_conversations_user_idx on public.ai_conversations (user_id, created_at desc);

create table public.ai_messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid not null references public.ai_conversations (id) on delete cascade,
  role text not null check (role in ('user', 'assistant')),
  content text not null,
  is_demo boolean not null default false,   -- resposta de demonstração, sem IA real
  created_at timestamptz not null default now()
);
create index ai_messages_conv_idx on public.ai_messages (conversation_id, created_at);

create table public.ai_usage (
  user_id uuid not null references auth.users (id) on delete cascade,
  day date not null default current_date,
  message_count int not null default 0,
  primary key (user_id, day)
);

-- ---------- Planos futuros ----------
create table public.subscriptions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  plan text not null default 'free',
  status text not null default 'active',
  current_period_end timestamptz,
  created_at timestamptz not null default now(),
  unique (user_id)
);

-- ---------- updated_at ----------
do $$
declare t text;
begin
  foreach t in array array[
    'learning_paths','levels','subjects','topics','lessons','lesson_blocks',
    'exercises','exercise_answers','exam_papers','mastery'
  ] loop
    execute format(
      'create trigger %I_updated before update on public.%I
         for each row execute function public.set_updated_at()', t, t);
  end loop;
end $$;

-- ---------- Defesa em profundidade: só admin publica ----------
create or replace function public.guard_publish()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  if new.status = 'published' and (tg_op = 'INSERT' or old.status is distinct from 'published') then
    if not public.is_admin() then
      raise exception 'Só o administrador pode publicar conteúdo';
    end if;
  end if;
  return new;
end $$;

do $$
declare t text;
begin
  foreach t in array array[
    'learning_paths','levels','subjects','topics','lessons','exercises','exam_papers'
  ] loop
    execute format(
      'create trigger %I_guard_publish before insert or update on public.%I
         for each row execute function public.guard_publish()', t, t);
  end loop;
end $$;

-- ====================== RLS ======================
alter table public.roles enable row level security;
alter table public.user_roles enable row level security;
alter table public.profiles enable row level security;
alter table public.teacher_students enable row level security;
alter table public.learning_paths enable row level security;
alter table public.levels enable row level security;
alter table public.subjects enable row level security;
alter table public.topics enable row level security;
alter table public.lessons enable row level security;
alter table public.lesson_blocks enable row level security;
alter table public.exercises enable row level security;
alter table public.exercise_answers enable row level security;
alter table public.exam_papers enable row level security;
alter table public.questions enable row level security;
alter table public.attempts enable row level security;
alter table public.mastery enable row level security;
alter table public.achievements enable row level security;
alter table public.user_achievements enable row level security;
alter table public.ai_conversations enable row level security;
alter table public.ai_messages enable row level security;
alter table public.ai_usage enable row level security;
alter table public.subscriptions enable row level security;

-- roles: leitura para autenticados; escrita só admin
create policy roles_read on public.roles for select to authenticated using (true);
create policy roles_admin on public.roles for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- user_roles: cada um vê os seus; admin gere. Nunca o próprio utilizador.
create policy user_roles_own on public.user_roles for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());
create policy user_roles_admin on public.user_roles for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- profiles
create policy profiles_select on public.profiles for select to authenticated
  using (id = (select auth.uid()) or public.is_admin() or public.is_teacher_of(id));
create policy profiles_update_own on public.profiles for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));
create policy profiles_admin on public.profiles for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- teacher_students
create policy teacher_students_select on public.teacher_students for select to authenticated
  using (teacher_id = (select auth.uid()) or student_id = (select auth.uid()) or public.is_admin());
create policy teacher_students_admin on public.teacher_students for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- Conteúdo hierárquico: autenticados leem publicado; admin tudo.
do $$
declare t text;
begin
  foreach t in array array['learning_paths','levels','subjects','topics','exam_papers'] loop
    execute format(
      'create policy %I on public.%I for select to authenticated
         using (status = ''published'' or public.is_admin())', t || '_read', t);
    execute format(
      'create policy %I on public.%I for all to authenticated
         using (public.is_admin()) with check (public.is_admin())', t || '_admin', t);
  end loop;
end $$;

-- Aulas: publicadas para todos; professor vê e edita os seus rascunhos; admin tudo.
create policy lessons_read on public.lessons for select to authenticated
  using (status = 'published' or public.is_admin() or created_by = (select auth.uid()));
create policy lessons_teacher_insert on public.lessons for insert to authenticated
  with check (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published');
create policy lessons_teacher_update on public.lessons for update to authenticated
  using (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published')
  with check (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published');
create policy lessons_admin on public.lessons for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- Blocos seguem a aula-mãe
create policy lesson_blocks_read on public.lesson_blocks for select to authenticated
  using (exists (select 1 from public.lessons l where l.id = lesson_id
    and (l.status = 'published' or public.is_admin() or l.created_by = (select auth.uid()))));
create policy lesson_blocks_teacher_write on public.lesson_blocks for all to authenticated
  using (public.is_teacher() and exists (select 1 from public.lessons l where l.id = lesson_id
    and l.created_by = (select auth.uid()) and l.status <> 'published'))
  with check (public.is_teacher() and exists (select 1 from public.lessons l where l.id = lesson_id
    and l.created_by = (select auth.uid()) and l.status <> 'published'));
create policy lesson_blocks_admin on public.lesson_blocks for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- Exercícios (enunciado e opções, sem solução)
create policy exercises_read on public.exercises for select to authenticated
  using (status = 'published' or public.is_admin() or created_by = (select auth.uid()));
create policy exercises_teacher_insert on public.exercises for insert to authenticated
  with check (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published');
create policy exercises_teacher_update on public.exercises for update to authenticated
  using (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published')
  with check (public.is_teacher() and created_by = (select auth.uid()) and status <> 'published');
create policy exercises_admin on public.exercises for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- Respostas certas: ninguém lê pelo cliente, exceto admin. O servidor usa a service role.
create policy exercise_answers_admin on public.exercise_answers for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

create policy questions_read on public.questions for select to authenticated
  using (exists (select 1 from public.exam_papers e where e.id = exam_paper_id
    and (e.status = 'published' or public.is_admin())));
create policy questions_admin on public.questions for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- Progresso: leitura própria, do professor ligado e do admin. Escrita só servidor.
create policy attempts_read on public.attempts for select to authenticated
  using (user_id = (select auth.uid()) or public.is_teacher_of(user_id) or public.is_admin());
create policy mastery_read on public.mastery for select to authenticated
  using (user_id = (select auth.uid()) or public.is_teacher_of(user_id) or public.is_admin());

create policy achievements_read on public.achievements for select to authenticated using (true);
create policy achievements_admin on public.achievements for all to authenticated
  using (public.is_admin()) with check (public.is_admin());
create policy user_achievements_read on public.user_achievements for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());

-- IA: leitura própria; escrita só servidor
create policy ai_conversations_read on public.ai_conversations for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());
create policy ai_conversations_delete_own on public.ai_conversations for delete to authenticated
  using (user_id = (select auth.uid()));
create policy ai_messages_read on public.ai_messages for select to authenticated
  using (exists (select 1 from public.ai_conversations c where c.id = conversation_id
    and (c.user_id = (select auth.uid()) or public.is_admin())));
create policy ai_usage_read on public.ai_usage for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());

create policy subscriptions_read on public.subscriptions for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());
create policy subscriptions_admin on public.subscriptions for all to authenticated
  using (public.is_admin()) with check (public.is_admin());
