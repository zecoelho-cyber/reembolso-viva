# Changelog — reembolso-viva

Todas as mudanças relevantes deste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/).

## [Fase 2 — ChatGPT] — 2026-06-24

### Adicionado
- Pasta `chatgpt/` com a versão para ChatGPT (Custom GPT): instruções do assistente
  (`INSTRUCOES-DO-GPT.md`), base de conhecimento pronta para upload (`chatgpt/conhecimento/`) e
  guia de montagem (`COMO-MONTAR-NO-CHATGPT.md`). Mesma base de conhecimento da versão Claude;
  é um consultor — sem armazenamento de dados nem acompanhamento de casos.

## [0.1.1] — 2026-06-24

### Corrigido
- Onboarding (`reembolso-viva-config`): blindado para **nunca** varrer arquivos, planilhas ou
  projetos do usuário, nem pré-preencher dados a partir do ambiente. Agora coleta tudo
  exclusivamente perguntando ao usuário, campo por campo (reforça a regra anti-inferência).
- Skill operacional: esclarecido que a busca por `config.local.yaml` se limita a esse arquivo,
  sem vasculhar o resto do computador.

## [0.1.0] — 2026-06-24

Primeira versão pública. Despersonalizada a partir de um fluxo pessoal de um
beneficiário, generalizada para qualquer Habilitado do plano Viva Mais Saúde.

### Adicionado
- Skill `reembolso-viva` — fluxo operacional: nova solicitação de adiantamento,
  acompanhamento (tracking), prestação de contas e organização para o IR.
- Skill `reembolso-viva-config` — onboarding conversacional que coleta os dados
  do usuário e grava o `config.local.yaml` (fica só no computador do usuário).
- Módulos de conhecimento (markdown) reaproveitáveis: regras do canal de e-mail,
  prazos/SLA, cobertura, checklist de documentos por tipo, prestação de contas,
  organização de arquivos e base legal (Acordo TST 2013 × Manual da operadora).
- Template do formulário de adiantamento em branco da Viva Mais.
- Cópia do Acordo Judicial TST 2013 (fonte primária pública).
- Script de preenchimento do formulário por sobreposição (PyMuPDF).
- `CONNECTORS.md` — modelo de conectores (e-mail / repositório / lembretes) que o
  usuário pluga conforme o que já tem.
- Scanner de privacidade (`scripts/verificar_privacidade.sh`).
- Manual de instalação no Claude em linguagem para leigos.

### Notas
- Não inclui nenhum dado pessoal de nenhum beneficiário.
- Integrações (e-mail, Notion, lembretes) são opcionais — o fluxo funciona só
  com arquivos locais.
