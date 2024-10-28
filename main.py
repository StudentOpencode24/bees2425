#!/usr/bin/env pybricks-micropython
from hardware import *

def first():
    ev3.speaker.beep()
    back_m.run_angle(200, 95)
    front_m.run(9999)
    motor.straight(350)
    wait(4)
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105)
    motor.straight(234)

def sec():
    ev3.speaker.beep()
    motor.straight(-355)
    turn_acc_change(90, rate=50)
    motor.straight(-275)
    for i in range(2):
        motor.straight(30)
        motor.straight(-50)
    motor.straight(130)
    motor.turn(-100)
    motor.straight(-630)
    motor.turn(105)
    motor.straight(500)
    motor.drive(200, 0)
    wait(1)
    for _ in range(2):
        motor.straight(100)
        motor.straight(-50)
    motor.straight(-165) # отъезд от кортофли
    motor.turn(-90)
    motor.straight(-1000)

def third():
    ev3.speaker.beep()
    motor.straight(250)
    motor.turn(90)
    motor.straight(100)
    back_m.run_angle(200, 95)
    motor.turn(-90)
    motor.straight(300)

first()