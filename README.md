# Reembolso Viva Mais Saúde

Um assistente que ajuda **beneficiários do plano Viva Mais Saúde** a cuidar dos
adiantamentos e reembolsos sem se perder na burocracia: ele prepara o formulário, monta o
e-mail no padrão que a operadora exige, controla os prazos, organiza a prestação de contas e
explica seus direitos com base no Acordo Judicial de 2013.

Funciona dentro do Claude (aplicativo de desktop). É um plugin: você instala uma vez,
configura com os seus dados e passa a pedir as coisas em linguagem natural — por exemplo,
*"prepara um reembolso de consulta com a cardiologista"*.

> ### ⚠️ Importante
> - **Não é uma ferramenta oficial** da Viva Mais Saúde, da operadora, da ATESQ nem das
>   empresas do Acordo. É um projeto comunitário, feito por um beneficiário para ajudar
>   outros.
> - **Não é aconselhamento jurídico nem médico.** As informações sobre o Acordo e sobre
>   direitos são leitura informativa. Para decisões com efeito legal, procure um advogado.
> - **Seus dados são seus.** Nenhum dado pessoal vem embutido aqui. Você informa os seus na
>   primeira vez, e eles ficam **só no seu computador**.

## Para quem é

Para qualquer Habilitado do plano Viva Mais Saúde que precise pedir adiantamento ou
reembolso de consultas, exames, terapias, medicamentos, internações ou materiais — para si
ou para um dependente.

## O que ele faz

- **Prepara o pedido:** preenche o formulário de adiantamento e monta o pacote de anexos com
  os nomes certos.
- **Escreve o e-mail certo:** no formato que a operadora aceita (assunto com protocolo, sem
  "responder", anexos bem nomeados) — evitando os erros que fazem um pedido ser fechado.
- **Controla prazos:** sabe os SLAs (5 dias úteis para pagamento, 60 dias para prestar
  contas) e te lembra.
- **Acompanha o caso:** do protocolo ao depósito, registrando cada etapa.
- **Organiza a prestação de contas e o IR:** guarda notas fiscais e comprovantes no lugar
  certo.
- **Explica seus direitos:** traz o Acordo de 2013 e os 12 pontos em que o Manual da
  operadora restringe além do que o Acordo garante.

## Como instalar

Há um manual passo a passo em linguagem simples em **[`docs/INSTALACAO.md`](docs/INSTALACAO.md)**
(e em PDF, `docs/INSTALACAO.pdf`). Em resumo:

1. Tenha o aplicativo do Claude no computador, com suporte a plugins.
2. Instale este plugin (pelo arquivo `reembolso-viva.plugin` ou adicionando este repositório
   como marketplace).
3. Na primeira vez, diga **"configurar reembolso"** e responda às perguntas — isso cria o seu
   `config.local.yaml`.
4. Pronto: peça **"preparar um reembolso de consulta"** e siga a conversa.

## Como usar (exemplos)

- `preparar um reembolso de consulta com a Dra Fulana`
- `tenho exames para pedir adiantamento`
- `o plano respondeu? checa pra mim`
- `recebi o protocolo 12345 do meu pedido`
- `depositou hoje` (ele cria o lembrete de prestar contas em 60 dias)
- `quais são meus direitos sobre internação?`

## Privacidade

- Os seus dados ficam em `config.local.yaml`, **no seu computador**. O `.gitignore` impede
  que ele seja versionado ou compartilhado.
- O repositório público **não contém nenhum dado pessoal de ninguém**. Há um verificador
  automático (`tools/verificar_privacidade.sh`) que confirma isso a cada mudança.

## O que tem dentro

```
reembolso-viva/                          (repositório = marketplace)
├── .claude-plugin/marketplace.json      catálogo do marketplace
├── plugins/
│   └── reembolso-viva/                  o plugin instalável
│       ├── .claude-plugin/plugin.json
│       ├── skills/
│       │   ├── reembolso-viva/          assistente operacional (+ conhecimento)
│       │   └── reembolso-viva-config/   configuração guiada (onboarding)
│       ├── scripts/preencher_formulario.py
│       ├── templates/                   formulário de adiantamento em branco
│       ├── referencias/                 Acordo Judicial TST 2013 (fonte pública)
│       ├── examples/                    exemplo de caso
│       ├── config.example.yaml          modelo do arquivo de configuração
│       └── CONNECTORS.md                como ligar e-mail / repositório / lembretes
├── tools/verificar_privacidade.sh       verificador de privacidade (manutenção)
├── docs/INSTALACAO.md                   manual de instalação para leigos
└── README.md · LICENSE · CHANGELOG.md
```

## Base legal

A pasta `plugins/reembolso-viva/referencias/` traz o texto integral do Acordo Judicial
homologado pelo TST em 2013 (processo TST-ARR-22200-28.2007.5.15.0126), e o módulo
`plugins/reembolso-viva/skills/reembolso-viva/references/base-legal.md` resume os direitos e
os 12 conflitos entre o Manual da operadora e o Acordo.

## Também no ChatGPT (Fase 2)

Além do plugin do Claude, há uma versão em **ChatGPT (Custom GPT)** na pasta
[`chatgpt/`](chatgpt/) — um assistente que qualquer pessoa usa **de graça pelo link, sem
instalar**. É um consultor: tira dúvidas, redige o e-mail no padrão, ajuda no formulário e
explica direitos. Não guarda dados entre conversas nem acompanha casos sozinho — isso é só na
versão do Claude. Para montar, veja
[`chatgpt/COMO-MONTAR-NO-CHATGPT.md`](chatgpt/COMO-MONTAR-NO-CHATGPT.md).

## Contribuindo

Sugestões e correções são bem-vindas (issues / pull requests). Ao contribuir, **nunca inclua
dados pessoais** — rode `tools/verificar_privacidade.sh` antes de enviar.

## Licença

MIT — ver [`LICENSE`](LICENSE) (com o aviso de "não oficial / não é aconselhamento jurídico").
