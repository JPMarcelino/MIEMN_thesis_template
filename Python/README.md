# Python figure helpers

Scripts and notebooks for producing results go here. `PI_eg.ipynb` is a
worked example.

## Compliant figures in one line

The DCM rules require plots to use **Arial, 28 pt for the tick numbers
and 30–32 pt for the axis labels**, with units on every axis. The
`miemn.mplstyle` file encodes exactly that, so you only have to opt in:

```python
import matplotlib.pyplot as plt
import figure_style

figure_style.use_thesis_style()

fig, ax = plt.subplots()          # 17 cm wide, the text-block width
ax.plot(x, y)
ax.set_xlabel("Time (ns)")        # 31 pt, Arial
ax.set_ylabel("Voltage (mV)")
ax.tick_params(axis="both")       # ticks are 28 pt

figure_style.save_figure(fig, "../figures/Python/my-plot")
```

`save_figure` writes both a PDF (include this in the thesis) and a PNG
(preview). The PDF has fonts embedded (Type 42) so it renders correctly
everywhere.

If your figure is narrower than the full text block, keep the physical
size by *not* scaling it down in LaTeX:

```latex
\includegraphics[width=0.8\textwidth]{my-plot.pdf}
```

## Vector vs raster

- Line plots, schematics, block diagrams → PDF (vector).
- Photos, micrographs, screenshots → PNG/TIFF at ≥ 300 dpi.
