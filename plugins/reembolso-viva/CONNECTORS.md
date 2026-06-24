# Conectores

## Como as referências de ferramenta funcionam

Os arquivos deste plugin usam `~~categoria` como espaço reservado para a ferramenta que
**você** conectar naquela categoria. O plugin é agnóstico de ferramenta — ele descreve o
fluxo em termos de categorias, não de produtos específicos. Assim cada pessoa usa o que já
tem, e nada é obrigatório.

## Conectores deste plugin

| Categoria | Espaço reservado | Opções comuns | Padrão (sem configurar nada) |
|---|---|---|---|
| E-mail | `~~email` | Gmail, Outlook/Microsoft, outro e-mail conectado ao Claude | **Manual** — o assistente escreve o texto e você copia, anexa e envia |
| Repositório (estado dos casos) | `~~repositório` | Notion, Google Sheets/Excel | **Arquivos locais** — `status.yaml` em cada pasta de caso |
| Lembretes (prazos) | `~~lembretes` | App de lembretes, Google/Apple Calendar | **Arquivo** — uma lista local de prazos |

## O que significa "degradar com elegância"

Se você não tiver uma integração de uma categoria, o assistente faz a parte que dá para
fazer localmente e te diz o que fazer à mão. Exemplos:

- **Sem e-mail conectado:** ele monta o texto do e-mail e a lista de anexos; você cola no seu
  e-mail, anexa os PDFs e envia.
- **Sem Notion/planilha:** ele guarda o estado de cada caso em arquivos `status.yaml` na sua
  pasta de trabalho.
- **Sem app de lembretes:** ele anota os prazos em uma lista local e te avisa quando você
  abrir o assistente.

## Como ligar uma integração

Você escolhe isso na configuração inicial (diga "configurar reembolso"), e fica gravado no
seu `config.local.yaml`, no bloco `integracoes`. Dá para mudar quando quiser.

> Importante: conectar um e-mail (por exemplo) é algo que você faz **no aplicativo do
> Claude**, nas configurações de conectores — não dentro deste plugin. O plugin apenas usa o
> que estiver conectado.
