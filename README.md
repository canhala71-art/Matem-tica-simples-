# MenteMat

_A matemática começa na tua mente._ Plataforma de aprendizagem de matemática (React + TypeScript + Vite + Tailwind, Supabase, PWA).

## Estado atual (honesto)

| Parte | Estado |
|---|---|
| Base de dados Supabase (22 tabelas, RLS, gatilhos) | Criada e testada (`supabase/migrations/`) |
| Validador matemático (`shared/`) | 9 testes a passar (`npm test` em `app/`) |
| Edge Functions `validate-answer` e `ai-teacher` | Publicadas no Supabase, ainda sem teste ponta a ponta |
| Aplicação React (`app/`) | Código escrito, **ainda não compilada nem testada num navegador** |
| Conteúdos matemáticos | **Nenhuma aula/exercício ainda.** Só a estrutura dos 6 níveis (rascunho) |
| Publicação (Cloudflare Pages) | Por fazer: ver abaixo |

## Estrutura

```
app/                  Aplicação React (Vite)
shared/               Validador matemático (usado na app e na Edge Function)
supabase/migrations/  SQL: esquema, RLS, estrutura dos níveis, quota da IA
supabase/functions/   validate-answer, ai-teacher
docs/superpowers/specs/  Especificação do design
```

## Correr localmente

```bash
cd app
cp .env.example .env.local      # preenche URL e chave publishable do Supabase
npm install
npm test                        # validador matemático
npm run dev
```

## Primeiro administrador

1. Regista-te na app (fica "estudante").
2. No painel do Supabase → SQL Editor, corre (troca o email):

```sql
insert into public.user_roles (user_id, role)
select id, 'admin' from auth.users where email = 'O_TEU_EMAIL';
```

3. Entra no separador **Admin** para criar aulas e exercícios (ficam em rascunho) e publicá-los depois de rever.
4. Para ver os níveis e disciplinas na Academia, publica-os no separador **Conteúdo**.

## Professor IA

Sem chave, devolve respostas marcadas **"Demonstração — sem IA real"**. Para ativar:

```bash
supabase secrets set ANTHROPIC_API_KEY=...   # nunca no repositório nem no frontend
supabase secrets set AI_DAILY_LIMIT=20       # mensagens por utilizador/dia
```

## Publicar no Cloudflare Pages (grátis)

1. Cloudflare → Workers & Pages → Create → Pages → Connect to Git → escolhe o repositório.
2. Configuração de build:
   - Root directory: `app`
   - Build command: `npm run build`
   - Build output directory: `dist`
3. Variáveis de ambiente (Production): `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY`.
4. `app/public/_redirects` já trata das rotas SPA; a página 404 é tratada pela própria app.
5. No Supabase → Authentication → URL Configuration, define o **Site URL** e adiciona `https://O-TEU-SITE/redefinir` aos Redirect URLs.

O HTTPS é automático. Faz push para `main` e o deploy repete-se sozinho.

## Segurança

- Nenhuma chave privada no repositório. A chave publishable é pública por desenho; a proteção vem do RLS.
- Respostas certas e resoluções ficam em `exercise_answers`, ilegível pelos alunos; só `validate-answer` as lê.
- Só o administrador publica conteúdo (política RLS + gatilho).
- Menores: só se guarda "menor sim/não", sem data de nascimento.
- Todo conteúdo é original e só chega aos alunos depois de revisto e publicado por um administrador.

## Conteúdo do Nível 1 (rascunho)

`content/nivel-1/` tem 7 aulas e 45 exercícios, escritos de raiz (não copiados de nenhuma plataforma). Todas as respostas são calculadas em `tools/build_level1.py` com aritmética exata e conferidas contra o validador do site (`tools/check_content.mts`). Estão na base de dados como **rascunho**: revê-as no painel Admin e publica-as.
