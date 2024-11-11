from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog#, multitask, run_task
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color
# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
lmot = Motor(Port.B, gears=[28, 20])
rmot = Motor(Port.C, gears=[28, 20])
front_m = Motor(Port.A, gears=[12, 20])
back_m = Motor(Port.D, gears=[12, 20])
motor = DriveBase(lmot, rmot, 49.5, 119)

turn_acceleration = 500
straight_acceleration = 500


motor.settings(straight_speed=1000, straight_acceleration=straight_acceleration, turn_rate=200, turn_acceleration=turn_acceleration)

def turn_acc_change(ang, rate = 1000, acc = turn_acceleration):
    motor.stop()
    motor.settings(turn_rate=rate, turn_acceleration=acc)
    motor.turn(ang)
    motor.stop()
    motor.settings(turn_rate=1000, turn_acceleration = turn_acceleration)
    

def move_speed_change(distance, speed=1000, acc=straight_acceleration):
    motor.stop()
    motor.settings(straight_speed=speed, straight_acceleration=acc)
    motor.straight(distance)
    motor.stop()
    motor.settings(straight_speed=1000, straight_acceleration = straight_acceleration)