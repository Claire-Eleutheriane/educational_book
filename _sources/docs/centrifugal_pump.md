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

# A cooling system

We consider a cooling system relying on a centrifugal pump, activated by a motor (see Figure 1). A centrifugal pump converts rotational energy from a motor to energy in a moving fluid, which creates pressure.

The purpose of this case study is to build the cooling system model and check its adequation with the reality.

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

We are interested in the mass flow rate at the output of the pump. The mass flow rate must reach a defined nominal value for the installation to work properly.

```{figure} /_static/centrifugal_pump/pump_output.png
---
height: 250px
name: pump_output_image
---
Evolution of the fluid mass flow rate in the pipe after switching on the motor.
```


## Understanding the system parameters

The centrifugal pump has two characteristic functions, usually provided by the manufacturer.
Both apply to the average volumetric flow rate $q$ divided by the shaft angular speed $\omega$.
The first characteristic $f_\eta$ relates the pump hydraulic efficiency to the ratio.
The other characteristic $f_h$ relates the pump head to the ratio.

These characteristics are approximated by second-order polynomials in the pump component:

$$f_h\left(\frac{q}{\omega}\right) = a_0 + a_1\left(\frac{q}{\omega}\right) + a_2\left(\frac{q}{\omega}\right)^2$$

$$f_\eta\left(\frac{q}{\omega}\right) = b_0 + b_1\left(\frac{q}{\omega}\right) + b_2\left(\frac{q}{\omega}\right)^2$$

To understand the effect of the characteristic parameters, we modify their value.


## Bibliography

```{bibliography} ../_bibliography/references.bib
```
