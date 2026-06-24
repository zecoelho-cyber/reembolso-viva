---
name: reembolso-viva
description: |
  Ajuda beneficiários do plano Viva Mais Saúde a gerenciar o ciclo de adiantamentos e
  reembolsos: prepara o formulário de adiantamento, monta o e-mail no padrão que a operadora
  exige, controla prazos, organiza a prestação de contas e explica direitos com base no
  Acordo TST de 2013. USE ESTE SKILL quando o usuário mencionar: reembolso, adiantamento,
  Viva Mais, Viva Mais Saúde, plano de saúde, formulário de adiantamento, pedido médico,
  orçamento de laboratório, prestação de contas, nota fiscal médica, protocolo do plano,
  "preparar reembolso", "checar o plano", "respondeu o plano", "depositou", ou quando enviar
  pedidos médicos / orçamentos. Não é ferramenta oficial da operadora.
---

# Reembolso Viva Mais Saúde

Assistente para o ciclo completo de adiantamentos e reembolsos do plano Viva Mais Saúde.

> **Não é ferramenta oficial.** Não substitui aconselhamento jurídico ou médico. Confirme
> regras e prazos na fonte (operadora / Acordo). Ver `referencias/Acordo-2013-...pdf` e o
> arquivo `LICENSE` (aviso).

## Anti-invenção — regra inegociável

NUNCA invente dado factual (nome, CPF, e-mail, telefone, conta bancária, protocolo, valor,
data, CNPJ). Se faltar informação, **pergunte ao usuário**. Nunca preencha um campo com um
valor plausível. Todo dado que entra em formulário, e-mail ou registro vem do
`config.local.yaml` do usuário ou de um documento que ele forneceu — nunca de suposição.
Antes de enviar qualquer e-mail, mostre o conteúdo ao usuário e **aguarde a confirmação dele**.

## Pré-requisito: configuração do usuário

Os dados pessoais vivem em `config.local.yaml` (no computador do usuário, fora deste
repositório). Antes de qualquer ação que precise dos dados do usuário:

1. Procure por `config.local.yaml` na pasta-base do usuário.
2. Se **não existir**, acione o skill `reembolso-viva-config` (onboarding) para criá-lo —
   não tente adivinhar os dados.
3. Se existir, leia dele: identidade do titular, dependentes, pasta-base, e quais
   integrações estão ligadas (e-mail, repositório, lembretes).

## Conectores (o usuário pluga o que tem)

Este skill é agnóstico de ferramenta. Onde aparecer:

- `~~email` → o serviço de e-mail do usuário (Gmail, Outlook, etc.) ou, se nenhum estiver
  conectado, gere o texto do e-mail para ele copiar e enviar manualmente.
- `~~repositório` → onde o usuário guarda o estado dos casos (Notion, planilha ou apenas
  arquivos locais — o padrão).
- `~~lembretes` → onde criar lembretes de prazo (app de lembretes, calendário ou uma lista
  em arquivo — opcional).

Ver `CONNECTORS.md`. Se uma integração não estiver disponível, **degrade com elegância**:
faça a parte local (arquivos) e diga ao usuário o que ele precisa fazer à mão.

## Conhecimento de referência

Carregue o módulo certo conforme a necessidade (não leia todos de uma vez):

- `references/regras-canal.md` — como o e-mail com a operadora funciona (nunca dar reply,
  protocolo no assunto, nomes de anexo, regras para dependentes).
- `references/prazos-sla.md` — prazos, cálculo de dias úteis, consequências do atraso.
- `references/cobertura.md` — o que é coberto e o que não é.
- `references/checklist-documentos.md` — documentos por tipo de pedido.
- `references/prestacao-contas.md` — prestação, regra dos R$ 500, validação de recibo, IR.
- `references/organizacao-arquivos.md` — estrutura de pastas dos casos.
- `references/base-legal.md` — Acordo 2013 × Manual: direitos e os 12 conflitos.

---

## FASE 1 — Nova solicitação de adiantamento

Acione quando o usuário disser "preparar reembolso", "tenho consulta/exame", "novo pedido",
ou enviar pedidos médicos + orçamentos.

1. **Identifique o beneficiário:** titular ou qual dependente? Se não estiver claro,
   **pergunte**.
2. **Identifique o tipo:** consulta, terapia, exames, medicamento, internação/cirurgia,
   materiais. Veja a documentação necessária em `references/checklist-documentos.md`.
