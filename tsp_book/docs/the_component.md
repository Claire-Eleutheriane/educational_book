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

# The component

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

*CentrifugalPump* is a very general pump model, which enables all functioning modes except for cavitation.
This component covers all functioning modes in static as well as in dynamic.
In practice, we need the characteristic on the four quadrants which are rarely given by the pump constructors.

```{figure} /_static/centrifugal_pump/characteristic_domain.png
---
height: 400px
name: characteristic_domain
---
Centrifugal pump operating domains.
```

*StaticCentrifugalPump* can be seen as a static restriction of CentrifugalPump to the first quadrant, corresponding to "Normal pumping".
This component must be used only in normal functioning, even only in nominal functioning as dynamic aspects are neglected.

*StaticCentrifugalPump* thus corresponds to *CentrifugalPump* with:
- static equations (derived terms are removed),
- semi-parabolic head characteristic,
- semi-parabolic torque characteristic (analytic formula which is exact only around the nominal point $\theta = \frac{\pi}{4}$).

```{figure} /_static/centrifugal_pump/static_vs_dynamic.png
---
height: 200px
name: static_vs_dynamic
---
*StaticCentrifugalPump* (left) and *CentrifugalPump* (right).
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


## Bibliography

```{bibliography} ../_bibliography/references.bib
```
