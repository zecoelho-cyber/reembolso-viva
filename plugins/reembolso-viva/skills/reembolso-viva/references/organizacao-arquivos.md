# Organização de arquivos

Uma estrutura simples de pastas para manter cada caso organizado, do pedido até a
prestação de contas e o IR. A **pasta-base** é escolhida por você no onboarding e fica
gravada no `config.local.yaml` (ex.: `~/Documentos/Reembolsos-Viva/`). Tudo abaixo é
relativo a ela.

## Estrutura por caso

```
[pasta-base]/
├── [ANO]/                                   ex.: 2026/  — casos do titular
│   └── [AAAAMMDD]_[CASO]/                   ex.: 20260624_CONSULTA_CARDIO/
│       ├── 00_pedidos/                       pedidos/encaminhamentos médicos (PDF)
│       ├── 01_orcamentos/                    orçamentos de laboratório/clínica (PDF)
│       ├── 02_solicitacao/                   formulário preenchido + RG + corpo do e-mail
│       ├── 03_confirmacoes/                  protocolo + respostas + comprovante de depósito
│       ├── 04_realizado/                     notas fiscais + comprovantes de pagamento
│       ├── 05_prestacao_contas/              e-mail de prestação + protocolo final
│       └── status.yaml                        estado do caso (espelho local)
│
├── DEPENDENTES/                              apenas se você tiver dependentes
│   └── [NOME_DEPENDENTE]/
│       ├── perfil.yaml                        dados fixos do dependente (CPF, e-mail, conta)
│       └── [ANO]/[AAAAMMDD]_[CASO]/          mesma estrutura interna acima
│
└── ARQUIVOS_IR-[ANO]/                        cópia consolidada para o Imposto de Renda
    └── [PROTOCOLO]_[DESCRICAO]/              ex.: 4981_FISIOTERAPIA/
```

## Convenções

- **Nome do caso:** `AAAAMMDD_DESCRICAO_CURTA` em maiúsculas, separador `_`.
  Ex.: `20260624_CONSULTA_CARDIO`, `20260515_EXAMES_LABORATORIO`.
- **Datas:** ISO (`2026-06-24`) nos arquivos de controle; formato BR (`24/06/2026`) só no
  formulário impresso.
- **Valores:** em reais, formato `1.060,00`.

## Pacote de envio (DOCS-TMP)

Na hora de montar o e-mail, é útil reunir **todos** os anexos em uma pasta temporária, já
renomeados com nomes descritivos e diferentes entre si (ver `regras-canal.md`, Regra 7):

```
[ANO]/DOCS-TMP/envio_[CASO]/
├── RG_Nome_Do_Beneficiario.pdf
├── PEDIDO_Dr_Fulano_AAAA-MM-DD.pdf
├── ORCAMENTO_Laboratorio.pdf
├── FORMULARIO_Solicitacao_Adiantamento.pdf
└── LEIA-ME.txt                               lista os anexos na ordem
```

Assim dá para selecionar tudo de uma vez e arrastar para o e-mail. Depois de enviar, essa
pasta pode ser apagada — os originais continuam nas subpastas `00_` a `02_` do caso.

## status.yaml — o estado de cada caso

Um arquivo pequeno que registra em que pé está o caso (status atual, protocolo, datas,
valores, interações). Serve para você (ou o assistente) saber rapidamente o que falta sem
abrir o e-mail. Quando você usa um repositório externo (Notion, planilha), ele é o espelho
local desse repositório.