3. **Valide os orçamentos** (se exames/materiais): confira a validade. Vencido → peça novo
   antes de continuar.
4. **Crie a pasta do caso** conforme `references/organizacao-arquivos.md` e copie os anexos
   para as subpastas (`00_pedidos`, `01_orcamentos`, `02_solicitacao`).
5. **Preencha o formulário** com `scripts/preencher_formulario.py`, usando os dados do
   `config.local.yaml` + os dados do caso. O resultado vai para `02_solicitacao/`.
6. **Assinatura:** se houver imagem de assinatura no config do beneficiário, o script a
   insere; senão, oriente o usuário a imprimir/assinar ou assinar no celular e salvar o PDF
   assinado.
7. **Monte o pacote de envio (DOCS-TMP)** com os anexos renomeados em nomes descritivos e
   diferentes entre si (ver `references/regras-canal.md`, Regra 7).
8. **Escreva o corpo do e-mail** seguindo `references/regras-canal.md`:
   - assunto descritivo (com protocolo, se já houver); para dependente, nome + CPF do
     dependente no assunto e na assinatura;
   - salve o corpo em `02_solicitacao/email_body.txt`.
9. **Crie o rascunho no `~~email`** (apenas to/cc/assunto/corpo — o usuário anexa os PDFs e
   envia). Se não houver `~~email` conectado, entregue o texto para ele colar.
10. **Registre o caso no `~~repositório`** (ou no `status.yaml` local) com status "Pronta
    para envio".
11. **Crie lembretes no `~~lembretes`** (ou anote): cobrar protocolo (~D+3) e conferir
    pagamento (referência de 5 dias úteis).
12. **Mostre tudo ao usuário** e aguarde ele confirmar o envio. Quando confirmar, atualize o
    status para "Enviada".

## FASE 2 — Acompanhamento (tracking)

É uma conversa com a operadora: protocolo → análise → eventual pendência → aprovação/negativa
→ depósito. Atualize sempre os três lugares que estiverem em uso (pasta local +
`~~repositório` + `~~lembretes`).

**Eventos que o usuário relata** (reconheça em linguagem natural):

| O usuário diz | Ação |
|---|---|
| "chegou o protocolo XXX" | registre o protocolo; status → "Aguardando análise"; ajuste lembrete |
| "pediram mais um documento" | status → "Pendência aberta"; crie lembrete para responder |
| "respondi a pendência" | status → "Aguardando análise"; novo lembrete de prazo |
| "aprovaram, depósito DD/MM" | status → "Aprovada"; lembrete "conferir depósito" |
| "depositou / caiu na conta" | status → "Depositada"; **crie lembrete de prestação (D+60 corridos)** |
| "recebi negativa, motivo X" | status → "Negada"; ofereça checar `references/base-legal.md` se a negativa for de uma regra do Manual sem base no Acordo |

**Checar o plano (`~~email`):** quando o usuário pedir "vê se o plano respondeu", busque
e-mails da operadora (`central@atendimentovivamais.com.br`), classifique cada novo
(protocolo / pendência / aprovação / depósito / negativa), relacione ao caso e **mostre sua
interpretação antes de mudar qualquer status**. Não reapresente eventos já registrados.

## FASE 3 — Prestação de contas

Após o procedimento, dentro de 60 dias corridos do depósito. Siga
`references/prestacao-contas.md`: e-mail NOVO, assunto com protocolo, notas fiscais +
comprovantes, regra dos R$ 500. Guarde os documentos para o IR (gatilho = emissão da nota).

## FASE 4 — Imposto de Renda

Consolide as notas fiscais do ano (critério = data da nota) em
`ARQUIVOS_IR-[ANO]/`, para entregar ao contador. Ver `references/prestacao-contas.md`.

---

## Comandos rápidos

- `reembolso → nova consulta [médico]` — Fase 1, tipo consulta
- `reembolso → exames` — Fase 1, tipo exames
- `reembolso → checar plano` — Fase 2, leitura do e-mail
- `reembolso → recebi protocolo XXX` — registra protocolo
- `reembolso → depositou` — registra depósito + cria prestação D+60
- `reembolso → status` — lista casos abertos e prazos
- `reembolso → prestação [caso]` — Fase 3
- `reembolso → meus direitos` — abre `references/base-legal.md`

Linguagem natural sempre funciona — detecte a intenção.
