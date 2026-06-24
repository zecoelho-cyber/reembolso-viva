---
name: reembolso-viva-config
description: |
  Configuração inicial (onboarding) do assistente de reembolso Viva Mais Saúde. Conduz o
  usuário por uma conversa simples que coleta os dados pessoais dele e grava o arquivo
  config.local.yaml no computador dele — esse arquivo NUNCA sai do computador. USE ESTE SKILL
  quando o usuário disser "configurar reembolso", "primeira vez", "começar a usar o
  reembolso", "meus dados", "configurar o plano", ou quando o skill reembolso-viva não
  encontrar um config.local.yaml. Coleta nome, CPF, contato, dados bancários, dependentes,
  pasta de trabalho e quais integrações usar.
---

# Configuração do assistente de reembolso (onboarding)

Conduz o usuário pela primeira configuração e grava os dados dele em `config.local.yaml`.
Objetivo: depois disso, o skill `reembolso-viva` funciona com os dados da pessoa, sem que
ela precise repetir nada.

## Princípios

- **Nunca invente nada.** Todo dado vem da boca do usuário. Se ele não souber um campo agora,
  deixe em branco e siga — dá para completar depois.
- **Um assunto de cada vez.** Pergunte em blocos curtos, confirme, avance. Não despeje um
  formulário gigante.
- **Linguagem simples.** O usuário pode não ter familiaridade técnica. Explique o porquê de
  cada dado em uma frase.
- **Privacidade primeiro.** Diga, no começo, que esses dados ficam **só no computador dele**,
  dentro do arquivo `config.local.yaml`, e que esse arquivo nunca é enviado para lugar nenhum.

## Roteiro da conversa

Use `config.example.yaml` (na raiz do repositório) como modelo da estrutura final.

### 1. Abertura
Explique em 2-3 frases o que o assistente faz e que você vai pedir alguns dados, que ficam só
no computador dele. Pergunte se pode começar.

### 2. Pasta de trabalho
Pergunte onde ele quer guardar os casos (ex.: uma pasta "Reembolsos-Viva" nos Documentos).
Esse será o `pasta_base`. Crie a pasta se ele autorizar.

### 3. Titular (a própria pessoa)
Colete, um a um: nome completo; CPF; endereço (rua, bairro, cidade, UF, CEP); e-mail;
telefone. Explique que esses dados vão no formulário e no e-mail.

### 4. Dados bancários (para receber o depósito)
Colete: nome do titular da conta; CPF do titular da conta; banco; agência; conta; chave Pix.
Lembre que a conta precisa ser do próprio beneficiário (mesmo CPF) — ver regra do canal.

### 5. Assinatura (opcional)
Pergunte se ele quer que o formulário já saia assinado. Se sim, peça uma imagem da assinatura
(PNG com fundo claro) e guarde o caminho em `assinatura_png`. Se não, tudo bem — ele assina à
mão ou no celular depois.

### 6. Dependentes (se houver)
Pergunte se ele faz pedidos para dependentes (filhos, etc.). Para cada dependente, colete:
nome completo; CPF; e-mail; e, se for receber em conta própria, os dados bancários dele.
Se não houver dependentes, pule.

### 7. Cópia do e-mail (opcional)
Pergunte se ele quer receber uma cópia (CC) dos e-mails enviados — nele mesmo ou em um
familiar de confiança. Anote em `cc_padrao`. Deixe claro que advogado em cópia é caso a caso,
nunca automático.

### 8. Integrações (o que ele já usa)
Pergunte, uma de cada vez, e marque como ligada/desligada:
- **E-mail:** ele usa algum e-mail conectado ao Claude (Gmail, etc.) ou prefere copiar e
  enviar à mão? → `integracoes.email`
- **Repositório:** quer guardar o estado dos casos no Notion, numa planilha, ou só em
  arquivos locais (padrão)? → `integracoes.repositorio`
- **Lembretes:** quer lembretes de prazo num app de lembretes/calendário, ou só anotados em
  arquivo? → `integracoes.lembretes`

Explique que **nada disso é obrigatório** — só com arquivos locais já funciona.

### 9. Gravar
Monte o `config.local.yaml` na `pasta_base` com tudo que foi coletado (campos vazios para o
que ficou em branco). Mostre um resumo legível ao usuário e peça confirmação. Depois de
gravar, avise: "Pronto — agora é só pedir, por exemplo, 'preparar um reembolso de consulta'."

> Garanta que `config.local.yaml` está coberto pelo `.gitignore` (já está, por padrão) — ele
> nunca deve ser versionado nem compartilhado.
