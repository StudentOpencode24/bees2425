#!/usr/bin/env pybricks-micropython
from hardware import *
def one():
    ev3.speaker.beep()
    back_m.run_angle(200, 95)
    front_m.run(9999)
    motor.straight(350)
    wait(4)
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105)
    motor.straight(260)

def two():
    ev3.speaker.beep()
    motor.straight(150)
    motor.reset()
    motor.drive(290, -88)
    while motor.angle() > -93:
       pass     
    motor.stop()

    move_speed_change(800, 9999)
    for _ in range(4):
        move_speed_change(100, 9999, 999)
        move_speed_change(-50, 9999, 999)
    #motor.straight(-150)
    #move_speed_change(500, 9999, 999)
    motor.straight(-100)
    motor.turn(90)
    motor.straight(-400)

def three():
    motor.straight(-10)
    front_m.run_angle(-200, -110,wait = 0)
    motor.turn(90)
    move_speed_change(150, 100)
    back_m.run_angle(900, 90)
    motor.turn(-90)
    motor.straight(-950)

def four():
    ev3.speaker.beep()
    motor.straight(-355)
    turn_acc_change(90, rate=50)
    motor.straight(-275)
    for _ in range(2):
        motor.straight(30)
        motor.straight(-50)
    motor.straight(130)
    motor.turn(-100)
    motor.straight(-620)
    motor.turn(105)
    motor.straight(500)
    motor.drive(200, 0) #подъезд к картофелю
    wait(1)
    for _ in range(2):
        motor.straight(100)
        motor.straight(-50)
    motor.straight(-160) # отъезд от кортофли
    motor.turn(-90)
    motor.straight(-1000)

def five():
    back_m.run_angle(300  ,180)

def six():
    motor.straight(-20)
    motor.straight(200)
    back_m.run_angle(300, -110,wait = 0)
    motor.turn(-15)
    motor.straight(210)
    motor.turn(15)
    motor.straight(290) #подъезд к винограду
    motor.straight(-130)
    back_m.run_angle(200, -100)
    motor.turn(90)
    motor.straight(-90)
    back_m.run_angle(300, 100)
    motor.straight(-600)
    motor.turn(100)
    motor.straight(500)
    # motor.turn(100)


start([one, two, three, four, five, six])