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

# Test running FMU online

```{code-cell} ipython3
import numpy as np
from os.path import join
import fmpy

directory = "../script/fmu"
fmu_filename = "PumpMotor.fmu"
path_fmu = join(directory, fmu_filename)

kwargs = {
        "validate": False, "fmi_type": "ModelExchange", "solver": "CVode",
        "relative_tolerance": 1e-6
}
result = fmpy.simulate_fmu(path_fmu, **kwargs)
print(result)
```

