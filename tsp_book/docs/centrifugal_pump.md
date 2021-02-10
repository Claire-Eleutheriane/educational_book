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

# A centrifugal pump system

We build and analyse a cooling system, based on a centrifugal pump.

## The model

The physics preceding the modeling choices of the component is detailed in {cite}`el2019modeling`.
The correspondance between theoretical and Modelica notations is explicited in the [centrifugal pump online documentation](https://thermosyspro.gitlab.io/documentation/src/WaterSteam/Machines/CentrifugalPump.html).

```{figure} /_static/centrifugal_pump/CentrifugalPump.svg
---
height: 250px
name: pump_image
---
Centrifugal pump symbol in ThermoSysPro.
```

We connect the centrifugal pump to a motor. The motor starts working at $t=0$ and activates the pump. A pipe links the pump to a water tank and to a valv. A resistance mimics the friction of the liquid on the inner side of the pipe. 

```{figure} /_static/centrifugal_pump/omedit_pump_motor.png
---
height: 250px
name: pump_motor_image
---
Cooling system using a centrifugal pump activated by a motor.
```


## Bibliography

```{bibliography} ../_bibliography/references.bib
```
