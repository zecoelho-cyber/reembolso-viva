# Guia operacional — Reembolso Viva Mais Saúde

Base de conhecimento do assistente. Conteúdo derivado do Manual da operadora e do
Acordo Judicial TST de 2013. NÃO é ferramenta oficial; não substitui advogado nem médico.

---

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

---

# Prazos e SLAs — plano Viva Mais Saúde

Prazos conforme o Manual Saúde Viva Mais (oficial). **Não envie e-mail à operadora só
para perguntar prazo** — a resposta está aqui.

> ⚠️ Os prazos são em **dias úteis** (excluindo sábados, domingos e feriados nacionais e
> estaduais de SP), EXCETO a prestação de contas, que é em **dias corridos**.

## Cadência oficial

| Etapa | Gatilho | Prazo (manual) |
|---|---|---|
| 1. Aguardando protocolo | envio do e-mail | varia (resposta automática do sistema); usar **D+3 corridos** como referência de cobrança |
| 2. Aguardando pagamento | recebimento da solicitação | **5 dias úteis** a contar do dia útil seguinte ao recebimento |
| 2b. Pendência (operadora pede documento) | recebimento | a operadora contata em **até 72h úteis** se houver pendência |
| 3. Pendência aberta | operadora pediu documento | sem prazo formal, mas trava o andamento |
| 4. Pagamento aprovado | aprovação com data | data informada no e-mail de aprovação |
| 5. Prestação de contas | depósito confirmado | **60 dias corridos** a partir do depósito |

### Texto literal do manual sobre o pagamento

> "Após a aprovação do pedido (protocolo de pedido), o prazo estipulado para pagamento na
> conta bancária de titularidade do beneficiário requerente será de 5 (cinco) dias úteis a
> contar do dia útil posterior ao recebimento da solicitação."

### Em caso de pendência

> "Em até 72 horas úteis após o recebimento, a operadora contata via e-mail/telefone
> informando necessidade de complemento. O prazo de 5 dias úteis é INTERROMPIDO e fica
> pendente até o envio das informações. A partir do dia posterior à entrega das
> informações complementares, contam-se NOVAMENTE 5 dias úteis."

## Como os prazos transitam de uma etapa para a outra

- **Protocolo recebido (1 → 2):** começa a contar os 5 dias úteis a partir do dia útil
  seguinte.
- **Pendência aberta (2 → 3):** o prazo dos 5 dias úteis é pausado.
- **Pendência respondida (3 → 2):** recomeçam 5 dias úteis a partir da resposta.
- **Aprovação com data (2 → 4):** anote a data de depósito informada.
- **Depósito confirmado (4 → 5):** começam os **60 dias corridos** para prestar contas.
  É prudente criar um aviso antecipado por volta do 50º dia.

## ⚠️ Consequências de não prestar contas no prazo

| Atraso após o depósito | Consequência (manual) |
|---|---|
| **60 dias sem prestação** | bloqueio dos benefícios — não pode fazer novas solicitações nem usar a rede até apresentar a prestação |
| **90 dias sem prestação** | devolução do valor integral + **1% de juros ao mês + correção monetária + multa de 20%** sobre o valor liberado (parágrafo 6 do acordo coletivo que originou o plano) |

## Cálculo de dias úteis

Para calcular `D+N dias úteis` a partir de uma data, considerando feriados nacionais do
Brasil e estaduais de São Paulo:

```python
from datetime import date, timedelta
import holidays  # pip install holidays

br_holidays = holidays.country_holidays('BR', subdiv='SP')

def add_business_days(start: date, n: int) -> date:
    current = start
    added = 0
    while added < n:
        current += timedelta(days=1)
        if current.weekday() < 5 and current not in br_holidays:
            added += 1
    return current
```

> A prestação de contas (60 dias) é em dias **corridos** — para ela, basta somar 60 dias
> à data do depósito, sem pular fins de semana.

---

# Cobertura — o que o plano cobre e o que não cobre

> Há duas fontes que tratam de cobertura: o **Acordo Judicial de 2013** (instrumento de
> hierarquia superior, homologado pelo TST) e o **Manual da operadora** (regulamento
> administrativo). Quando os dois conflitam, o Acordo prevalece. Os pontos onde o Manual
> restringe além do Acordo estão detalhados em `base-legal.md`.

## A regra geral do Acordo: cobertura ampla

