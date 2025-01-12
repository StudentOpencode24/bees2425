#!/usr/bin/env pybricks-micropython
from hardware import *
#на глаз напротив теплицы
def one():
    ev3.speaker.beep()
    back_m.run_angle(200, 95) #запуск мотора для сбора ящиков
    front_m.run(9999)
    motor.straight(350) #подъезд к теплице
    wait(4) # ожидание пока собирает ящики
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(260) #возвращение в зону
    
def three():
    ev3.speaker.beep()
    motor.straight(160)
    motor.reset()
    motor.drive(160, -80) #поворот по дуге для подъеза(вместе с while)
    while motor.angle() > -100:
       pass     
    motor.stop()
    move_speed_change(500, 9999) # подъезд к яблокам
    move_speed_change(200, 9999, 999) #подъезд на высокой скорости
    motor.straight(-150)
    motor.turn(90)
    motor.straight(-400) #возвращение в зону

def two():
    ev3.speaker.beep()
    motor.straight(-10)
    back_m.run_angle(100, -90,wait = 0) #поднятие лапы
    motor.straight(745)
    motor.turn(90)
    motor.straight(100) # подъезд к пшенице
    back_m.run_angle(100, 90) #сбор ящика
    motor.straight(-15)
    motor.turn(-90)
    motor.straight(-900) #возвращение в зону


def four():
    ev3.speaker.beep()
    back_m.run_angle(50, 81, wait= 0)
    motor.straight(350)
    turn_acc_change(88, rate=1000)
    for i in range(2):
        motor.straight(273)
        motor.straight(-70)
    motor.straight(-70)
    motor.turn(-100)
    motor.straight(620)
    motor.turn(100)
    motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    back_m.run_angle(50, -58, wait=0)
    motor.straight(90) # отъезд от кортофли
    motor.turn(-88) #сбор винограда
    move_speed_change(280, 400, 500)
    move_speed_change(160, 390, 490)
    back_m.run_angle(1000, 90)
    motor.straight(800)

def five():
    motor.straight(10)
    motor.straight(-450)
    motor.turn(-35)
    motor.straight(-88)
    motor.turn(33)
    motor.straight(-180) #подъезд к винограду
    motor.straight(160)
    motor.turn(90)
    motor.straight(90) # подъезд к трактору
    front_m.run_angle(300, -125)
    motor.stop() 
    motor.reset()
    motor.drive(-1000, 80)
    while motor.angle() < 145:
       pass  
    motor.stop() 
    motor.turn(60)

# def six():
#     motor.straight(-100)
#     back_m.run_angle(500, 215) # сбор рамки скотча
#     motor.turn(-30)
#     motor.straight(380)

# def seven():
#     motor.straight(97)
#     gyro.reset_angle(0)
#     while abs(gyro.angle()) < 30: # поворот по гироскопу на 30
#         motor.drive(0, 100)
#     motor.stop()
#     motor.straight(430)
#     gyro.reset_angle(0)
#     while abs(gyro.angle()) < 30:
#         motor.drive(0, -100)
#     motor.stop()
#     back_m.run_angle(800, 30, wait= 0)
#     move_speed_change(-500, 500, 1000) # подъезд к скотчу
#     motor.straight(350)
#     motor.turn(55)
#     motor.straight(-550)

def nine():
    motor.straight(1040)
    motor.turn(45)
    motor.straight(340)
    motor.turn(50)
    motor.straight(280) #контейнеры в овощебазу
    motor.straight(-210)
    motor.turn(-45) #ин. проект
    motor.straight(-150)

def f():
    motor.straight(200)
    motor.straight(-300)
def s():
    motor.straight(-280)
    motor.straight(300)
    



# start([one, two, three, four, five, six, seven, f, eight])
start([one, two, three, four, five, f, s, nine])
click = 0


# Добавить поворот на забирании напралющей для рулонника
# Добавить поврот на отвозе рулоннника
