-- MenteMat: planos, pagamentos manuais, códigos de ativação, auditoria, quizzes.
-- Toda a lógica sensível corre no servidor (funções SECURITY DEFINER); o cliente nunca escreve diretamente.

create extension if not exists pgcrypto with schema extensions;

-- ---------- Configurações ----------
create table if not exists public.app_settings (
  key text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);
alter table public.app_settings enable row level security;
create policy settings_read on public.app_settings for select to authenticated using (true);
create policy settings_admin_write on public.app_settings for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

insert into public.app_settings(key, value) values
  ('whatsapp', '{"number":"937007567"}'),
  ('pay_multicaixa', '{"number":"","holder":"","active":false}'),
  ('pay_unitel', '{"number":"","holder":"","active":false}'),
  ('trial', '{"enabled":true,"days":7}'),
  ('code_validity_days', '{"days":30}'),
  ('free_quiz', '{"daily_limit":3,"difficulties":["facil","intermedio"]}'),
  ('support', '{"text":"Dúvidas? Fala connosco pelo WhatsApp."}')
on conflict (key) do nothing;

-- ---------- Planos ----------
create table if not exists public.plans (
  id text primary key,
  name text not null,
  audience text not null check (audience in ('student','teacher')),
  period text not null check (period in ('monthly','annual')),
  price_kz integer not null check (price_kz >= 0),
  days integer not null check (days > 0),
  active boolean not null default true,
  features jsonb not null default '[]',
  sort integer not null default 0
);
alter table public.plans enable row level security;
create policy plans_read on public.plans for select to anon, authenticated using (active or public.is_admin());
create policy plans_admin_write on public.plans for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

insert into public.plans(id, name, audience, period, price_kz, days, features, sort) values
 ('student_monthly','Premium Estudante','student','monthly',1500,30,
  '["Tudo do plano Free","Exercícios avançados","Resolução passo a passo","Professor IA","Testes e simulados","Histórico e estatísticas completos","Quizzes ilimitados, todas as categorias e dificuldades","Sem publicidade"]',1),
 ('student_annual','Premium Estudante','student','annual',12000,365,
  '["Tudo do plano Free","Exercícios avançados","Resolução passo a passo","Professor IA","Testes e simulados","Histórico e estatísticas completos","Quizzes ilimitados, todas as categorias e dificuldades","Sem publicidade"]',2),
 ('teacher_monthly','Premium Professor','teacher','monthly',3000,30,
  '["Tudo do Premium Estudante","Gestão de turmas e convite de alunos","Criação de exercícios, fichas e testes","Acompanhamento de resultados"]',3),
 ('teacher_annual','Premium Professor','teacher','annual',30000,365,
  '["Tudo do Premium Estudante","Gestão de turmas e convite de alunos","Criação de exercícios, fichas e testes","Acompanhamento de resultados"]',4)
on conflict (id) do nothing;

-- ---------- Assinaturas (tabela existente) ----------
do $$
declare c record;
begin
  for c in select conname from pg_constraint
           where conrelid = 'public.subscriptions'::regclass and contype = 'c' loop
    execute format('alter table public.subscriptions drop constraint %I', c.conname);
  end loop;
end $$;
alter table public.subscriptions
  add column if not exists plan_id text references public.plans(id),
  add column if not exists tier text not null default 'free',
  add column if not exists started_at timestamptz;
alter table public.subscriptions add constraint subscriptions_status_chk
  check (status in ('FREE','TRIAL','ACTIVE','EXPIRED','CANCELLED'));
alter table public.subscriptions add constraint subscriptions_tier_chk
  check (tier in ('free','student','teacher'));
create unique index if not exists subscriptions_user_uidx on public.subscriptions(user_id);
alter table public.subscriptions enable row level security;
do $$
declare p record;
begin
  for p in select policyname from pg_policies where schemaname='public' and tablename='subscriptions' loop
    execute format('drop policy %I on public.subscriptions', p.policyname);
  end loop;
end $$;
create policy subs_read_own on public.subscriptions for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());
-- sem políticas de escrita: só funções do servidor alteram o plano.

create table if not exists public.trials (
  user_id uuid primary key references auth.users(id) on delete cascade,
  started_at timestamptz not null default now(),
  ends_at timestamptz not null
);
alter table public.trials enable row level security;
create policy trials_read_own on public.trials for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());

