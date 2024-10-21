#!/usr/bin/env pybricks-micropython
from hardware import *

def first():
    ev3.speaker.beep()
    back_m.run_angle(200, 95)
    front_m.run(9999)
    motor.straight(350)
    wait(2)
    motor.straight(-570)
    front_m.stop()
    back_m.run_angle(200, -105)
    motor.straight(218)

def sec():
    ev3.speaker.beep()
    motor.straight(-360)
    turn_acc_change(90, rate=50)
    motor.straight(-275)
    for i in range(2):
        motor.straight(30)
        motor.straight(-50)
    motor.straight(130)
    motor.turn(-100)
    motor.straight(-660)
    motor.turn(100)
    motor.straight(500)
    motor.drive(200, 0)
    wait(1)
    for _ in range(2):
        motor.straight(100)
        motor.straight(-50)
    motor.straight(-180)
    motor.turn(90)

sec()