# Como montar o assistente no ChatGPT (Custom GPT)

Guia passo a passo. Você precisa de **ChatGPT Plus** (ou superior) para *criar*. Depois de
pronto e publicado, **qualquer pessoa usa de graça** pelo link, só precisa estar logada no
ChatGPT.

Tempo: ~15 minutos. Faça no **computador**, pelo navegador.

---

## Passo 1 — Abrir o criador de GPT

1. Entre em **chatgpt.com** e faça login.
2. Na barra da esquerda, clique em **GPTs** (ou "Explorar GPTs") → botão **+ Criar**
   (em inglês, "Create"). Atalho direto: **chatgpt.com/gpts/editor**.
3. No alto, escolha a aba **Configurar** (em inglês, "Configure") — é onde você tem controle
   de tudo. Ignore a aba "Criar"/"Create" (que monta por conversa).

## Passo 2 — Nome e descrição

- **Nome:** `Reembolso Viva Mais (não oficial)`
- **Descrição:** `Ajuda beneficiários do plano Viva Mais Saúde com adiantamentos e reembolsos: documentos, prazos, e-mail no padrão certo, formulário e direitos (Acordo TST 2013). Não oficial.`

## Passo 3 — Instruções

No campo **Instruções** ("Instructions"), cole **todo** o conteúdo do arquivo
`INSTRUCOES-DO-GPT.md` (da linha "Quem você é" até o fim). É o "cérebro" do assistente.

## Passo 4 — Sugestões de conversa (conversation starters)

Adicione estas quatro (ajude o usuário a começar):

- `Que documentos preciso para pedir adiantamento de um exame?`
- `Me ajuda a montar o e-mail de uma consulta?`
- `Quais são meus direitos numa internação?`
- `Como faço a prestação de contas?`

## Passo 5 — Conhecimento (Knowledge)

Em **Conhecimento** ("Knowledge"), clique em **Carregar arquivos** e suba os **4 arquivos**
da pasta `chatgpt/conhecimento/` deste projeto:

1. `guia-operacional-reembolso-viva.md`
2. `base-legal-acordo-2013.md`
3. `Acordo-2013-TST-Shell-Raizen-BASF.pdf`
4. `formulario-adiantamento-viva.pdf`

## Passo 6 — Capacidades (Capabilities)

- **Ligue** "Interpretador de Código e Análise de Dados" ("Code Interpreter & Data
  Analysis") — é o que permite preencher o formulário PDF no chat.
- Navegação na web: opcional (pode deixar ligada).
- Geração de imagem: pode deixar desligada.

## Passo 7 — Salvar e publicar

1. Clique em **Criar** / **Salvar** (canto superior direito).
2. Em compartilhamento, escolha **"Qualquer pessoa com o link"** ("Anyone with a link").
   Assim o pessoal do grupo usa sem você adicionar um por um.
3. Copie o link gerado.

## Passo 8 — Testar antes de divulgar

Abra o link numa conversa nova e teste:
- "Que documentos preciso para um exame?" → deve responder pelo guia.
- "Me ajuda a montar o e-mail de uma consulta com a Dra Fulana, R$ 300" → deve perguntar o que
  falta e montar o e-mail no padrão.
- "Quais meus direitos sobre acomodação em internação?" → deve usar a base legal (conflito #2).

Se ele inventar algo ou fugir do padrão, me avise que a gente ajusta as instruções.

## Passo 9 — Divulgar

Mande o link no grupo com um aviso curto (igual ao da Fase 1): não é oficial, não substitui
advogado, e o que a pessoa digitar passa pelos servidores da OpenAI — então compartilhar só o
necessário.

---

## Atualizar depois

Para mudar algo: abra o GPT → **Editar** → ajuste instruções ou arquivos → **Atualizar**. O
link continua o mesmo.

## Diferença para a versão do Claude

Este assistente é um **consultor**: tira dúvidas, redige o e-mail e ajuda no formulário. Ele
**não** guarda os dados da pessoa entre conversas, não cria lembretes e não acompanha os casos
sozinho — isso é só na versão do Claude (Fase 1). Em compensação, qualquer um usa de graça,
sem instalar nada.
