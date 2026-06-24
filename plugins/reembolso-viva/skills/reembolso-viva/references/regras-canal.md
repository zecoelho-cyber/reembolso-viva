# Regras do canal de e-mail com a Viva Mais Saúde

Como a comunicação com a operadora funciona na prática. Seguir estas regras evita
que um pedido seja perdido, fechado por engano ou tratado como duplicado.

## Dados do canal

- **E-mail de destino:** `central@atendimentovivamais.com.br`
- **Telefone de orientação:** 0800-777-0154
- **Também aceita:** WhatsApp e atendimento presencial na unidade Viva Mais Saúde
- **Sistema da operadora:** healthbit (as respostas automáticas chegam com prefixo
  e código de chamado/ticket)

> Confirme estes canais no rodapé do formulário oficial de adiantamento — é a
> fonte mais atual. Se a operadora divulgar um canal novo, ele prevalece.

## Regra 1 — Todo e-mail para a Viva é um e-mail NOVO. Nunca responda (reply)

Cada comunicação deve ser enviada como mensagem nova, com assunto próprio. Vale para:
nova solicitação, resposta a pendência, esclarecimento, prestação de contas — qualquer
coisa. O sistema da operadora não trabalha bem com respostas encadeadas (reply): a
triagem pode não reconhecer a mensagem e o pedido se perde.

O próprio manual reforça isso para novas solicitações: *"Cada pedido exigirá o
preenchimento de um novo formulário de solicitação."*

## Regra 2 — Nunca use "Reenvio", "Re:", "Fwd:", "Resposta" no ASSUNTO

O assunto deve ser sempre **inédito, descritivo e autônomo**. Já houve caso real em que
um pedido foi **fechado pela operadora** porque o assunto do reenvio começava com
"Reenvio Solicitação…" — o sistema tratou como resposta a um chamado e perdeu o rastro.

Quando precisar reenviar ou complementar algo, **mude o assunto** em vez de prefixar com
"Reenvio". Exemplo: em vez de `Reenvio — Fisioterapia`, use
`Nova solicitação — Fisioterapia (substitui protocolo XXXXX)`.

## Regra 3 — Coloque o número do protocolo no assunto sempre que ele existir

- **Primeira solicitação (ainda sem protocolo):** assunto descritivo livre.
- **Qualquer e-mail posterior sobre um caso já protocolado** (pendência, esclarecimento,
  prestação de contas): o número do protocolo é **obrigatório no assunto E no corpo**.

Padrão recomendado: `Protocolo nº XXXXX — [assunto descritivo]`.

## Regra 4 — Responder-a-todos serve só para LER, não para enviar

A operadora costuma responder para todos os destinatários do e-mail original, então a
resposta dela chega normalmente na sua caixa. Mas isso vale apenas para **receber**.
Para **enviar** de volta, sempre um e-mail novo (Regra 1).

## Regra 5 — Conta bancária do próprio beneficiário

A conta indicada para receber o depósito deve ser de titularidade do beneficiário
(mesmo CPF) ou do representante legal. É a conta informada no formulário que recebe o
valor.

## Regra 6 — Documentação legível e assinada

Os documentos precisam estar legíveis e assinados pelo beneficiário maior de idade
(ou pelo representante legal, no caso de incapaz). **Procurações não são aceitas.**

## Regra 7 — Nomeie os anexos com nomes descritivos e DIFERENTES entre si

Nunca use prefixos sequenciais idênticos (`pedido_01`, `pedido_02`, `pedido_03`…). Já
houve caso real em que um pedido foi fechado porque os anexos tinham nomes quase iguais e
a triagem não os distinguiu sem abrir um por um.

Use prefixos diferentes e descritivos, por exemplo:

- `RG_Nome_Do_Beneficiario.pdf`
- `PEDIDO_Dr_Fulano_Especialidade_AAAA-MM-DD.pdf`
- `ENCAMINHAMENTO_Dr_Fulano_AAAA-MM-DD.pdf`
- `ORCAMENTO_Laboratorio_Cidade.pdf`
- `FORMULARIO_Solicitacao_Adiantamento.pdf`

Assim dá para selecionar tudo de uma vez e arrastar para o e-mail, e a operadora
distingue cada documento de imediato.

## Cópia (CC) do e-mail

- Por padrão, o e-mail vai apenas para `central@atendimentovivamais.com.br`.
- Se você quiser acompanhar, pode colocar **a si mesmo ou um familiar de confiança** em
  cópia — isso é configurável no seu `config.local.yaml`.
- Se você tiver acompanhamento jurídico, inclua um advogado em cópia **apenas quando
  fizer sentido para aquele caso específico** — nunca de forma automática.

## Quando o beneficiário é um DEPENDENTE (não o titular)

A operadora gerencia cada beneficiário individualmente. Quando o pedido é de um
dependente, o e-mail deve refletir os dados **do dependente**, não os do titular:

- **Assunto:** deve conter o **nome e o CPF do dependente**.
  - Padrão: `Solicitação de Adiantamento — [Especialidade] [Profissional] — [Nome do Dependente] - cpf [CPF do Dependente]`
  - O separador antes do CPF é ` - cpf ` (traço simples).
- **Corpo:** apresente diretamente os dados do beneficiário (o dependente). Não é preciso
  uma seção "titular do plano".
- **Assinatura do e-mail (sign-off):** o nome e o e-mail **do dependente**.
- **Campo "Para":** inclua `central@atendimentovivamais.com.br` e, se quiser, o e-mail do
  próprio dependente, para ele receber cópia e acompanhar.
