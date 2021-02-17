---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(centrifugal_pump)=

# Centrifugal pump

A centrifugal pump converts rotational energy from a motor to energy in a moving fluid, which creates pressure.

```{figure} /_static/centrifugal_pump/scheme.png
---
height: 300px
name: scheme
---
Schematic diagramm of a centrifugal pump.
```

The purpose of this case study is to understand the functioning of the pump component and model a cooling system.

## CentrifugalPump versus StaticCentrifugalPump

Two ThermoSysPro components model a centrifugal pump: [StaticCentrifugalPump](https://thermosyspro.gitlab.io/documentation/src/WaterSteam/Machines/StaticCentrifugalPump.html) and [CentrifugalPump](https://thermosyspro.gitlab.io/documentation/src/WaterSteam/Machines/CentrifugalPump.html).

For the static centrifugal pump, the rotational speed of the pump is fixed.
It is therefore impossible to diminish the pump speed to regulate or modify the output flow.
The centrifugal pump however accepts modifications of the rotational speed during operations.
% FALSE : IN MODELICA, THE ROTATION SPEED IS A PARAMETER FOR BOTH CASES.

```{figure} /_static/centrifugal_pump/static_vs_dynamic.png
---
height: 200px
name: static_vs_dynamic
---
StaticCentrifugalPump (left) and CentrifugalPump (right).
```

In the following case study, we employ the CentrifugalPump component.

## The model

The physics preceding the modeling choices of the component is detailed in {cite}`el2019modeling`.
The correspondance between theoretical and Modelica notations is explicited in the [centrifugal pump online documentation](https://thermosyspro.gitlab.io/documentation/src/WaterSteam/Machines/CentrifugalPump.html).

%```{figure} /_static/centrifugal_pump/CentrifugalPump.svg
%---
%height: 250px
%---
%Centrifugal pump symbol in ThermoSysPro.
%```

We connect the centrifugal pump to a motor. The motor starts working at $t=0$ and activates the pump. A pipe links the pump to a water tank and to a valv. A resistance mimics the friction of the liquid on the inner side of the pipe. 

```{figure} /_static/centrifugal_pump/omedit_pump_motor.png
---
height: 300px
name: pump_motor_image
---
Cooling system using a centrifugal pump activated by a motor.
```

We are interested in the mass flow rate at the output of the pump. The mass flow rate must reach a defined nominal value for the installation to work properly.

```{figure} /_static/centrifugal_pump/pump_output.png
---
height: 250px
name: pump_output_image
---
Evolution of the fluid mass flow rate in the pipe after switching on the motor.
```


## Understanding the pump characteristics

```{code-cell} ipython3
:tags: [hide-cell]
from bokeh.plotting import figure, show, output_notebook
import numpy as np
output_notebook()
```

The efficiency of the pump is quantified by its hydraulic efficiency $\eta_h$, and the pump head $h_n$.  
The hydraulic efficiency relates the useful mechanical work to the work produced by the shaft.
It is linked the hydraulic torque $T_h$.  
The pump head is the height at which the pump can raise water up.

The centrifugal pump has two characteristic functions, usually provided by the manufacturer.
Both apply to the angle between the average volumetric flow rate $q$ divided by the shaft angular speed $\omega$:

$$\theta = arctan\left(\frac{q}{\omega}\right) $$

The head characteristic $F$ relates the pump head $h_n$ to the angle $\theta$:

$$ \frac{h_n}{q^2 + \omega^2} = F(\theta). $$

The torque characteristic $G$ relates the pump hydraulic torque $T_h$ to the angle $\theta$:

$$ \frac{T_h}{q^2 + \omega^2} = G(\theta).$$


Two modes are possible for the characteristics, depending on the parameters `mode_car_hn` and `mode_car_Cr`.

If `mode_car_hn`=2, the head characteristic is semi-parabolic : only positive values of $q$ and $\omega$ are authorized. The head characteristic is computed from the two coefficients `hn_coef`.  
If `mode_car_hn`=1, the head characteristic is complete. It is interpolated from the table `F_t`.

```{code-cell} ipython3
:tags: [hide-input]
data = [0.634, 0.643, 0.646, 0.640, 0.629, 0.613, 0.595, 0.575, 0.552, 0.533,
0.516, 0.505, 0.504, 0.510, 0.512, 0.522, 0.539, 0.559, 0.580, 0.601, 0.630,
0.662, 0.692, 0.722, 0.753, 0.782, 0.808, 0.832, 0.857, 0.879, 0.904, 0.930,
0.959, 0.996, 1.027, 1.060, 1.090, 1.124, 1.165, 1.204, 1.238, 1.258, 1.271,
1.282, 1.288, 1.281, 1.260, 1.225, 1.172, 1.107, 1.031, 0.942, 0.842, 0.733,
0.617, 0.500, 0.368, 0.240, 0.125, 0.011, -0.102, -0.168, -0.255, -0.342,
-0.423, -0.494, -0.556, -0.620, -0.655, -0.670, -0.670, -0.660, -0.655, -0.640,
-0.600, -0.570, -0.520, -0.470, -0.430, -0.360, -0.275, -0.160, -0.040, 0.130,
0.295, 0.430, 0.550, 0.620, 0.634]
p = figure(plot_width=400, plot_height=400, x_range=(-3.14, 3.14))
array_x = np.linspace(- np.pi, np.pi, len(data))
p.line(array_x, data)
show(p)
```

Similarly, if `mode_car_Cr`=2, the torque characteristic is semi-parabolic. It is computed using the two coefficients `rh_coef`.  
If `mode_car_Cr`=1, the torque characteristic is complete. It is interpolated from the table `G_t`.

```{code-cell} ipython3
:tags: [hide-input]
data = [-0.684, -0.547, -0.414, -0.292, -0.187, -0.105, -0.053, -0.012, 0.042, 0.097, 0.156, 0.227,0.300, 0.371, 0.444, 0.522, 0.596, 0.672, 0.738, 0.763, 0.797, 0.837, 0.865, 0.883,0.886, 0.877, 0.859, 0.838, 0.804, 0.758, 0.703, 0.645, 0.583, 0.520, 0.454, 0.408, 0.370, 0.343, 0.331, 0.329, 0.338, 0.354, 0.372, 0.405, 0.450, 0.486, 0.520, 0.552, 0.579, 0.603, 0.616, 0.617, 0.606, 0.582, 0.546, 0.500, 0.432, 0.360, 0.288, 0.214, 0.123, 0.037, -0.053, -0.161, -0.248, -0.314, -0.372, -0.580, -0.740, -0.880, -1.000, -1.120, -1.250, -1.370, -1.490, -1.590, -1.660, -1.690, -1.770, -1.650, -1.590, -1.520, -1.420, -1.320, -1.230, -1.100, -0.980, -0.820, -0.684]
p = figure(plot_width=400, plot_height=400, x_range=(-3.14, 3.14))
array_x = np.linspace(- np.pi, np.pi, len(data))
p.line(array_x, data)
show(p)
```


## Bibliography

```{bibliography} ../_bibliography/references.bib
```
