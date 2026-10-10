#!/usr/bin/env bash
#
# Full thesis build: cover + thesis (pdflatex + makeglossaries + bibtex).
#
#   ./build.sh          build everything into thesis.pdf
#
# Requires a LaTeX distribution with pdflatex, bibtex and makeglossaries
# (xindy). See README.md for installation notes.
set -uo pipefail
cd "$(dirname "$0")"

LATEX="pdflatex -interaction=nonstopmode -file-line-error"
status=0

run() {
  local label="$1"; shift
  echo "==> ${label}"
  if ! "$@"; then
    echo "    (pdflatex returned a non-zero status)"
    status=1
  fi
}

# cover.tex uses TikZ "current page", so it needs two passes to settle.
run "Cover (cover.tex), pass 1" $LATEX cover.tex
run "Cover (cover.tex), pass 2" $LATEX cover.tex
run "Thesis, pass 1" $LATEX thesis.tex

echo "==> Glossary (makeglossaries)"
if command -v makeglossaries >/dev/null 2>&1; then
  makeglossaries thesis >/dev/null || echo "    makeglossaries reported problems"
else
  echo "    makeglossaries not found — glossaries will be empty"
fi

echo "==> Bibliography (bibtex)"
if command -v bibtex >/dev/null 2>&1; then
  bibtex thesis >/dev/null || echo "    bibtex reported problems"
else
  echo "    bibtex not found — bibliography will be empty"
fi

run "Thesis, pass 2" $LATEX thesis.tex
run "Thesis, pass 3" $LATEX thesis.tex

echo
if grep -nE '^! |LaTeX Error:|^Error:' thesis.log >/dev/null 2>&1; then
  echo "Build finished with errors — see thesis.log:" >&2
  grep -nE '^! |LaTeX Error:|^Error:' thesis.log >&2 || true
  status=1
fi

if [ "$status" -ne 0 ]; then
  echo "Build FAILED." >&2
  exit 1
fi

echo "Done. Output: thesis.pdf"
