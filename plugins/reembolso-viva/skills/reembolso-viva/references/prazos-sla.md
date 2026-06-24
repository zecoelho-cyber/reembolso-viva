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