alter table public.profiles add column if not exists suspended boolean not null default false;

-- ---------- Pedidos de pagamento ----------
create table if not exists public.payment_requests (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  plan_id text not null references public.plans(id),
  amount_kz integer not null,
  method text not null check (method in ('multicaixa','unitel')),
  reference text,
  notes text,
  status text not null default 'PENDING' check (status in ('PENDING','CONFIRMED','REJECTED','CANCELLED')),
  admin_note text,
  decided_by uuid references auth.users(id),
  decided_at timestamptz,
  created_at timestamptz not null default now()
);
create index if not exists payment_requests_user_idx on public.payment_requests(user_id, created_at desc);
create index if not exists payment_requests_status_idx on public.payment_requests(status, created_at desc);
create index if not exists payment_requests_plan_idx on public.payment_requests(plan_id);
alter table public.payment_requests enable row level security;
create policy pay_read on public.payment_requests for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());

-- ---------- Códigos de ativação ----------
create table if not exists public.activation_codes (
  id uuid primary key default gen_random_uuid(),
  code_hash text not null unique,
  code_hint text not null,
  user_id uuid not null references auth.users(id) on delete cascade,
  plan_id text not null references public.plans(id),
  payment_request_id uuid not null unique references public.payment_requests(id),
  status text not null default 'ISSUED' check (status in ('ISSUED','USED','EXPIRED','REVOKED')),
  issued_by uuid references auth.users(id),
  issued_at timestamptz not null default now(),
  expires_at timestamptz not null,
  used_at timestamptz,
  revoked_at timestamptz
);
create index if not exists activation_codes_user_idx on public.activation_codes(user_id);
create index if not exists subscriptions_plan_idx on public.subscriptions(plan_id);
create index if not exists activation_codes_plan_idx on public.activation_codes(plan_id);
alter table public.activation_codes enable row level security;
create policy codes_read on public.activation_codes for select to authenticated
  using (user_id = (select auth.uid()) or public.is_admin());

create table if not exists public.code_attempts (
  id bigserial primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  success boolean not null,
  at timestamptz not null default now()
);
create index if not exists code_attempts_user_idx on public.code_attempts(user_id, at desc);
alter table public.code_attempts enable row level security;

-- ---------- Auditoria ----------
create table if not exists public.audit_log (
  id bigserial primary key,
  actor uuid,
  action text not null,
  entity text,
  entity_id text,
  details jsonb not null default '{}',
  created_at timestamptz not null default now()
);
alter table public.audit_log enable row level security;
create policy audit_admin_read on public.audit_log for select to authenticated using (public.is_admin());

create or replace function public.audit(_action text, _entity text, _id text, _details jsonb)
returns void language sql security definer set search_path = '' as $$
  insert into public.audit_log(actor, action, entity, entity_id, details)
  values (auth.uid(), _action, _entity, _id, coalesce(_details,'{}'::jsonb));
$$;

create or replace function public.audit_trigger() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  perform public.audit(
    case tg_table_name when 'plans' then 'plan_alterado' else 'configuracao_alterada' end,
    tg_table_name,
    coalesce((to_jsonb(new)->>'id'), (to_jsonb(new)->>'key')),
    jsonb_build_object('antes', to_jsonb(old), 'depois', to_jsonb(new)));
  return new;
end $$;
create trigger plans_audit after update on public.plans
  for each row when (old.* is distinct from new.*) execute function public.audit_trigger();
create trigger settings_audit after update on public.app_settings
  for each row when (old.* is distinct from new.*) execute function public.audit_trigger();

-- ---------- Acesso efetivo ----------
create or replace function public.user_access(_uid uuid) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare s record;
begin
  select * into s from public.subscriptions where user_id = _uid;
  if s is null then
    return jsonb_build_object('tier','free','status','FREE','plan_id',null,'started_at',null,'ends_at',null,'days_left',0);
  end if;
  if s.status in ('ACTIVE','TRIAL') and s.current_period_end is not null and s.current_period_end > now() then
    return jsonb_build_object('tier', s.tier, 'status', s.status, 'plan_id', s.plan_id,
      'started_at', s.started_at, 'ends_at', s.current_period_end,
      'days_left', ceil(extract(epoch from (s.current_period_end - now())) / 86400)::int);
  end if;
  return jsonb_build_object('tier','free',
    'status', case when s.status in ('ACTIVE','TRIAL') then 'EXPIRED' else s.status end,
    'plan_id', s.plan_id, 'started_at', s.started_at, 'ends_at', s.current_period_end, 'days_left', 0);
