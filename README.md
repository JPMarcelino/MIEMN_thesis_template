# Nova FCT Thesis Template

This is a LaTeX template for writing a thesis at the NOVA School of Science and Technology (FCT NOVA). It is based on the official regulations and is designed to be easy to use.

The template already configures the main formatting requirements:

- Times New Roman, 11 pt font
- 2 cm margins on all sides
- 1.25 line spacing
- No blank pages between sections

## Features

-   **Correct Formatting**: Pre-set for FCT NOVA rules—margins, fonts, line spacing, page numbering and required sections.
-   **Structured Sections**: The thesis is organized into logical sections, with each chapter in its own file under the `sections/` directory.
-   **Glossary and Notation**: Includes a pre-configured glossary for acronyms and a list of notation. See `glossary.tex` for examples.
-   **Bibliography**: Uses `natbib` for citations and includes a `bibliography.bib` file for your references.
-   **Appendices**: Includes examples of how to add appendices to your thesis.

## How to Use

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```

2.  **Edit the content**:
    -   **`thesis.tex`**: Main file where you set the title, author name, supervisors and include or remove chapters.
    -   **`sections/`**: Each chapter has its own file (e.g., `introduction.tex`). Comments in these files describe the expected content and page limits.
    -   **`glossary.tex`**: Add your acronyms and notations here.
    -   **`bibliography.bib`**: Store bibliographic references in BibTeX format.
    -   **`figures/`**: Place your images here and include them using `\includegraphics`.

3.  **Compile the thesis**:
    To compile the thesis and generate the PDF, you will need a LaTeX distribution (e.g., TeX Live, MiKTeX). You also need to have the `xindy` and `makeglossaries` tools installed.

    Run the following commands in your terminal:

    ```bash
    pdflatex thesis.tex
    makeglossaries thesis
    pdflatex thesis.tex
    ```

    This will generate a `thesis.pdf` file with your compiled thesis. You may need to run `pdflatex thesis.tex` one more time to ensure all cross-references and citations are correct.

    Alternatively, you can use a LaTeX editor with integrated PDF compilation and build tools (e.g., TeXstudio, VS Code with the LaTeX Workshop extension). These editors can automate the compilation process.

## License

This template is provided as-is, without any warranty. You are free to use and modify it for your own purposes.
