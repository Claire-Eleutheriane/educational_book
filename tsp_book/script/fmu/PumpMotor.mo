model PumpMotor
  ThermoSysPro.ElectroMechanics.Machines.SynchronousMotor Motor(Im(start = 2000)) annotation(
    Placement(visible = true, transformation(extent = {{-80, -80}, {-60, -60}}, rotation = 0)));
  ThermoSysPro.WaterSteam.Machines.CentrifugalPump Pump(dynamic_mech_equation = true, mode_car = 2, mode_car_Cr = 1, mode_car_hn = 2, w_a(start = 1)) annotation(
    Placement(transformation(extent = {{0, -40}, {-20, -20}}, rotation = 0)));
  ThermoSysPro.WaterSteam.Volumes.Tank Tank(ze2 = 10, zs2 = 10) annotation(
    Placement(transformation(extent = {{-20, 20}, {0, 40}}, rotation = 0)));
  ThermoSysPro.WaterSteam.PressureLosses.ControlValve Valve annotation(
    Placement(transformation(extent = {{40, 20}, {60, 40}}, rotation = 0)));
  ThermoSysPro.InstrumentationAndControl.Blocks.Sources.Constante Constante1(k = 0.5) annotation(
    Placement(transformation(extent = {{0, 60}, {20, 80}}, rotation = 0)));
  ThermoSysPro.WaterSteam.PressureLosses.LumpedStraightPipe Pipe(continuous_flow_reversal = true, inertia = true) annotation(
    Placement(transformation(origin = {50, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  ThermoSysPro.InstrumentationAndControl.Blocks.Logique.Pulse Pulse(period=500, startTime = 1, width = 100) annotation(
    Placement(visible = true, transformation(extent = {{-100, -60}, {-80, -40}}, rotation = 0)));

equation
  connect(Pulse.yL, Motor.marche) annotation(
    Line(points = {{-79, -50}, {-70, -50}, {-70, -65.6}}));
  connect(Motor.C, Pump.M) annotation(
    Line(points = {{-59.8, -70}, {-10, -70}, {-10, -41}}));
  connect(Pump.C2, Tank.Ce2) annotation(
    Line(points = {{-20, -30}, {-60, -30}, {-60, 24}, {-20, 24}}, color = {0, 0, 255}));
  connect(Tank.Cs2, Valve.C1) annotation(
    Line(points = {{0, 24}, {40, 24}}, color = {0, 0, 255}));
  connect(Constante1.y, Valve.Ouv) annotation(
    Line(points = {{21, 70}, {50, 70}, {50, 41}}, color = {0, 0, 255}));
  connect(Pump.C1, Pipe.C2) annotation(
    Line(points = {{0, -30}, {40, -30}}));
  connect(Pipe.C1, Valve.C2) annotation(
    Line(points = {{60, -30}, {80, -30}, {80, 24}, {60, 24}}));
  annotation(
    Window(x = 0.32, y = 0.02, width = 0.39, height = 0.47),
    Diagram(coordinateSystem(preserveAspectRatio = false, extent = {{-100, -100}, {100, 100}}, grid = {2, 2}), graphics),
    uses(ThermoSysPro(version = "3.1")));
end PumpMotor;