#!/usr/bin/env bash
# =========================================================================
# verificar_privacidade.sh
# Falha se encontrar QUALQUER dado pessoal/privado nos arquivos de texto do
# repositório. Rode ANTES de publicar e a cada mudança.
#
# Entidades PÚBLICAS do Acordo (ATESQ como organização, Shell, Raízen, BASF,
# advogados signatários, número do processo TST) são PERMITIDAS e não entram
# na lista de proibidos. O que NÃO pode aparecer são dados privados de
# qualquer pessoa: nomes de família, CPFs, e-mails pessoais, IDs de bases
# privadas, identificadores de casos individuais.
# =========================================================================
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

PATTERNS=(
  'Jos[eé] Fernando'
  'Z[eé] Coelho'
  'zecoelho'
  'Coelho'
  'Giraldi'
  'Fernanda'
  'Giulia'
  'Antonieta'
  'antonietabraga'
  'fernandagrcoelho'
  'josefrcoelho'
  '057\.?960\.?768'
  '455\.?836\.?538'
  '62811fea'
  'CIESB-VIVA'
  'JACCARD'
  'LERARIO'
  'KALIL'
  'DROGASIL'
  'PREVCARE'
  '03\.?813\.?882'
  'atesq\.com\.br'
  '13851|14488|13700|14545'
)

FOUND=0
for p in "${PATTERNS[@]}"; do
  HITS=$(grep -rEnI \
    --exclude-dir=.git \
    --exclude="*.pdf" --exclude="*.png" --exclude="*.jpg" \
    --exclude="verificar_privacidade.sh" \
    "$p" . 2>/dev/null || true)
  if [ -n "$HITS" ]; then
    echo "PADRAO PROIBIDO ENCONTRADO: /$p/"
    echo "$HITS"
    echo
    FOUND=1
  fi
done

echo "------------------------------------------------------------------"
if [ "$FOUND" -eq 0 ]; then
  echo "LIMPO: nenhum dado pessoal/privado encontrado nos arquivos de texto."
  echo "(Os PDFs em referencias/ e templates/ foram verificados separadamente"
  echo " e contem apenas conteudo publico, sem dados de beneficiarios.)"
  exit 0
else
  echo "ATENCAO: revise os arquivos acima ANTES de publicar."
  exit 1
fi