end $$;

create or replace function public.get_my_access() returns jsonb
language sql stable security definer set search_path = '' as $$
  select public.user_access((select auth.uid()));
$$;

-- ---------- Pedido de pagamento (cliente) ----------
create or replace function public.create_payment_request(_plan_id text, _method text, _reference text, _notes text)
returns jsonb language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); p record; m jsonb; r public.payment_requests;
begin
  if uid is null then raise exception 'Inicia sessão para continuar.'; end if;
  if _method not in ('multicaixa','unitel') then raise exception 'Método de pagamento inválido.'; end if;
  select * into p from public.plans where id = _plan_id and active;
  if p is null then raise exception 'Plano indisponível.'; end if;
  select value into m from public.app_settings where key = 'pay_' || _method;
  if m is null or not coalesce((m->>'active')::boolean, false) or coalesce(m->>'number','') = '' then
    raise exception 'Este método de pagamento ainda não está disponível.';
  end if;
  if (select count(*) from public.payment_requests where user_id = uid and status = 'PENDING') >= 3 then
    raise exception 'Já tens pedidos pendentes. Aguarda a confirmação antes de criar outro.';
  end if;
  insert into public.payment_requests(user_id, plan_id, amount_kz, method, reference, notes)
  values (uid, p.id, p.price_kz, _method, left(nullif(trim(_reference),''),80), left(nullif(trim(_notes),''),500))
  returning * into r;
  return jsonb_build_object('id', r.id, 'amount_kz', r.amount_kz, 'plan', p.name, 'period', p.period,
    'method', r.method, 'status', r.status);
end $$;

create or replace function public.cancel_payment_request(_id uuid) returns void
language plpgsql security definer set search_path = '' as $$
begin
  update public.payment_requests set status='CANCELLED', decided_at=now()
  where id=_id and user_id=auth.uid() and status='PENDING';
  if not found then raise exception 'Pedido não encontrado ou já tratado.'; end if;
end $$;

-- ---------- Administração de pagamentos e códigos ----------
create or replace function public.admin_decide_payment(_id uuid, _decision text, _note text)
returns void language plpgsql security definer set search_path = '' as $$
declare r public.payment_requests;
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  if _decision not in ('CONFIRMED','REJECTED','CANCELLED','PENDING') then raise exception 'Decisão inválida.'; end if;
  select * into r from public.payment_requests where id=_id for update;
  if r is null then raise exception 'Pedido não encontrado.'; end if;
  if r.status='CONFIRMED' and _decision <> 'CONFIRMED' and
     exists (select 1 from public.activation_codes where payment_request_id=_id and status in ('ISSUED','USED')) then
    raise exception 'Já existe um código para este pagamento; revoga-o primeiro.';
  end if;
  update public.payment_requests set status=_decision, admin_note=left(_note,500),
    decided_by=auth.uid(), decided_at=now() where id=_id;
  perform public.audit(case _decision when 'CONFIRMED' then 'pagamento_confirmado'
    when 'REJECTED' then 'pagamento_rejeitado' else 'pagamento_'||lower(_decision) end,
    'payment_requests', _id::text, jsonb_build_object('nota',_note,'valor',r.amount_kz,'utilizador',r.user_id));
end $$;

