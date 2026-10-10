# =====================================================================
# MIEMN thesis — common tasks
# =====================================================================
.PHONY: all pdf cover check clean distclean

# Default: build the whole document.
all: pdf

# Full build (cover + thesis + glossary + bibliography).
pdf:
	./build.sh

# Compile only the cover page into cover.pdf (two passes: TikZ current page).
cover:
	pdflatex -interaction=nonstopmode cover.tex
	pdflatex -interaction=nonstopmode cover.tex

# Build, then report per-chapter page counts against the DCM budgets.
check: pdf
	python3 scripts/check_page_budget.py thesis.pdf

# Remove LaTeX auxiliary files.
clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.idx *.ind \
	      *.ilg *.acn *.acr *.alg *.glg *.glo *.gls *.glsdefs *.ist \
	      *.nlg *.not *.ntn *.xdy *.run.xml *.bcf *.fdb_latexmk *.fls
	rm -rf build

# Also remove generated PDFs.
distclean: clean
	rm -f thesis.pdf cover.pdf