O Acordo estabelece o custeio **"prévio e integral da assistência ampla, plena e vitalícia
à saúde"**, prestada por entidades hospitalares, clínicas especializadas e consultórios
médicos, psicológicos, nutricionais, fisioterapêuticos, odontológicos e terapêuticos no
Estado de São Paulo, incluindo medicamentos de prescrição médica — **independentemente de
comprovação de nexo causal**.

A cobertura é a regra; as exclusões são uma **lista fechada (exaustiva)**. Ou seja: se o
procedimento não está na lista de exclusões abaixo, ele está coberto.

## Exclusões previstas no Acordo (lista exaustiva)

Estas são as únicas hipóteses de exclusão previstas na Cláusula Primeira do Acordo:

1. Tratamento clínico ou cirúrgico **experimental**.
2. Procedimentos clínicos ou cirúrgicos **estéticos não reparadores**.
3. **Inseminação artificial**.
4. Tratamento de **rejuvenescimento ou emagrecimento com finalidade estética**.
5. Medicamentos **não aprovados pela ANVISA**.
6. Tratamentos **ilícitos ou antiéticos**, ou não reconhecidos pelas autoridades
   competentes.
7. Casos de **cataclismos, guerras e comoções internas** declarados pela autoridade
   competente.
8. **Abuso quanto aos valores** referentes ao tratamento (avaliação caso a caso — não é um
   teto fixo).

> Importante: parto, gestação, obstetrícia e maternidade **não estão** na lista de
> exclusões — pela regra geral do Acordo, estão cobertos para a beneficiária habilitada.
> (Há nuances sobre o recém-nascido nos primeiros dias de vida — ver `base-legal.md`.)

## Restrições adicionais que o Manual da operadora aplica

O Manual cria algumas restrições e exigências que **não constam do Acordo**. As mais
comuns:

- **Medicamentos inibidores de apetite** (canetas emagrecedoras — semaglutida,
  liraglutida, tirzepatida): tratados como excluídos quando o uso é estético. Para uso
  **terapêutico** com prescrição médica (não estético), há base no Acordo para cobertura.
- **Reembolso de atendimentos médicos/odontológicos** "desde março de 2015, exceto
  urgência/emergência": esta é uma restrição **do Manual**, não do Acordo — ver conflito
  detalhado em `base-legal.md`.
- **Limites financeiros fixos** (ex.: teto para armação de óculos), **prazo de validade de
  receitas**, **exigência de 3 orçamentos**, **indução à rede credenciada**: também são
  regras administrativas do Manual, sem previsão no Acordo.

Sempre que um pedido for negado com base em uma dessas regras, vale conferir em
`base-legal.md` se a negativa tem fundamento no Acordo ou se é restrição criada pelo Manual.

## Tratamentos longos — regras do Manual

- **Terapias:** o Manual libera no máximo **1 mês por solicitação**; a renovação pede a
  prestação anterior + relatório com data/horário de cada sessão. (O Acordo não impõe esse
  ciclo mensal — ver `base-legal.md`.)
- **Internações:** no máximo **1 mês por solicitação** + relatório de evolução para renovar.
- **Tratamentos ortodônticos:** no máximo **2 meses por solicitação** + comprovação
  anterior.

---

# Checklist de documentos por tipo de pedido

Documentação que a operadora pede em cada tipo de adiantamento. O **formulário de
adiantamento preenchido e assinado** e o **RG** (ou documento de identidade) entram em
**todos** os casos.

| Tipo de pedido | Documentação |
|---|---|
| **Consulta médica** | Formulário + RG |
| **Consulta não-médica** (psicólogo, fonoaudiólogo, fisioterapeuta, nutricionista) | Formulário + RG + **encaminhamento médico** |
| **Exames laboratoriais e de imagem** | Formulário + RG + pedido médico (com CRM; CRO apenas para imagem odontológica) + orçamento detalhado do laboratório |
| **Cirurgia** | Formulário + RG + encaminhamento médico + orçamento do hospital + honorários (médico, auxiliar, anestesista, instrumentador) |
| **Materiais cirúrgicos** | Formulário + RG + relatório médico + orçamento do fabricante |
| **Terapias** (psicoterapia, psiquiatria, fono, fisio) | Formulário + RG + encaminhamento médico + orçamento do especialista (quantidade de sessões + valor unitário + período) |
| **Internações** | Formulário + RG + relatório médico + encaminhamento + orçamento da clínica/hospital |
| **Vacinas** | Formulário + RG + encaminhamento médico + orçamento da clínica |
| **Medicamentos** | Formulário + RG + receita médica (datada/assinada/carimbada) + orçamento |
| **Óculos de grau** | Formulário + RG + receita oftalmológica + orçamento da óptica |
| **Dental — consulta** | Formulário + RG + CPF/CNPJ do dentista |
| **Dental — tratamento** | Formulário + RG + orçamento detalhado por fase/dente |

