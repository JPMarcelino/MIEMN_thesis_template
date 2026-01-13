# LaTeX Thesis Template

A clean, customizable LaTeX thesis template ready for academic writing. This template has been anonymized and is suitable for sharing on GitHub as a starting point for your own thesis.

## Features

- **Clean Structure**: Well-organized document with proper front matter and back matter
- **Automated Navigation**: Table of contents, list of figures, and list of tables
- **Glossary Support**: Automatic generation of acronyms and notation lists
- **Customizable Cover**: Professional cover page with university branding
- **Bibliography Management**: Integrated BibTeX support with IEEE style
- **Responsive Header/Footer**: Page numbers and section headers
- **GitHub-Ready**: Complete with `.gitignore` for LaTeX projects

## Directory Structure

```
.
├── thesis_jpm_22.5G_MPG_3nm.tex   # Main LaTeX file (RENAME to thesis_main.tex)
├── cover.tex                     # Cover page source
├── glossary.tex                  # Acronyms and notation definitions
├── bibliography.bib              # Bibliography database
├── .gitignore                   # Git ignore file for LaTeX
├── README.md                    # This file
├── figures/                      # Images and graphics
│   ├── university-logo.png      # UPDATE: Your university logo
│   ├── Python/                  # Python-generated figures
│   ├── Results/                 # Result figures
│   └── Schematics/              # Circuit/System schematics
├── sections/                     # Thesis chapters
│   ├── introduction.tex          # Introduction
│   ├── stateoftheart.tex        # State of the art / Literature review
│   ├── methods.tex              # Methodology / Materials and methods
│   ├── results.tex              # Results and discussion
│   ├── conclusions.tex          # Conclusions and future perspectives
│   ├── abstract.tex             # English abstract
│   ├── resumo.tex               # Portuguese abstract (if required)
│   ├── acknowledgements.tex     # Acknowledgments
│   ├── copyright.tex            # Copyright page
│   ├── appendix_a.tex           # Appendix A
│   ├── appendix_b.tex           # Appendix B
│   ├── appendix_c.tex           # Appendix C
│   ├── appendix_d.tex           # Appendix D
│   ├── appendix_e.tex           # Appendix E
│   ├── appendix_f.tex           # Appendix F
│   ├── appendix_g.tex           # Appendix G
│   └── appendix_h.tex           # Appendix H
├── cover-assets/                 # Cover page images
├── Python/                      # Python scripts if needed
└── cover.pdf                    # Generated cover (ignored in git)
```

## Getting Started

### Prerequisites

- **LaTeX Distribution**: TeX Live, MiKTeX, or MacTeX
- **LaTeX Editor**: Overleaf, TeXShop, VS Code with LaTeX Workshop, etc.

### 1. Fork or Clone This Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Customize Personal Information

#### a) Rename the Main File

Rename `thesis_jpm_22.5G_MPG_3nm.tex` to something appropriate for your thesis, e.g., `thesis_main.tex`:

```bash
mv thesis_jpm_22.5G_MPG_3nm.tex thesis_main.tex
```

#### b) Update `thesis_main.tex` (or your renamed file)

Find and replace all `[bracketed content]` with your information in the `\frontpage` command:

```latex
\newcommand{\frontpage}{
    \begin{titlepage}
        ...
        {\Huge\bfseries [Your Title Here]\par}
        ...
        {\Large\bfseries [Your Full Name]\par}
        ...
        for the degree of \emph{[Your Degree]}
        in [Your Program Name]
        ...
        {\bfseries Supervisors:}\\[0.5em]
        [Supervisor 1 Name], [Supervisor 2 Name]
        ...
        {\bfseries Examining Committee:}\\[0.5em]
        President: [President Name]\\
        Examiner: [Examiner Name]\\
        Member: [Member Name]
        ...
        [Your University Name]\\
        {\large [Month Year]\par}
    \end{titlepage}
}
```

Also update the header:

```latex
\fancyhead[L]{[Your Title Here]} % Header left - UPDATE THIS
```

#### c) Update `cover.tex`

Edit the metadata at the top of the file:

```latex
\newcommand*{\coverTitle}{[YOUR TITLE]}
\newcommand*{\coverAuthor}{[Your Name]}
\newcommand*{\coverAuthorDegree}{[Your Degree]}
\newcommand*{\coverProgram}{[Program Name]}
\newcommand*{\coverUniversity}{[University Name]}
\newcommand*{\coverDate}{[Month, Year]}
\newcommand*{\coverSupervisors}{[Supervisor 1]\\[Supervisor 2]}
\newcommand*{\coverCommittee}{President: Name\\Examiner: Name\\Member: Name}
\newcommand*{\coverSchool}{[School Name]}
\newcommand*{\coverDepartment}{[Department Name]}
```

