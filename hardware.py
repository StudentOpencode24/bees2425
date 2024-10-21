from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.

lmot = Motor(Port.B)
rmot = Motor(Port.C)
front_m = Motor(Port.A, gears=[12, 20])
back_m = Motor(Port.D, gears=[12, 20])
motor = DriveBase(lmot, rmot, 49.5 / 20 * 28, 119)

turn_acceleration = 500
straight_acceleration = 500


motor.settings(straight_speed=9999, straight_acceleration=straight_acceleration, turn_acceleration=turn_acceleration)

def turn_acc_change(ang, rate = 9999, acc = turn_acceleration):
    motor.stop()
    motor.settings(turn_rate=rate, turn_acceleration=acc)
    motor.turn(ang)
    motor.stop()
    motor.settings(turn_rate=9999, turn_acceleration = turn_acceleration)
    

def move_speed_change():
    pass