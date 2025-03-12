#!/usr/bin/env pybricks-micropython
from hardware import *
def one1():
    """первый заезд теплица, забирает плуг и оборудвания для сена 
    """
    back_m.run_angle(200, 95) #запуск мотора для сбора ящиков
    front_m.run(-9999)
    move_speed_change(240, 400) #подъезд к теплице. Блок 1
    wait(200) # ожидание пока собирает ящики
    move_speed_change(-50, 200)
    move_speed_change(100, 400) #подъезд к теплице. Блок 2
    wait(200) # ожидание пока собирает ящики
    move_speed_change(-150,100)
    motor.straight(-410)
    front_m.stop()
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(270) #возвращение в зону 
    back_m.run_angle(800, -1500)
    back_m.run_angle(800, 1700)

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
    back_m.run_angle(1000, 82) #сбор ящика
    motor.straight(-20)
    motor.turn(-90)
    motor.straight(-900) #возвращение в зону
    
def three():
    """выполнение яблони с забором контейнера 
    """
    motor.straight(-30)
    motor.straight(260)
    motor.turn(-65)
    motor.straight(90)
    motor.turn(-25)
    move_speed_change(400, 280) # подъезд к яблокам
    motor.straight(-100)
    move_speed_change(400, 1000)
    wait(1000)
    motor.straight(-140)
    motor.turn(90)
    motor.straight(-400) # возвращение в зону

def four1():
    """переезд в красеую зону, с картошкой и зернохранилищем
    """
    front_m.run_angle(800, -7, wait=0)
    motor.straight(-10)
    motor.straight(355)
    turn_acc_change(90, rate=1000)
    for i in range(1):
        motor.straight(273)
        motor.straight(-70)
    motor.straight(-70)
    motor.turn(-100)
    motor.straight(620)
    motor.turn(104)
    front_m.run_angle(800, 50, wait=0)
    move_speed_change(-550, 400) #подъезд к картофелю
    motor.straight(60)
    motor.straight(-150)
    motor.straight(138) # подъезд к комбайну
    back_m.run_angle(800, -1560)
    back_m.run_angle(800, 1580, wait=0)
    wait(500)
    motor.straight(60) 
    motor.turn(-89) #сбор винограда
    motor.straight(1100)

def four2():
    """переезд в красную зону, с картошкой без зернохранилища 
    """
    motor.straight(-3)
    back_m.run_angle(400, 100, wait= 0)
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
    move_speed_change(400, 200)
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
    motor.straight(30)
    front_m.run_angle(1000, -3100, wait= 0)
    motor.straight(-500)
    back_m.run_angle(550, -600, wait= 0)
    motor.straight(-200)
    motor.straight(150)
    motor.turn(90)
    motor.straight(160)
    front_m.run_angle(1000, 1000)
    motor.straight(-200)
    motor.turn(100)
    motor.straight(-700)
    motor.turn(90)

    
def five1():
    front_m.run_angle(1000, 1000)
    

def six():
    # front_m.run_angle(1000, -4000)
    motor.straight(-8)
    front_m.run_angle(500, 70, wait=0)
    motor.straight(190)
    motor.turn(90)
    motor.straight(130)
    front_m.run_angle(500, -85) # сбор рамки скотча
    motor.turn(-30)
    motor.straight(-220)

def seven():
    motor.straight(-8)
    motor.straight(200)
    front_m.run_angle(250, -110)
    move_speed_change(-250, 250)
    move_speed_change(50, 250)
    motor.turn(30)
    front_m.run_angle(300, 110)
    motor.turn(-30)

def eight():
    motor.straight(-8)
    motor.straight(200)
    motor.turn(90)
    motor.straight(110)
    arc(1, 90, 8)
    back_m.run_angle(300, -100)
    motor.straight(-120)
    motor.turn(-90)
    motor.straight(-100)

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
start([[one1, one2], [two], [three], [four1, four2, four3, four4, front], [five, five1],[six], [seven], [eight, f], [s], [nine1, nine2], [power_down]])
