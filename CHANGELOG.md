# Changelog — reembolso-viva

Todas as mudanças relevantes deste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/).

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
