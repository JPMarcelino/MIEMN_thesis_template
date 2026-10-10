#!/usr/bin/env bash
#
# Full thesis build: cover + thesis (pdflatex + makeglossaries + bibtex).
#
#   ./build.sh          build everything into thesis.pdf
#
# Requires a LaTeX distribution with pdflatex, bibtex and makeglossaries
# (xindy). See README.md for installation notes.
set -euo pipefail
cd "$(dirname "$0")"

LATEX="pdflatex -interaction=nonstopmode -file-line-error"

echo "==> Cover (cover.tex)"
$LATEX cover.tex >/dev/null

echo "==> Thesis, pass 1"
$LATEX thesis.tex >/dev/null

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

echo "==> Thesis, pass 2"
$LATEX thesis.tex >/dev/null
echo "==> Thesis, pass 3"
$LATEX thesis.tex >/dev/null

# Fail loudly if LaTeX logged an error, even though nonstopmode continued.
if grep -qE '^! ' thesis.log 2>/dev/null; then
  echo
  echo "Build finished with errors — see thesis.log:" >&2
  grep -nE '^! ' thesis.log >&2 || true
  exit 1
fi

echo
echo "Done. Output: thesis.pdf"
