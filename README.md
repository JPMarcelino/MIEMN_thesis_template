# MIEMN Master's Thesis Template

[![Build thesis](https://github.com/JPMarcelino/MIEMN_thesis_template/actions/workflows/build.yml/badge.svg)](https://github.com/JPMarcelino/MIEMN_thesis_template/actions/workflows/build.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A ready-to-write, rules-compliant LaTeX template for the Master's
dissertation of the **Integrated Master in Micro and Nanotechnology
Engineering (MIEMN)** at NOVA FCT.

Fill in one file (`metadata.tex`), write your chapters in `sections/`,
and you get a properly formatted PDF — title page, bilingual abstract,
copyright page, lists of abbreviations/notation/figures/tables, IEEE
bibliography and lettered annexes — plus a live build on GitHub Actions.

## Why this template

- **One place for your details.** Title, name, degree and supervisors are
  defined once in `metadata.tex` and reused by the title page, the cover
  and the PDF metadata.
- **Rules built in.** 2 cm margins, Times New Roman 11 pt, 1.25 line
  spacing, numbered floats, IEC/ISO units via `siunitx`, IEEE references —
  all matching the DCM dissertation rules. See [`COMPLIANCE.md`](COMPLIANCE.md).
- **Compliant figures by default.** A matplotlib style
  (`Python/miemn.mplstyle`) produces plots with Arial 28 pt ticks and
  31 pt axis labels, exactly as the rules require.
- **Beautiful typography.** Times, hyperlinked cross-references
  (`\cref`), `booktabs` tables, clickable bookmarks and a clean cover.
- **One-command build.** `make` runs the full pdflatex → makeglossaries →
  bibtex → pdflatex ×2 cycle and fails loudly on errors.
- **Continuous integration.** Every push and pull request builds the PDF
  and uploads it as an artifact; tags publish a release.

## Quick start

### Overleaf

1. Upload this repository (or use *New Project → Import from GitHub*).
2. Set the main document to `thesis.tex`.
3. Edit `metadata.tex` and the files in `sections/`.

> Overleaf has xindy and `makeglossaries`, so the abbreviation and
> notation lists build automatically once you enable the glossary step.

### Local build

Install a full TeX Live distribution (or MiKTeX/MacTeX) — xindy and
`makeglossaries` are required for the glossary.

```bash
git clone https://github.com/JPMarcelino/MIEMN_thesis_template.git
cd MIEMN_thesis_template

make            # full build -> thesis.pdf
make cover      # rebuild just the cover
make check      # build + page-budget report
make clean      # remove auxiliary files
```

`make` calls [`build.sh`](build.sh), which is the canonical recipe. Plain
`latexmk -pdf thesis` also works via the bundled [`.latexmkrc`](.latexmkrc).

### GitHub Actions

No setup needed: pushing to `main` builds `thesis.pdf` and attaches it to
the workflow run. Push a tag like `v1.0` to publish a release with the PDF.

## What to edit

| File | What it is for |
| --- | --- |
| `metadata.tex` | **Start here.** Title, author, degree, supervisors, committee, university, date, keywords. |
| `sections/abstract.tex` | English abstract (Summary, ~300 words). |
| `sections/resumo.tex` | Portuguese abstract. |
| `sections/acknowledgements.tex` | Acknowledgements. |
| `sections/introduction.tex` | Chapter 1 — Introduction. |
| `sections/stateoftheart.tex` | Chapter 2 — State of the Art. |
| `sections/methods.tex` | Chapter 3 — Materials and Methods. |
| `sections/results.tex` | Chapter 4 — Results and Discussion. |
| `sections/conclusions.tex` | Chapter 5 — Conclusions and Future Perspectives. |
| `glossary.tex` | Acronyms and notation. |
| `bibliography.bib` | Your references (BibTeX). |
| `sections/appendix_*.tex` | Annexes A–H. Delete the ones you do not use. |
| `figures/`, `cover-assets/` | Images and cover artwork. |

You should never need to edit `thesis.tex` except to add, remove or
reorder chapters.

### Wiring your data in

`metadata.tex` defines simple commands that the rest of the document
consumes:

```latex
\newcommand*{\thesistitle}{Full Title of Your Thesis}
\newcommand*{\thesisauthor}{Your Full Name}
\newcommand*{\thesisdegree}{Master of Science}
\newcommand*{\thesisprogram}{Micro and Nanotechnology Engineering}
\newcommand*{\thesisuniversity}{NOVA University Lisbon}
\newcommand*{\thesissupervisors}{Supervisor One, Supervisor Two}
```

## Project structure

```text
.
├── thesis.tex            # main document (preamble + chapter order)
├── metadata.tex          # your personal data — edit this
├── cover.tex             # cover page, compiled to cover.pdf
├── glossary.tex          # acronym + notation definitions
├── bibliography.bib      # references
├── build.sh / Makefile   # one-command builds
├── .latexmkrc            # latexmk configuration
├── COMPLIANCE.md         # DCM rules → how this template satisfies them
├── sections/             # all chapters and front/back matter
├── figures/              # images used in the thesis
├── cover-assets/         # logos and cover artwork
├── Python/               # scripts + compliant matplotlib style
└── scripts/              # build helpers (page-budget report)
```

## Writing

### Figures

Put images in `figures/` (subfolders are fine) and include them with a
path relative to that folder — `\graphicspath` is already set:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{my-plot.pdf}
  \caption{Device response as a function of bias.}
  \label{fig:response}
\end{figure}
```

Reference it with `\cref{fig:response}` (self-updating “Figure 4.2”, with
a hyperlink).

Generate compliant plots with the bundled style:

```python
import sys; sys.path.insert(0, "Python")
import matplotlib.pyplot as plt, figure_style
figure_style.use_thesis_style()
# ... draw ...
figure_style.save_figure(fig, "figures/Python/my-plot")
```

### Tables

Use `booktabs` and `siunitx` for publication-quality tables:

```latex
\begin{table}[htbp]
  \centering
  \caption{Measured performance.}
  \label{tab:performance}
  \begin{tabular}{l S[table-format=2.1]}
    \toprule
    Parameter & {Value (\si{\micro\second})} \\
    \midrule
    Rise time & 3.4 \\
    Fall time & 2.1 \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Equations, references and acronyms

```latex
\begin{equation}
  \label{eq:rc}
  \tau = R\,C
\end{equation}

As shown in \cref{eq:rc} \cite{smith2020example}, ...
The \gls{serdes} block ...
```

## Page budgets

The rules cap the written content at 33 pages. `make check` prints how
many pages each chapter currently takes and flags anything over budget.
The full breakdown is in [`COMPLIANCE.md`](COMPLIANCE.md).

## Requirements

- A full TeX Live 2023+ (or MiKTeX/MacTeX) with `pdflatex`, `bibtex`,
  `makeglossaries` and **xindy** (for the glossary).
- Python 3 only if you use the figure helpers or the page-budget report.

## Troubleshooting

- **Glossary lists are empty.** Run `makeglossaries thesis` (or just run
  `make`, which does it for you). xindy must be installed.
- **Bibliography is empty.** Run `bibtex thesis` between pdflatex passes,
  or use `make`. Check that your `\cite` keys exist in `bibliography.bib`.
- **“File `cover.pdf` not found”.** Run `make cover` first; the main
  document warns but still builds without it.
- **Overfull boxes.** Usually harmless; enable `\usepackage{showframe}` in
  `thesis.tex` temporarily to see the text block.

## Contributing

Issues and pull requests are welcome. Please keep the template compiling
cleanly (`make`) and keep personal data out of the committed files.

## License

[MIT](LICENSE).