create or replace function public.admin_issue_code(_payment_id uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare r public.payment_requests; raw text; days int; c text;
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  select * into r from public.payment_requests where id=_payment_id for update;
  if r is null then raise exception 'Pedido não encontrado.'; end if;
  if r.status <> 'CONFIRMED' then raise exception 'O pagamento tem de estar confirmado antes de gerar o código.'; end if;
  if exists (select 1 from public.activation_codes where payment_request_id=_payment_id and status in ('ISSUED','USED')) then
    raise exception 'Já foi emitido um código para este pagamento.';
  end if;
  -- se existir um código revogado/expirado antigo, remove a ligação para permitir reemissão
  delete from public.activation_codes where payment_request_id=_payment_id and status in ('REVOKED','EXPIRED');
  select coalesce((value->>'days')::int, 30) into days from public.app_settings where key='code_validity_days';
  raw := upper(encode(extensions.gen_random_bytes(10), 'hex'));   -- 80 bits de aleatoriedade
  c := 'MM-' || substr(raw,1,5) || '-' || substr(raw,6,5) || '-' || substr(raw,11,5) || '-' || substr(raw,16,5);
  insert into public.activation_codes(code_hash, code_hint, user_id, plan_id, payment_request_id, issued_by, expires_at)
  values (encode(extensions.digest(c,'sha256'),'hex'), right(c,4), r.user_id, r.plan_id, r.id, auth.uid(),
          now() + make_interval(days => days));
  perform public.audit('codigo_gerado','activation_codes',_payment_id::text,
    jsonb_build_object('utilizador',r.user_id,'plano',r.plan_id,'final',right(c,4)));
  return jsonb_build_object('code', c, 'plan_id', r.plan_id, 'user_id', r.user_id);
end $$;

create or replace function public.admin_revoke_code(_id uuid) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  update public.activation_codes set status='REVOKED', revoked_at=now() where id=_id and status='ISSUED';
  if not found then raise exception 'Só é possível revogar códigos emitidos e ainda não usados.'; end if;
  perform public.audit('codigo_revogado','activation_codes',_id::text,'{}');
end $$;

create or replace function public.admin_set_suspended(_user uuid, _value boolean) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  if _user = auth.uid() then raise exception 'Não podes suspender a tua própria conta.'; end if;
  update public.profiles set suspended=_value where id=_user;
  perform public.audit(case when _value then 'conta_suspensa' else 'conta_reativada' end,'profiles',_user::text,'{}');
end $$;

create or replace function public.admin_stats() returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare j jsonb;
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  select jsonb_build_object(
    'utilizadores', (select count(*) from public.profiles),
    'professores', (select count(*) from public.subscriptions where tier='teacher' and status='ACTIVE' and current_period_end>now()),
    'premium_ativos', (select count(*) from public.subscriptions where status='ACTIVE' and current_period_end>now()),
    'assinaturas_expiradas', (select count(*) from public.subscriptions where status in ('ACTIVE','TRIAL') and current_period_end<=now()),
    'testes_ativos', (select count(*) from public.subscriptions where status='TRIAL' and current_period_end>now()),
    'pagamentos_pendentes', (select count(*) from public.payment_requests where status='PENDING'),
    'pagamentos_confirmados', (select count(*) from public.payment_requests where status='CONFIRMED'),
    'receita_confirmada_kz', (select coalesce(sum(amount_kz),0) from public.payment_requests where status='CONFIRMED'),
    'quizzes_realizados', (select count(*) from public.quiz_sessions where finished_at is not null)
  ) into j;
  j := j || jsonb_build_object('gratuitos', (j->>'utilizadores')::int - (j->>'premium_ativos')::int - (j->>'testes_ativos')::int);
  return j;
end $$;

-- ---------- Resgate do código (atómico, com limite de tentativas) ----------
create or replace function public.redeem_code(_code text) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); h text; ac public.activation_codes; p public.plans;
        s public.subscriptions; base timestamptz; new_end timestamptz; fails int;
begin
  if uid is null then raise exception 'Inicia sessão para continuar.'; end if;
  select count(*) into fails from public.code_attempts
    where user_id=uid and not success and at > now() - interval '15 minutes';
  if fails >= 5 then raise exception 'Demasiadas tentativas. Tenta novamente dentro de alguns minutos.'; end if;

  h := encode(extensions.digest(upper(regexp_replace(coalesce(_code,''),'\s','','g')),'sha256'),'hex');
  select * into ac from public.activation_codes where code_hash=h for update;

  if ac is null or ac.user_id <> uid or ac.status <> 'ISSUED' then
    insert into public.code_attempts(user_id, success) values (uid,false);
    return jsonb_build_object('error','Código inválido ou indisponível.');
  end if;
  if ac.expires_at <= now() then
    update public.activation_codes set status='EXPIRED' where id=ac.id;
    insert into public.code_attempts(user_id, success) values (uid,false);
    return jsonb_build_object('error','Código inválido ou indisponível.');
  end if;
  select * into p from public.plans where id=ac.plan_id;

  select * into s from public.subscriptions where user_id=uid for update;
  base := now();
  if s is not null and s.status='ACTIVE' and s.tier=p.audience and s.current_period_end > now() then
    base := s.current_period_end;           -- renovação antecipada soma ao período restante
  end if;
  new_end := base + make_interval(days => p.days);

  insert into public.subscriptions(user_id, plan, plan_id, tier, status, started_at, current_period_end)
  values (uid, p.id, p.id, p.audience, 'ACTIVE', now(), new_end)
  on conflict (user_id) do update set plan=excluded.plan, plan_id=excluded.plan_id, tier=excluded.tier,
    status='ACTIVE', started_at=case when base=now() then now() else public.subscriptions.started_at end,
    current_period_end=excluded.current_period_end;

  update public.activation_codes set status='USED', used_at=now() where id=ac.id;
  insert into public.code_attempts(user_id, success) values (uid,true);
  perform public.audit('premium_ativado','subscriptions',uid::text,
    jsonb_build_object('plano',p.id,'ate',new_end,'codigo_final',ac.code_hint));
  return public.user_access(uid);
