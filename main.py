#!/usr/bin/env pybricks-micropython
from hardware import *
def one():
    """первый заезд теплица, забирает плуг и оорудвания для сена 
    """
    ev3.speaker.beep()
    back_m.run_angle(200, 95) #запуск мотора для сбора ящиков
    front_m.run(9999)
    motor.straight(350) #подъезд к теплице
    wait(4) # ожидание пока собирает ящики
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(290) #возвращение в зону 
    
def three():
    """выполнение яблони с забором контейнера 
    """
    ev3.speaker.beep()
    motor.straight(-10)
    motor.straight(170)
    motor.reset()
    motor.drive(160, -80) # поворот по дуге для подъеза(вместе с while)
    while motor.angle() > -100:
       pass     
    motor.stop()
    move_speed_change(400, 360) # подъезд к яблокам
    motor.straight(-100)
    move_speed_change(400, 1000)
    wait(1000)
    motor.straight(-160)
    motor.turn(90)
    motor.straight(-400) # возвращение в зону

def two():
    """_summary_
    """
    ev3.speaker.beep()  # заезд с пшеницей 
    motor.straight(-10)
    back_m.run_angle(100, -90,wait = 0) #поднятие лапы
    motor.straight(745)
    motor.turn(100)
    motor.straight(100) # подъезд к пшенице
    back_m.run_angle(100, 60) #сбор ящика
    motor.straight(-15)
    motor.turn(-90)
    motor.straight(-900) #возвращение в зону



def four1():
    """переезд в красеую зону, с картошкой и зернохранилищем
    """
    motor.straight(-20)
    ev3.speaker.beep()
    motor.straight(350)
    turn_acc_change(88, rate=1000)
    for i in range(2):
        motor.straight(273)
        motor.straight(-70)
    back_m.run_angle(50, 81, wait= 0)
    motor.straight(-70)
    motor.turn(-100)
    motor.straight(630)
    motor.turn(102)
    motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    motor.straight(135) # отъезд от кортофли
    motor.turn(-88) #сбор винограда
    move_speed_change(1200, 1000, 500)

def four2():
    """переезд в красную зону, с картошкой без зернохранилища 
    """
    motor.straight(980)
    motor.turn(90)
    motor.straight(-630)
    # motor.turn(100)
    # motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    motor.straight(140) # отъезд от кортофли
    motor.turn(-88) #сбор винограда
    move_speed_change(1200, 1000, 500)




def front():
    """заезд в красную зону для тренировки только красной зоны 
    """
    motor.straight(800)

def five():
    """выполняет виноградник и забирает трактор в синию зону
    """
    motor.straight(15)
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

def nine1():
    """последний заезд с иновационном проектом
    """
    motor.straight(-40)
    motor.straight(1040)
    motor.turn(50)
    motor.straight(360)
    motor.turn(51)
    motor.straight(280) #контейнеры в овощебазу
    motor.straight(-210)
    motor.turn(-45) #ин. проект
    motor.straight(-170)

def nine2():
    """последний заезд только с иновационным проектам
    """
    motor.straight(-1000)

def f():
    """завоз обарудования на поле
    """
    motor.straight(200)
    motor.straight(-100)
def s():
    """завоз тактора и плуга н поле
    """
    motor.straight(-280)    
    motor.straight(300)
    



# start([one, two, three, four, five, six, seven, f, eight])
start([[one], [two], [three], [four1, four2, front], [five], [f], [s], [nine1, nine2]])