## Exigências do Manual que podem ir além do Acordo

Algumas exigências do Manual são mais rígidas do que o que o Acordo pede (que é apenas:
identidade, formulário, requisição médica e custo estimado). Use `base-legal.md` para
saber quando contestar:

- **3 orçamentos/cotações** para materiais cirúrgicos, lentes ≥ R$ 4.000 e medicamentos
  acima de R$ 5.000. (O Acordo pede **um** orçamento estimado.)
- **Carimbo e papel timbrado** em documentos. (Há decisão judicial determinando que a
  operadora se abstenha dessa exigência — ver `base-legal.md`.)
- **Validade de 6 meses** para receitas de uso contínuo.
- **Limite financeiro fixo** para armação de óculos.

## Dicas práticas

- **Validade do orçamento:** confira a data. Orçamento vencido costuma ser motivo de
  pendência — peça um novo antes de enviar.
- **Vários pedidos/laboratórios no mesmo caso:** podem ser consolidados em um único
  formulário, com observação explicando.
- **CRM/CRO sem UF:** se faltar a UF do registro profissional, vale confirmar antes de
  enviar.
- **Pedido médico sem assinatura digital:** costuma ser aceito, mas é bom sinalizar.

---

# Prestação de contas

Depois que o procedimento/exame é realizado, você presta contas à operadora — envia as
notas fiscais e comprovantes do que foi efetivamente gasto. Prazo: **60 dias corridos a
partir do depósito** (ver `prazos-sla.md` para as consequências do atraso).

## Como enviar

- **E-mail NOVO** (nunca reply — ver `regras-canal.md`).
- **Assunto:** `Protocolo nº XXXXX — Prestação de contas` (o protocolo é obrigatório no
  assunto e no corpo).
- **Anexos:** nota(s) fiscal(is) + comprovante(s) de pagamento.

## Critérios de validação do recibo / nota fiscal (Manual)

O recibo ou nota deve conter:

- Nome completo do prestador
- CPF ou CNPJ do prestador
- Carimbo com registro profissional (CRM / CRO / CRP / CREFITO)
- Descrição detalhada do serviço prestado
- Data
- Nome completo do paciente
- CPF do paciente
- Valor numérico **igual** ao valor por extenso
- Documento **não rasurado**

> **Profissionais autônomos:** quando não houver nota fiscal, vale o recibo emitido pela
> plataforma da Receita Federal (Carnê-Leão / recibo eletrônico).

## Regra dos valores acima de R$ 500 (exigência do Manual)

> "Solicitações de adiantamento acima de R$ 500,00 deverão apresentar, além da nota
> fiscal, comprovante de pagamento (pix/transferência/boleto) **no mesmo CNPJ da requisição
> de adiantamento**."

Na prática: se o valor do caso for acima de R$ 500, anexe também o comprovante de pagamento
e confira se o **CNPJ do comprovante é o mesmo da nota fiscal**. Se não bater, vale resolver
ou explicar **antes** de enviar.

> Atenção a um caso comum: quando o pagamento é feito a um profissional autônomo que recebe
> via plataforma (CPF/chave Pix) mas a nota é emitida por uma pessoa jurídica (CNPJ
> diferente), essa exigência de "mesmo CNPJ" pode travar o pedido. Essa exigência é do
> Manual e **não consta do Acordo** — ver `base-legal.md` (conflito sobre comprovante com
> CNPJ idêntico).

## Guardar para o Imposto de Renda

- **O gatilho do arquivamento é a emissão da nota fiscal, não a aprovação da operadora.**
  Uma vez emitida, a NF será declarada no IRPF independentemente de a operadora aprovar ou
  rejeitar a prestação. Guarde a cópia assim que a NF existir.
- **Critério de ano fiscal = data da nota fiscal**, não a data do pagamento nem a do
  protocolo. Importante para notas do fim do ano cuja prestação só ocorre no ano seguinte.
- **O valor da NF pode ser diferente do valor reembolsado** — isso é normal. Para o IRPF
  declara-se o valor da NF (a despesa médica efetiva), não o que a operadora pagou.
- **Copie, não mova:** mantenha os originais na pasta do caso e guarde uma cópia
  consolidada por ano para entregar ao contador.