end $$;

-- ---------- Teste gratuito (uma vez por conta) ----------
create or replace function public.start_trial() returns jsonb
language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); t jsonb; d int; s public.subscriptions; e timestamptz;
begin
  if uid is null then raise exception 'Inicia sessão para continuar.'; end if;
  select value into t from public.app_settings where key='trial';
  if not coalesce((t->>'enabled')::boolean,false) then raise exception 'O teste gratuito não está disponível neste momento.'; end if;
  if exists (select 1 from public.trials where user_id=uid) then raise exception 'Já usaste o teste gratuito nesta conta.'; end if;
  select * into s from public.subscriptions where user_id=uid;
  if s is not null and s.status='ACTIVE' and s.current_period_end > now() then
    raise exception 'Já tens um plano Premium ativo.';
  end if;
  d := coalesce((t->>'days')::int, 7);
  e := now() + make_interval(days => d);
  insert into public.trials(user_id, ends_at) values (uid, e);
  insert into public.subscriptions(user_id, plan, tier, status, started_at, current_period_end)
  values (uid, 'trial', 'student', 'TRIAL', now(), e)
  on conflict (user_id) do update set plan='trial', plan_id=null, tier='student', status='TRIAL',
    started_at=now(), current_period_end=e;
  perform public.audit('teste_iniciado','trials',uid::text,jsonb_build_object('dias',d));
  return public.user_access(uid);
end $$;

-- ---------- Quizzes ----------
create table if not exists public.quiz_questions (
  id uuid primary key default gen_random_uuid(),
  category text not null,
  difficulty text not null check (difficulty in ('facil','intermedio','avancado')),
  statement text not null,
  options jsonb not null check (jsonb_typeof(options)='array' and jsonb_array_length(options)=4),
  explanation text not null,
  status text not null default 'draft' check (status in ('draft','published','archived')),
  created_by uuid references auth.users(id),
  created_at timestamptz not null default now()
);
create index if not exists quiz_questions_filter_idx on public.quiz_questions(status, category, difficulty);
create table if not exists public.quiz_answers (
  question_id uuid primary key references public.quiz_questions(id) on delete cascade,
  correct_index smallint not null check (correct_index between 0 and 3)
);
create table if not exists public.quiz_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  category text, difficulty text,
  question_ids uuid[] not null,
  started_at timestamptz not null default now(),
  finished_at timestamptz,
  correct int, total int, points int, seconds int
);
create index if not exists quiz_sessions_user_idx on public.quiz_sessions(user_id, started_at desc);
create table if not exists public.quiz_session_answers (
  session_id uuid references public.quiz_sessions(id) on delete cascade,
  question_id uuid references public.quiz_questions(id) on delete cascade,
  chosen smallint not null,
  is_correct boolean not null,
  primary key (session_id, question_id)
);
create index if not exists quiz_sa_question_idx on public.quiz_session_answers(question_id);
alter table public.quiz_questions enable row level security;
alter table public.quiz_answers enable row level security;
alter table public.quiz_sessions enable row level security;
alter table public.quiz_session_answers enable row level security;
create policy qq_admin on public.quiz_questions for all to authenticated
  using (public.is_admin()) with check (public.is_admin());
create policy qa_admin on public.quiz_answers for all to authenticated
  using (public.is_admin()) with check (public.is_admin());
create policy qs_read on public.quiz_sessions for select to authenticated
  using (user_id=(select auth.uid()) or public.is_admin());
create policy qsa_read on public.quiz_session_answers for select to authenticated
  using (public.is_admin() or exists (select 1 from public.quiz_sessions s
        where s.id=session_id and s.user_id=(select auth.uid())));

