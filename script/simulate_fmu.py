# -*- coding: utf-8 -*-
# @Author: Claire-Eleutheriane Gerrer
# @Date:   2019-09-17 14:43:37
# @Last Modified by:   Claire-Eleuthèriane Gerrer
# @Last Modified time: 2021-02-17 13:48:50

from simulate import fmpy_sim
import pandas as pd
import numpy as np
from os.path import join
import matplotlib.pyplot as plt

directory = "fmu"
fmu_filename = "PumpMotor.fmu"
path_fmu = join(directory, fmu_filename)


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
kwargs = fmpy_sim.get_recommended_dict()
kwargs.update({"stop_time": 50, "output": output_filter})

list_df = fmpy_sim.simulate_on_doe(
    list_input, doe_data, path_fmu, **kwargs)

# Plot the simulation

plt.figure()
for (df, value) in zip(list_df, doe_data):
    plt.plot(df["Pipe.Q"], label=str(value[0]))
plt.legend()
plt.show()
