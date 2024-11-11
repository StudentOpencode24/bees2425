#!/usr/bin/env pybricks-micropython
from hardware import *
click = 0
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
    motor.straight(260)

def sec():
    ev3.speaker.beep()
    motor.straight(150)
    motor.reset()
    motor.drive(290, -90)
    while motor.angle() > -90:
       pass     
    motor.stop()
    motor.settings(straight_acceleration = 1000)
    motor.straight(500)
    for _ in range(2):
        motor.straight(150)
        motor.straight(-40)
    motor.straight(-150)
    move_speed_change(400, 9999)
    motor.straight(-280)
    motor.turn(90)
    motor.straight(-400)

def third():
    motor.straight(-10)
    front_m.run_angle(-200, -110,wait = 0)
    motor.turn(90)
    move_speed_change(150, 100)
    back_m.run_angle(900, 90)
    motor.turn(-90)
    motor.straight(-950)

def fourth():
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
a = [first, sec, third, fourth]
while not Button.CENTER in ev3.buttons.pressed():
    if Button.LEFT in ev3.buttons.pressed():
        ev3.screen.clear()
        click += 1
        if click >= len(a):
            click = 0
        ev3.screen.draw_text(30, 50, str(click))
        while Button.LEFT in ev3.buttons.pressed():
            pass
    if Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.clear()
        click -= 1
        if click < 0:
            click = len(a) - 1
        ev3.screen.draw_text(30, 50, str(click))
        while Button.RIGHT in ev3.buttons.pressed():
            pass
    wait(100)

if Button.CENTER in ev3.buttons.pressed():
    ev3.screen.draw_text(30, 50, click)
    a[click]()