create or replace function public.start_quiz(_category text, _difficulty text, _n int) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); acc jsonb; fq jsonb; ids uuid[]; sid uuid; qs jsonb; today_cnt int;
begin
  if uid is null then raise exception 'Inicia sessão para continuar.'; end if;
  if _n not in (5,10,20) then raise exception 'Escolhe 5, 10 ou 20 perguntas.'; end if;
  if _difficulty is not null and _difficulty not in ('facil','intermedio','avancado') then raise exception 'Dificuldade inválida.'; end if;
  acc := public.user_access(uid);
  if acc->>'tier' = 'free' then
    select value into fq from public.app_settings where key='free_quiz';
    select count(*) into today_cnt from public.quiz_sessions
      where user_id=uid and started_at >= date_trunc('day', now());
    if today_cnt >= coalesce((fq->>'daily_limit')::int, 3) then
      raise exception 'Atingiste o limite diário de quizzes gratuitos. Volta amanhã ou passa a Premium.';
    end if;
    if _difficulty is null or not ((fq->'difficulties') ? _difficulty) then
      raise exception 'Esta dificuldade é exclusiva do plano Premium.';
    end if;
  end if;
  select array_agg(id) into ids from (
    select id from public.quiz_questions
    where status='published' and (_category is null or category=_category)
      and (_difficulty is null or difficulty=_difficulty)
    order by random() limit _n) q;
  if ids is null then raise exception 'Ainda não há perguntas para esta escolha.'; end if;
  insert into public.quiz_sessions(user_id, category, difficulty, question_ids, total)
  values (uid, _category, _difficulty, ids, array_length(ids,1)) returning id into sid;
  select jsonb_agg(jsonb_build_object('id',q.id,'statement',q.statement,'options',q.options,
           'category',q.category,'difficulty',q.difficulty) order by array_position(ids,q.id))
    into qs from public.quiz_questions q where q.id = any(ids);
  return jsonb_build_object('session_id', sid, 'questions', qs);
end $$;

create or replace function public.quiz_answer(_session uuid, _question uuid, _chosen int) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); s public.quiz_sessions; ci smallint; ex text; ok boolean;
begin
  select * into s from public.quiz_sessions where id=_session and user_id=uid;
  if s is null or s.finished_at is not null then raise exception 'Sessão inválida.'; end if;
  if not (_question = any(s.question_ids)) then raise exception 'Pergunta inválida.'; end if;
  if _chosen not between 0 and 3 then raise exception 'Resposta inválida.'; end if;
  if exists (select 1 from public.quiz_session_answers where session_id=_session and question_id=_question) then
    raise exception 'Esta pergunta já foi respondida.';
  end if;
  select a.correct_index, q.explanation into ci, ex
    from public.quiz_answers a join public.quiz_questions q on q.id=a.question_id where a.question_id=_question;
  ok := (ci = _chosen);
  insert into public.quiz_session_answers(session_id, question_id, chosen, is_correct) values (_session,_question,_chosen,ok);
  return jsonb_build_object('is_correct', ok, 'correct_index', ci, 'explanation', ex);
end $$;

