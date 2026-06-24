#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preenche o formulario de adiantamento da Viva Mais por sobreposicao de texto.

O formulario oficial e um PDF "chapado" (sem campos de formulario), entao os
dados sao desenhados por cima, em coordenadas calibradas para o template que
acompanha este plugin (templates/formulario-adiantamento-viva.pdf).

Uso:
  python3 preencher_formulario.py \
      --config /caminho/config.local.yaml \
      --caso   /caminho/caso.yaml \
      --beneficiario titular \
      --out    /caminho/form-preenchido.pdf

caso.yaml (exemplo em examples/caso-exemplo.yaml):
  data: "24/06/2026"
  tipo: consultas        # consultas | terapias | medicamento | internacao | exames | materiais
  itens:
    - procedimento: "Consulta cardiologia"
      profissional: "Dr Fulano de Tal"
      crm: "SP-123456"
      qtd: 1
      valor: 450.00
  total: 450.00

Dependentes: passe --beneficiario "Nome Completo do Dependente" (precisa existir
no bloco 'dependentes' do config).
"""
import argparse
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("Falta o pacote pyyaml: pip install pyyaml")
try:
    import fitz  # PyMuPDF
except ImportError:
    try:
        import pymupdf as fitz
    except ImportError:
        sys.exit("Falta o PyMuPDF: pip install pymupdf")

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "templates", "formulario-adiantamento-viva.pdf")

# Coordenadas (x, y do baseline) calibradas para o template oficial.
F = {
    "data": (458, 47),
    "nome": (84, 151),
    "cpf": (456, 151),
    "endereco": (100, 166),
    "bairro": (286, 166),
    "cidade": (417, 166),
    "uf": (524, 166),
    "cep": (78, 181),
    "email": (187, 181),
    "telefone": (399, 181),
    "banco_titular_nome": (173, 196),
    "banco_titular_cpf": (419, 196),
    "banco": (86, 211),
    "agencia": (245, 211),
    "conta": (387, 211),
    "pix": (103, 226),
    "eu_nome": (68, 621),
    "data_rodape": (266, 651),
}
CHECK = {
    "consultas": (55, 91),
    "terapias": (171, 91),
    "medicamento": (55, 106),
    "internacao": (171, 106),
    "exames": (55, 121),
    "materiais": (171, 121),
}
DECLARO = (54, 255)
COLS = {"proc": 52, "prof": 284, "crm": 406, "qtd": 482, "valor": 503}
ROW_Y0 = 324
ROW_DY = 16
TOTAL_XY = (503, 501)
SIG_RECT = (358, 636, 455, 655)


def fmt_brl(v):
    try:
        return ("%0.2f" % float(v)).replace(".", ",")
    except (TypeError, ValueError):
        return str(v)


def put(page, xy, text, size=9):
    if text is None or str(text).strip() == "":
        return
    page.insert_text((xy[0], xy[1]), str(text), fontsize=size,
                     fontname="helv", color=(0, 0, 0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--caso", required=True)
    ap.add_argument("--beneficiario", default="titular")
    ap.add_argument("--out", required=True)
    ap.add_argument("--template", default=TEMPLATE)
    a = ap.parse_args()

    cfg = yaml.safe_load(open(a.config, encoding="utf-8")) or {}
    caso = yaml.safe_load(open(a.caso, encoding="utf-8")) or {}

    if a.beneficiario == "titular":
        ben = cfg.get("titular", {}) or {}
        banco = cfg.get("banco", {}) or {}
    else:
        ben = None
        for d in (cfg.get("dependentes") or []):
            if d.get("nome", "").strip().lower() == a.beneficiario.strip().lower():
                ben = d
                break
        if ben is None:
            sys.exit("Beneficiario nao encontrado no config: %s" % a.beneficiario)
        banco = ben.get("banco", {}) or {}

    doc = fitz.open(a.template)
    page = doc[0]

    put(page, F["data"], caso.get("data", ""))
    tipo = (caso.get("tipo", "") or "").strip().lower()
    if tipo in CHECK:
        put(page, CHECK[tipo], "X", 11)

    put(page, F["nome"], ben.get("nome", ""))
    put(page, F["cpf"], ben.get("cpf", ""))
    put(page, F["endereco"], ben.get("endereco", ""))
    put(page, F["bairro"], ben.get("bairro", ""))
    put(page, F["cidade"], ben.get("cidade", ""))
    put(page, F["uf"], ben.get("uf", ""))
    put(page, F["cep"], ben.get("cep", ""))
    put(page, F["email"], ben.get("email", ""))
    put(page, F["telefone"], ben.get("telefone", ""))

    put(page, F["banco_titular_nome"], banco.get("titular_conta", ""))
    put(page, F["banco_titular_cpf"], banco.get("cpf_titular_conta", ""))
    put(page, F["banco"], banco.get("banco", ""))
    put(page, F["agencia"], banco.get("agencia", ""))
    put(page, F["conta"], banco.get("conta", ""))
    put(page, F["pix"], banco.get("chave_pix", ""))

    put(page, DECLARO, "X", 11)
    put(page, F["eu_nome"], ben.get("nome", ""))
    put(page, F["data_rodape"], caso.get("data", ""))

    y = ROW_Y0
    soma = 0.0
    for it in (caso.get("itens") or []):
        put(page, (COLS["proc"], y), it.get("procedimento", ""), 8)
        put(page, (COLS["prof"], y), it.get("profissional", ""), 8)
        put(page, (COLS["crm"], y), it.get("crm", ""), 8)
        put(page, (COLS["qtd"], y), it.get("qtd", ""), 8)
        v = it.get("valor")
        if v is not None:
            put(page, (COLS["valor"], y), fmt_brl(v), 8)
            try:
                soma += float(v)
            except (TypeError, ValueError):
                pass
        y += ROW_DY

    total = caso.get("total")
    if total is None and soma > 0:
        total = soma
    if total is not None:
        put(page, TOTAL_XY, fmt_brl(total), 9)

    sig = ben.get("assinatura_png", "")
    if sig:
        sig = os.path.expanduser(sig)
        if os.path.exists(sig):
            page.insert_image(fitz.Rect(*SIG_RECT), filename=sig, keep_proportion=True)

    doc.save(a.out)
    print("OK ->", a.out)


if __name__ == "__main__":
    main()
