# Nova FCT Thesis Template

This is a LaTeX template for writing a thesis at the NOVA School of Science and Technology (FCT NOVA). It is based on the official regulations and is designed to be easy to use.

## Features

-   **Correct Formatting**: The template is pre-configured to follow the official FCT NOVA thesis formatting guidelines for margins, fonts, line spacing, and page numbering.
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
    -   **`thesis.tex`**: This is the main file. You should set your thesis title, author name, supervisor, etc., in this file.
    -   **`sections/`**: Each chapter of your thesis has its own `.tex` file in this directory (e.g., `introduction.tex`, `stateoftheart.tex`). Edit these files to write your content.
    -   **`glossary.tex`**: Add your acronyms and notations to this file. Follow the examples and comments in the file.
    -   **`bibliography.bib`**: Add your bibliographic references in BibTeX format to this file.
    -   **`figures/`**: Place your images in this directory and include them in your chapters using the `\includegraphics` command.

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
