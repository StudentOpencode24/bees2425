#!/usr/bin/env pybricks-micropython
from hardware import *

def one():
    ev3.speaker.beep()
    back_m.run_angle(200, 95)
    front_m.run(9999)
    motor.straight(350) #подъезд к теплице
    wait(4)
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(260)

def two():
    ev3.speaker.beep()
    motor.straight(150)
    motor.reset()
    motor.drive(290, -88)
    while motor.angle() > -93:
       pass     
    motor.stop()

    move_speed_change(800, 9999) # подъезд к яблокам
    for _ in range(2):
        move_speed_change(100, 9999, 999)
        move_speed_change(-50, 9999, 999)
    #motor.straight(-150)
    #move_speed_change(500, 9999, 999)
    motor.straight(-100)
    motor.turn(90)
    motor.straight(-400)

def three():
    ev3.speaker.beep()
    back_m.run_angle(200, -110,wait = 0)
    motor.straight(710)
    motor.turn(90)
    motor.straight(100) # подъезд к пшенице
    back_m.run_angle(200, 95)
    motor.turn(-90)
    motor.straight(-710)
    # motor.straight(-10)
    # front_m.run_angle(-200, -110,wait = 0)
    # motor.turn(90)
    # move_speed_change(150, 100)
    # back_m.run_angle(900, 90)
    # motor.turn(-90)
    # motor.straight(-950)

def four():
    ev3.speaker.beep()
    motor.straight(-358)
    turn_acc_change(88, rate=1000)
    motor.straight(-273)
    for _ in range(2):
        motor.straight(30)
        motor.straight(-50) #подъезд к зерну
    motor.straight(130)
    motor.turn(-100)
    motor.straight(-620)
    motor.turn(105)
    motor.straight(470)
    motor.drive(200, 0) #подъезд к картофелю
    wait(1)
    for _ in range(2):
        motor.straight(150)
        motor.straight(-100)
    motor.straight(-100) # отъезд от кортофли
    motor.turn(-90) #сбор винограда
    motor.straight(-1000)

def five():
    motor.straight(-20)
    motor.straight(450)
    motor.turn(-35)
    motor.straight(88)
    motor.turn(35)
    motor.straight(180) #подъезд к винограду
    motor.straight(-160)
    motor.turn(90)
    motor.straight(-90) # подъезд к трактору
    back_m.run_angle(300, -125)
    motor.stop() 
    motor.reset()
    motor.drive(1000, 85)
    while motor.angle() < 145:
       pass  
    motor.stop() 
    motor.turn(30)

def six():
    motor.straight(-80)
    back_m.run_angle(500, 215) # сбор рамки скотча
    motor.turn(-20)
    motor.straight(300)

def seven():
    back_m.run_angle(500, -10, wait = 0)
    motor.straight(100)
    gyro.reset_angle(0)
    while abs(gyro.angle()) < 30: # поворот по гироскопу на 30
        motor.drive(0, 100)
    motor.stop()
    motor.straight(430)
    gyro.reset_angle(0)
    while abs(gyro.angle()) < 26:
        motor.drive(0, -100)
    motor.stop()
    back_m.run_angle(800, 30, wait= 0)
    motor.straight(-500) # подъезд к скотчу
    motor.straight(350)
    motor.turn(55)
    motor.straight(-550)

def eight():
    motor.straight(-10)
    motor.straight(1000)
    motor.turn(45)
    motor.straight(370)
    motor.turn(50)
    motor.straight(300) # контейнеры в овощебаза
    motor.straight(-400)
    motor.turn(-90)
    motor.straight(-150) # иновационный проект

start([one, two, three, four, five, six, seven, eight])