Replace the university logo files in `cover-assets/` with your own.

#### d) Create Your Content

Edit the chapter files in the `sections/` directory with your actual content:

- `abstract.tex` - English abstract
- `resumo.tex` - Portuguese abstract (if required)
- `introduction.tex` - Introduction chapter
- `stateoftheart.tex` - Literature review
- `methods.tex` - Methodology
- `results.tex` - Results and discussion
- `conclusions.tex` - Conclusions and future work
- `acknowledgements.tex` - Acknowledgments
- `copyright.tex` - Copyright page (if required)
- `appendix_a.tex` through `appendix_h.tex` - Appendices

#### e) Update Glossary

Edit `glossary.tex` to add your specific acronyms and notation:

```latex
% Acronyms
\newacronym[type=acronym]{ai}{AI}{Artificial Intelligence}
\newacronym[type=acronym]{serdes}{SerDes}{Serializer/Deserializer}

% Notation
\newglossaryentry{tau}{
  name={\(\tau\)},
  description={Time constant},
  sort={tau},
  type=notation
}
```

#### f) Add References

Add your references to `bibliography.bib` in BibTeX format:

```bibtex
@article{smith2020example,
  title   = {Your Article Title},
  author  = {Smith, John and Doe, Jane},
  journal = {Journal Name},
  volume  = {15},
  number  = {3},
  pages   = {123--145},
  year    = {2020},
  doi     = {10.1000/example}
}
```

### 3. Building the Document

#### Using pdflatex (for simple documents):

```bash
pdflatex thesis_main
bibtex thesis_main
pdflatex thesis_main
pdflatex thesis_main
```

#### Using latexmk (recommended):

```bash
latexmk -pdf -interaction=nonstopmode thesis_main
```

#### To clean auxiliary files:

```bash
latexmk -c
```

#### To build the cover separately:

```bash
pdflatex cover
```

### 4. Including Figures

Place your images in the `figures/` directory and include them:

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/your-image.png}
    \caption{Your figure caption}
    \label{fig:your-label}
\end{figure}
```

### 5. Citing References

Cite references in your text using `\cite{key}`:

```latex
As shown by Smith and Doe \cite{smith2020example}...
```

## Customization

### Changing Document Class

The template uses `report` class with 11pt font and A4 paper:

```latex
\documentclass[11pt, a4paper]{report}
```

### Page Margins

Adjust margins in the geometry package:

```latex
\usepackage[a4paper, margin=2cm]{geometry}
```

### Line Spacing

Default is 1.25 spacing:

```latex
\setstretch{1.25}
```

### Fonts

Template uses Times New Roman font:

```latex
\usepackage{times}
```

## Common Issues

### Missing Image Files

- Replace the placeholder images in `figures/` and `cover-assets/` with your own
- Or comment out the image includes temporarily while setting up

### Glossary Not Generating

- Make sure `xindy` is installed with your LaTeX distribution
- Run `makeglossaries thesis_main` before `pdflatex`

### Bibliography Not Appearing

- Ensure your citations use keys that exist in `bibliography.bib`
- Run `bibtex thesis_main` between `pdflatex` runs

### Chapter Files Not Found

- The template expects chapter files in `sections/` directory
- Update the `\importsection` commands if using a different structure

## Tips

1. **Commit Often**: Use version control to track changes
2. **Compile Regularly**: Compile frequently to catch errors early
3. **Organize References**: Keep your bibliography well-organized
4. **Use Clear Descriptions**: Make figures and tables self-explanatory
5. **Check Requirements**: Verify your university's specific formatting requirements

## University-Specific Requirements

**Important**: This template is a general-purpose template. You may need to adjust it to meet your university's specific requirements for:
- Margins and page layout
- Header/footer format
- Text font and size
- Line spacing
- Cover page design
- Abstract formatting (bilingual vs English only)
- Copyright page requirements

Always check your university thesis guidelines before starting!

## License

This template is provided as-is for educational purposes. Feel free to modify and adapt it for your needs.

## Contributing

If you find bugs or have suggestions for improvements, please:
1. Fork the repository
2. Make your changes
3. Open a pull request

Or open an issue to report bugs or request features.

## Changelog

- **v1.0** (2025-01-13): Initial template release

---

**Note**: This template has been anonymized with placeholder text. Replace all `[bracketed content]` with your actual information before using for your thesis.