create or replace function public.finish_quiz(_session uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare uid uuid := auth.uid(); s public.quiz_sessions; c int; secs int; det jsonb;
begin
  select * into s from public.quiz_sessions where id=_session and user_id=uid for update;
  if s is null then raise exception 'Sessão inválida.'; end if;
  if s.finished_at is null then
    select count(*) filter (where is_correct) into c from public.quiz_session_answers where session_id=_session;
    secs := extract(epoch from (now()-s.started_at))::int;
    update public.quiz_sessions set finished_at=now(), correct=c, points=c*10, seconds=secs where id=_session
      returning * into s;
  end if;
  select jsonb_agg(jsonb_build_object('statement',q.statement,'options',q.options,'chosen',a.chosen,
           'is_correct',a.is_correct,'correct_index',k.correct_index,'explanation',q.explanation))
    into det from public.quiz_session_answers a
    join public.quiz_questions q on q.id=a.question_id
    join public.quiz_answers k on k.question_id=q.id where a.session_id=_session;
  return jsonb_build_object('correct', s.correct, 'wrong', s.total - s.correct, 'total', s.total,
    'points', s.points, 'seconds', s.seconds,
    'percent', round(100.0 * s.correct / nullif(s.total,0)), 'details', coalesce(det,'[]'::jsonb));
end $$;

create or replace function public.daily_challenge() returns jsonb
language sql stable security definer set search_path = '' as $$
  select jsonb_build_object('id',q.id,'statement',q.statement,'options',q.options,
    'category',q.category,'difficulty',q.difficulty,
    'available', (select count(*) from public.quiz_questions where status='published'))
  from public.quiz_questions q where q.status='published'
  order by md5(q.id::text || current_date::text) limit 1;
$$;

create or replace function public.daily_challenge_answer(_question uuid, _chosen int) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare ci smallint; ex text;
begin
  select a.correct_index, q.explanation into ci, ex from public.quiz_answers a
    join public.quiz_questions q on q.id=a.question_id where a.question_id=_question and q.status='published';
  if ci is null then raise exception 'Pergunta inválida.'; end if;
  return jsonb_build_object('is_correct', ci=_chosen, 'correct_index', ci, 'explanation', ex);
end $$;

create or replace function public.quiz_leaderboard(_category text) returns table(display_name text, points bigint, quizzes bigint)
language sql stable security definer set search_path = '' as $$
  select p.display_name, sum(s.points)::bigint, count(*)::bigint
  from public.quiz_sessions s join public.profiles p on p.id = s.user_id
  where s.finished_at is not null and (_category is null or s.category=_category)
    and coalesce(p.preferences->>'ranking','false') = 'true' and not p.suspended
  group by p.display_name order by 2 desc limit 20;
$$;

-- ---------- Permissões de execução ----------
do $$
declare f text;
begin
  foreach f in array array[
    'audit(text,text,text,jsonb)','audit_trigger()','user_access(uuid)'] loop
    execute format('revoke all on function public.%s from public, anon, authenticated', f);
  end loop;
  foreach f in array array[
    'get_my_access()','create_payment_request(text,text,text,text)','cancel_payment_request(uuid)',
    'admin_decide_payment(uuid,text,text)','admin_issue_code(uuid)','admin_revoke_code(uuid)',
    'admin_set_suspended(uuid,boolean)','admin_stats()','redeem_code(text)','start_trial()',
    'start_quiz(text,text,int)','quiz_answer(uuid,uuid,int)','finish_quiz(uuid)',
    'daily_challenge()','daily_challenge_answer(uuid,int)','quiz_leaderboard(text)'] loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;

-- ---------- Perguntas iniciais (publicadas só após revisão do administrador) ----------
do $$
declare r record;
declare qid uuid;
begin
  for r in select * from (values
    ('aritmetica','facil','Quanto é $\frac{3}{5}+\frac{1}{5}$?','["4/5","4/10","3/10","2/5"]',0,'Os denominadores são iguais: somam-se os numeradores (3+1=4) e mantém-se o denominador 5. Resultado: 4/5.'),
    ('aritmetica','facil','Quanto é 15% de 200?','["20","30","35","15"]',1,'15% = 15/100. Então 200 × 15 ÷ 100 = 30.'),
    ('aritmetica','intermedio','Quanto é $2^5 \cdot 2^3$?','["64","128","256","512"]',2,'Na multiplicação de potências com a mesma base, somam-se os expoentes: 2^(5+3) = 2^8 = 256.'),
    ('matematica_basica','facil','Quanto é 7 × 8?','["54","56","58","63"]',1,'7 × 8 = 56.'),
    ('algebra','facil','Resolve: 2x + 6 = 14. Qual é o valor de x?','["3","4","5","8"]',1,'Subtrai 6 aos dois lados: 2x = 8. Divide por 2: x = 4.'),
    ('algebra','intermedio','Qual é a soma das soluções de $x^2-5x+6=0$?','["-5","5","6","1"]',1,'Fatorizando: (x-2)(x-3)=0, logo x=2 ou x=3. A soma é 2+3 = 5.'),
    ('algebra','avancado','Desenvolve $(x+3)^2$.','["x² + 9","x² + 6x + 9","x² + 3x + 9","x² + 6x + 6"]',1,'(x+3)² = x² + 2·x·3 + 3² = x² + 6x + 9.'),
    ('geometria','facil','Qual é a área de um retângulo com 8 cm de comprimento e 5 cm de largura?','["13 cm²","26 cm²","40 cm²","80 cm²"]',2,'Área = comprimento × largura = 8 × 5 = 40 cm².'),
    ('geometria','intermedio','Um triângulo retângulo tem catetos 6 e 8. Quanto mede a hipotenusa?','["10","12","14","48"]',0,'Pitágoras: h² = 6² + 8² = 36 + 64 = 100, logo h = 10.'),
    ('geometria','avancado','Qual é a soma dos ângulos internos de um hexágono?','["540°","720°","900°","360°"]',1,'Soma = (n−2)·180° = (6−2)·180° = 720°.'),
    ('trigonometria','intermedio','Qual é o valor de sen 30°?','["√3/2","1/2","1","√2/2"]',1,'sen 30° = 1/2 (valor notável).'),
    ('trigonometria','avancado','Se x é um ângulo agudo e sen x = 3/5, quanto vale cos x?','["3/4","4/5","5/4","1/5"]',1,'sen²x + cos²x = 1 → cos²x = 1 − 9/25 = 16/25. Como x é agudo, cos x = 4/5.'),
    ('funcoes','facil','Se f(x) = 2x + 1, quanto vale f(3)?','["5","6","7","9"]',2,'f(3) = 2·3 + 1 = 7.'),
    ('funcoes','intermedio','Qual é o declive da reta y = −3x + 4?','["4","3","-3","-4"]',2,'Em y = mx + b, o declive é m. Aqui m = −3.'),
    ('estatistica','facil','Qual é a média de 4, 6, 8, 10 e 12?','["6","8","9","10"]',1,'Soma = 40; 40 ÷ 5 = 8.'),
    ('estatistica','intermedio','Qual é a mediana de 3, 9, 5, 7 e 1?','["5","7","3","9"]',0,'Ordenando: 1, 3, 5, 7, 9. O valor do meio é 5.'),
    ('probabilidade','facil','Ao lançar um dado normal, qual é a probabilidade de sair um número par?','["1/6","1/3","1/2","2/3"]',2,'Pares: 2, 4, 6 → 3 casos em 6 = 1/2.'),
    ('probabilidade','intermedio','Ao lançar duas moedas, qual é a probabilidade de saírem duas caras?','["1/2","1/4","1/3","1/8"]',1,'1/2 × 1/2 = 1/4.'),
    ('probabilidade','avancado','Um saco tem 3 bolas vermelhas e 2 azuis. Tiram-se 2 sem reposição. Qual é a probabilidade de serem ambas vermelhas?','["3/10","9/25","2/5","3/5"]',0,'3/5 × 2/4 = 6/20 = 3/10.'),
    ('matematica_avancada','avancado','Qual é a derivada de $x^3$?','["x²","3x²","3x","x³/3"]',1,'Regra da potência: (xⁿ)′ = n·xⁿ⁻¹, logo (x³)′ = 3x².'),
    ('matematica_avancada','avancado','Qual é o resultado de $\int 2x\,dx$?','["x² + C","2 + C","x + C","2x² + C"]',0,'A primitiva de 2x é x², mais a constante C.'),
    ('preparacao_exames','intermedio','Calcula $\sqrt{144}+3^2$.','["15","21","27","153"]',1,'√144 = 12 e 3² = 9; 12 + 9 = 21.')
  ) as t(category, difficulty, statement, options, correct, explanation) loop
    insert into public.quiz_questions(category, difficulty, statement, options, explanation, status)
    values (r.category, r.difficulty, r.statement, r.options::jsonb, r.explanation, 'draft') returning id into qid;
    insert into public.quiz_answers(question_id, correct_index) values (qid, r.correct);
  end loop;
end $$;

-- Ajustes finais (pedido de 04/11): motivo obrigatório ao rejeitar e registo de referência pelo admin.
-- (já aplicados na base via execute_sql; admin_decide_payment passa a exigir motivo com REJECTED)
create or replace function public.admin_set_reference(_id uuid, _reference text)
returns void language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_admin() then raise exception 'Sem permissão.'; end if;
  update public.payment_requests set reference = left(btrim(_reference), 80) where id = _id;
  if not found then raise exception 'Pedido não encontrado.'; end if;
  perform public.audit('referencia_registada', 'payment_requests', _id::text, jsonb_build_object('referencia', left(btrim(_reference), 80)));
end $$;
revoke execute on function public.admin_set_reference(uuid, text) from public, anon;
grant execute on function public.admin_set_reference(uuid, text) to authenticated;
