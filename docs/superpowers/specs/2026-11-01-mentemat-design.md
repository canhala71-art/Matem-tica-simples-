# MenteMat — Especificação de design

Data: 2026-11-01 · Idioma inicial: português (i18n preparada para en/fr/es)
Slogan: A matemática começa na tua mente. · Assinatura: Aprende. Compreende. Raciocina. Domina.

## 1. Objetivo e decisões do utilizador
- Plataforma de aprendizagem de matemática do primário à universidade, começa em Angola.
- Construir os **seis níveis** antes de publicar (decisão do utilizador).
- Conteúdo: rascunhos escritos por Claude com texto **original** (plataformas angolanas e brasileiras servem só de referência de programa, nunca de cópia), cada exercício verificado com SymPy na criação, tudo em estado `rascunho` até aprovação do administrador.
- Validação de respostas em camadas: exata (MC, V/F, numérica) → algébrica em JavaScript → ponto SymPy opcional em runtime (desligado por defeito).
- Alojamento gratuito: GitHub + Cloudflare Pages (ou Vercel como alternativa) + Supabase Free.

## 2. Arquitetura
- Frontend: React + TypeScript + Vite + Tailwind, PWA, KaTeX, Lucide, Inter. Modo claro/escuro. Azul-marinho (principal), azul elétrico (secundária), roxo suave (destaque).
- Supabase: Postgres + Auth + RLS; Edge Functions `validate-answer` e `ai-teacher`.
- Pastas: `app/`, `supabase/migrations/`, `supabase/functions/`, `content/`, `tools/`, `docs/`.

## 3. Base de dados e permissões
- Tabelas: profiles, roles, learning_paths, levels, subjects, topics, lessons, lesson_blocks, exercises, questions, exercise_answers (privada), attempts, mastery, ai_conversations, ai_messages, ai_usage, achievements, exam_papers, subscriptions.
- Conteúdo com `status`: rascunho → revisão → publicado. Só administrador publica.
- RLS: estudante vê só os seus dados e conteúdo publicado; professor vê progresso dos alunos associados e propõe conteúdo; administrador gere tudo; papel de administrador atribuído só no servidor.
- Menores: recolha mínima, sem ranking público.
- Respostas certas em tabela separada, ilegível para o aluno.

## 4. Motor de exercícios e professor IA
- Tipos: escolha múltipla, numérica, algébrica, verdadeiro/falso, escrita, problema prático.
- Cada exercício: enunciado, dificuldade, assunto, resposta, explicação, resolução passo a passo, competência.
- Validação: normalização (espaços, vírgula decimal, frações, equivalência algébrica por avaliação numérica em pontos aleatórios + simplificação). Tolerância numérica configurável por exercício.
- Domínio: um assunto só é "dominado" após acertos consistentes em exercícios de dificuldades distintas e uma avaliação.
- MenteMat IA: Edge Function `ai-teacher`; sem chave `ANTHROPIC_API_KEY` devolve modo demonstração claramente identificado. Limite diário por utilizador (tabela `ai_usage`). Estilo socrático: pergunta, verifica compreensão. Fotos de exercícios: fase posterior, compatível com IA visual.

## 5. Offline, publicação, qualidade
- PWA instalável; cache de recursos; aulas e exercícios guardados em IndexedDB; fila de tentativas sincroniza quando voltar a internet; funcionalidades de IA avisam que precisam de ligação.
- Deploy: build `npm run build`, `_redirects` para SPA, página 404, `.env.example`, README. Nunca commitar credenciais.
- Testes: unitários (validador, domínio de competências), integração SQL/RLS, verificação de consola e responsividade.
- Não afirmar que o site está publicado sem confirmar o endereço.

## 6. Ciclos de implementação
1. Base: projeto, BD+RLS, autenticação, painel do estudante.
2. Academia: aulas, exercícios, motor matemático, conteúdo.
3. Professor IA, laboratório, desafios.
4. Administração, offline, publicação.

## 7. Limitações atuais
- Repositório GitHub `canhala71-art/MentMat` ainda sem acesso da sessão: o código fica local até o conector estar ligado.
- Sem conector Cloudflare: publicação por instruções ou via Vercel.
- Projeto Supabase ainda não existe; criação sujeita a confirmação de custo.
