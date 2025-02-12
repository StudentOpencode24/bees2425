#!/usr/bin/env pybricks-micropython
from hardware import *
def one1():
    """первый заезд теплица, забирает плуг и оборудвания для сена 
    """
    back_m.run_angle(200, 95) #запуск мотора для сбора ящиков
    front_m.run(9999)
    motor.straight(350) #подъезд к теплице
    wait(4) # ожидание пока собирает ящики
    move_speed_change(-150,40)
    motor.straight(-420)
    front_m.stop()
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(290) #возвращение в зону 

def one2():
    back_m.run_angle(200, 105)
    motor.straight(-270)
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(290) #возвращение в зону 

def two():
    """заезд с пшеницей
    """
    motor.straight(-20)
    back_m.run_angle(100, -90,wait = 0) #поднятие лапы
    motor.straight(745)
    motor.turn(95)
    motor.straight(100) # подъезд к пшенице
    # back_m.run_angle(100, 60) #сбор ящика
    motor.straight(-20)
    motor.turn(-90)
    motor.straight(-900) #возвращение в зону
    
def three():
    """выполнение яблони с забором контейнера 
    """
    motor.straight(-10)
    motor.straight(170)
    motor.reset()
    motor.drive(160, -80) # поворот по дуге для подъеза(вместе с while)
    while motor.angle() > -100:
       pass     
    motor.stop()
    move_speed_change(400, 280) # подъезд к яблокам
    motor.straight(-100)
    move_speed_change(400, 1000)
    wait(1000)
    motor.straight(-160)
    motor.turn(90)
    motor.straight(-400) # возвращение в зону

def four1():
    """переезд в красеую зону, с картошкой и зернохранилищем
    """
    back_m.run_angle(400, 100, wait= 0)
    motor.straight(-40)
    motor.straight(350)
    turn_acc_change(85, rate=1000)
    for i in range(1):
        motor.straight(273)
        motor.straight(-70)
    motor.straight(-70)
    motor.turn(-100)
    motor.straight(620)
    motor.turn(102)
    motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    motor.straight(130) # отъезд от кортофли
    motor.turn(-91) #сбор винограда
    back_m.run_angle(300, 90)
    move_By_Giro(400, 400, 2)
    back_m.run_angle(300, -80)
    move_speed_change(900, 400)

def four2():
    """переезд в красную зону, с картошкой без зернохранилища 
    """
    back_m.run_angle(300, 30, wait= 0)
    motor.straight(980)
    motor.turn(90)
    motor.straight(-630)
    # motor.turn(100)
    # motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    motor.straight(123) # отъезд от кортофли
    motor.turn(-91) #сбор винограда
    back_m.run_angle(300, 90)
    move_By_Giro(400, 400, 2)
    back_m.run_angle(300, -80)
    move_speed_change(900, 400)

def four3():
    """переезд в красеую зону, с картошкой и зернохранилищем
    """
    back_m.run_angle(400, 200, wait= 0)
    motor.straight(-40)
    motor.straight(350)
    turn_acc_change(85, rate=1000)
    for i in range(2):
        motor.straight(273)
        motor.straight(-70)
    motor.straight(-70)
    motor.turn(-100)
    motor.straight(620)
    motor.turn(102)
    motor.straight(-470)
    motor.drive(-100, 0) #подъезд к картофелю
    for _ in range(2): #несколько подъездов к кортофелю
        motor.straight(-150)
        motor.straight(60)
    motor.straight(123) # отъезд от кортофли
    motor.turn(-88) #сбор винограда
    move_speed_change(1000, 600, 1000)


def four4():
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
    motor.straight(123) # отъезд от кортофли
    motor.turn(-88) #сбор винограда
    move_speed_change(1000, 600, 1000)

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
    motor.straight(94)# подъезд к трактору
    front_m.run_angle(300, -60)
    motor.turn(-20)
    motor.turn(10)
    front_m.run_angle(300, -70)
    motor.stop() 
    motor.reset()
    motor.drive(-1000, 90)
    while motor.angle() < 145:
       pass  
    motor.stop() 
    motor.turn(70)

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
    # gyro.reset_angle(0)
    # while abs(gyro.angle()) < 30:
    #     motor.drive(0, -100)
#     motor.stop()
#     back_m.run_angle(800, 30, wait= 0)
#     move_speed_change(-500, 500, 1000) # подъезд к скотчу
#     motor.straight(350)
#     motor.turn(55)
#     motor.straight(-550)
def sixs():
    motor.straight(30)
    motor.straight(-250)
    back_m.run_angle(1000, -240)
    move_By_Giro(400, 450)
    motor.stop()
    back_m.run_angle(1000, 280)


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
    move_speed_change(1100, 1000, 600)
    motor.turn(70)

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
def power_down():
    while True:
        move_speed_change(1000, 1000, 1000)
    

# start([one, two, three, four, five, six, seven, f, eight])
start([[one1, one2], [two], [three], [four1, four2, four3, four4, front], [five], [f], [s], [nine1, nine2], [power_down]])


