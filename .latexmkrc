# latexmk configuration for the MIEMN thesis template.
#
#   latexmk -pdf thesis     # build thesis.pdf (runs makeglossaries too)
#   latexmk -c              # clean auxiliary files
#
# ./build.sh and `make` are the canonical builds; this file just makes
# plain latexmk do the right thing as well.

$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error %O %S';
$bibtex_use = 2;      # always run bibtex when the .bib changes
$clean_ext = 'bbl run.xml xdy acn acr alg glg glo gls glsdefs ist nlg not ntn';

# Run makeglossaries whenever a glossary source file changes.
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
add_cus_dep('acr', 'acn', 0, 'makeglossaries');
add_cus_dep('not', 'ntn', 0, 'makeglossaries');
sub makeglossaries {
    system("makeglossaries \"$_[0]\"");
}
