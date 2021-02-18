---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.8.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Run small FMU tests

```{code-cell} ipython3
import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import fmpy

# Establish parameter bounds

n_simu = 5

dic_nominal = {
    "Pump.hn_coef[1]": -88.67,
    "Pump.hn_coef[2]": 43.15
}

dic_range = {
    "Pump.hn_coef[1]": np.linspace(-100, -60, n_simu),
    "Pump.hn_coef[2]": np.linspace(20, 60, n_simu)
}

# Define simulation parameters

list_input = ["Pump.hn_coef[1]"]
list_output = ["Pipe.Q"]
output_filter = list_input.extend(list_output)
final_time = 50

doe_data = np.array([[xx] for xx in dic_range[list_input[0]]])
kwargs = {
        "validate": False, "fmi_type": "ModelExchange", "solver": "CVode",
        "relative_tolerance": 1e-6, "stop_time": 50, "output": output_filter}

directory = "../script/fmu"
fmu_filename = "PumpMotor.fmu"
path_fmu = join(directory, fmu_filename)

result = fmpy.simulate_fmu(path_fmu, **kwargs)
print(result[:3])
```

```{code-cell} ipython3
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
newpath = os.path.join(parent_dir, "script")
sys.path.insert(0, newpath) 
import fmpy_sim

list_df = fmpy_sim.simulate_on_doe(
    list_input, doe_data, path_fmu, **kwargs)
```

```{code-cell} ipython3
# Plot the simulation

from bokeh.plotting import figure, show, output_notebook
output_notebook()
```

```{code-cell} ipython3
from bokeh.palettes import Category10
colormap = Category10[n_simu]

p = figure(plot_width=400, plot_height=400)
list_color = [""]
for (df, value, color) in zip(list_df, doe_data, colormap):
    p.line(df.index, df[list_output[0]], legend_label=str(value[0]), color=color)
p.legend.location = "bottom_right"
p.legend.title = list_input[0]
show(p)
```

```{code-cell} ipython3

```
