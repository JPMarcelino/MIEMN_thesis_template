# Compliance with the DCM dissertation rules

This template implements the *Rules for Dissertation* of the Department
of Materials Science (DCM), approved 18 March 2014 and amended November
2020, for dissertations of the Integrated Master in Micro and
Nanotechnology Engineering. The rules PDF is in
[`Rules/`](Rules/RULES%20FOR%20DISSERTATION%20APPROVED%20NOV%202020.pdf).

## Formatting rules → where they live

| Rule | Requirement | Implemented in |
| --- | --- | --- |
| 1a | Written in English | whole template |
| 1a | Times New Roman, 11 pt | `\documentclass[11pt]` + `\usepackage{times}` in `thesis.tex` |
| 1a | 1.25 line spacing | `\setstretch{1.25}` in `thesis.tex` |
| 1a | Numbered, connected sections/sub-sections | `\setcounter{secnumdepth}{5}` |
| 1b | Properly numbered equations, tables, figures | standard LaTeX counters |
| 1c | Scientific notation for equations and plots | `siunitx` (`\SI`, `S` columns); `Python/miemn.mplstyle` |
| 1d | Plots: Arial 28 pt tick numbers, 30–32 pt axis labels, units on axes | `Python/miemn.mplstyle` (28 / 31 pt) |
| 1e | American or IOP reference style | `natbib` + `IEEEtran` |
| 1f | 2 cm margins on all sides | `\usepackage[a4paper, margin=2cm]{geometry}` |
| 1f | No empty space between sections | `\titlespacing*{\section}{0pt}{0pt}{0pt}` |
| 1f | ≤ 33 pages of content (excl. annexes/indexes/abbreviations) | `scripts/check_page_budget.py` |

## Required structure → where it lives

The thesis must contain, in order:

| Required part | Provided by |
| --- | --- |
| Title | cover (`cover.tex`) + title page (`\frontpage`) |
| General index (ToC) | `\tableofcontents` |
| Summary | `sections/abstract.tex` (and `sections/resumo.tex`) |
| Acknowledgements | `sections/acknowledgements.tex` |
| List of abbreviations and notation | `glossary.tex` |
| Index of figures | `\listoffigures` |
| Index of tables | `\listoftables` |
| Copyright page | `sections/copyright.tex` |
| Introduction | `sections/introduction.tex` |
| Materials and Methods | `sections/methods.tex` |
| Results and Discussion | `sections/results.tex` |
| Conclusions and Future Perspectives | `sections/conclusions.tex` |
| References | `bibliography.bib` |
| Annexes | `sections/appendix_a.tex` … `appendix_h.tex` |

The template also includes a **State of the Art** chapter, which is the
conventional place to satisfy the “Introduction must reflect the present
state of the art with correct, up-to-date references” criterion.

## Page budgets

| Section | Maximum |
| --- | --- |
| Motivation | 1 page |
| Summary (abstract) | 300 words (FCT-UNL) |
| Introduction | 5 pages |
| Materials and Methods | 2 pages (6 in industrial theses) |
| Results and Discussion | 20 pages |
| Conclusions and Future Perspectives | 2 pages |
| References | 2 pages |
| **Total written content** | **33 pages** |

Run `make check` to see current counts. The check is advisory; make it a
hard gate in CI by removing `continue-on-error` from the `page-budget`
job in `.github/workflows/build.yml`.

## Submission checklist

- [ ] `metadata.tex` filled in (title, name, degree, supervisors, committee).
- [ ] University logo replaced (`figures/university-logo.png`).
- [ ] Cover rebuilt: `make cover`.
- [ ] All `[bracketed placeholders]` removed from `sections/`.
- [ ] `\usepackage{lipsum}` and any placeholder text removed from `thesis.tex`.
- [ ] Acronyms and notation complete; each defined with `\gls{...}`.
- [ ] All figures generated with `Python/miemn.mplstyle` (Arial 28/31 pt, units on axes).
- [ ] All equations, tables and figures numbered and referenced with `\cref`.
- [ ] References up to date; IEEE style.
- [ ] `make` builds with no errors.
- [ ] `make check` within the page budgets.
