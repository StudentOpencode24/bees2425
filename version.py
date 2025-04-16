#!/usr/bin/env pybricks-micropython3
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks import version
# print(version)

lmot = Motor(Port.B, gears=[28, 20])
rmot = Motor(Port.C, gears=[28, 20])
motor = DriveBase(lmot, rmot, 49.5, 119)

print([method for method in dir(motor) if callable(getattr(motor, method))])