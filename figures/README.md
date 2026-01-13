# Figure Assets for Thesis Template

This directory should contain all images and figures used in your thesis.

## Required Images

### University Logo
- **File**: `university-logo.png` (or .pdf, .jpg)
- **Purpose**: University logo on the title page
- **Location**: Title page, cover page
- **Format**: PNG, PDF, or JPG (vector fonts recommended)
- **Resolution**: At least 300 DPI for print quality
- **Size**: Approximately 3-5 cm width when inserted

## Directory Structure

```
figures/
├── university-logo.png      # [REQUIRED] University logo
├── Python/                   # Python/Matplotlib generated figures
│   ├── figure1.png
│   └── ...
├── Results/                  # Experimental results
│   ├── result1.png
│   └── ...
├── Schematics/               # Circuit diagrams, block diagrams
│   ├── schematic1.pdf
│   └── ...
├── Plots/                    # Data plots
│   ├── plot1.pdf
│   └── ...
└── Photos/                   # Device photos, microscopy images
    ├── photo1.jpg
    └── ...
```

## Image Guidelines

### File Formats

- **Vector formats** (preferred for diagrams):
  - `.pdf` - Best for schematics, plots, line drawings
  - `.eps` - Alternative vector format

- **Raster formats** (for photos):
  - `.png` - Good for screenshots, photos with text
  - `.jpg` - Good for continuous-tone photos
  - `.tiff` - High-quality archival format

### Resolution

- **For online viewing**: 72-150 DPI
- **For print**: 300 DPI minimum
- **For figures with small text**: 600 DPI recommended

### Color

- Use high contrast for better readability
- Consider colorblind-friendly palettes
- Test in grayscale if printing in black & white

### Naming Conventions

Use descriptive, lowercase filenames with underscores:
- `good-example.png` ✓
- `chapter2_result3.pdf` ✓
- `Figure 1.JPG` ✗ (avoid spaces)
- `FinalVersion.png` ✗ (avoid ambiguous names)

### Organization

Organize figures by:
- Chapter number (e.g., `ch3_figure1.pdf`)
- Type (e.g., `schematic_blockdiagram.pdf`)
- Content (e.g., `python_trainingloss.png`)

## Including Figures in LaTeX

Basic figure inclusion:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/your-figure.png}
    \caption{Your figure caption}
    \label{fig:your-label}
\end{figure}
```

With subfigures:
```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/fig1a.png}
        \caption{Subfigure (a)}
        \label{fig:fig1a}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/fig1b.png}
        \caption{Subfigure (b)}
        \label{fig:fig1b}
    \end{subfigure}
    \caption{Combined figure caption}
    \label{fig:fig1}
\end{figure}
```

## Placeholder Images

If you don't have images yet, you can use:
1. `\usepackage{lipsum}` for placeholder text
2. `\rule{width}{height}` for placeholder boxes
3. Comment out `\includegraphics` temporarily
4. Use `demo` option in graphicx: `\usepackage[demo]{graphicx}`

## Tips

1. **Keep figures consistent** - Use the same style for similar figures
2. **Use vector formats** when possible - they scale better
3. **Test in grayscale** - Ensure figures are readable in B&W
4. **Keep file sizes reasonable** - Large PDFs can cause compilation issues
5. **Check licensing** - Use properly licensed images or create your own

## Common Issues

### Compilation errors with figures
- Check file paths are correct
- Ensure filenames don't have spaces
- Verify the file format is supported
- Check if the file exists in the correct directory

### Low quality in PDF
- Use vector formats (.pdf, .eps) for diagrams
- Ensure raster images are at least 300 DPI
- Avoid enlarging images beyond their resolution

### Figure placement issues
- Use `\begin{figure}[htbp]` for more placement options
- Add `!` before placement specifiers: `\begin{figure}[!htbp]`
- Consider using the `\float` package for advanced control

## Resources

- [LaTeX Graphics Companion](https://ctan.org/pkg/graphics) - Official documentation
- [TikZ and PGF](https://ctan.org/pkg/pgf) - Drawing with LaTeX
- [matplotlib](https://matplotlib.org/) - Python plotting with LaTeX support
- [draw.io](https://www.draw.io/) - Free diagramming tool
