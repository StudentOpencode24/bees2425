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

def one2():
    """первый заезд без типлицы
    """
    back_m.run_angle(200, 105)
    motor.straight(-270)
    back_m.run_angle(200, -105) #сбор плуга и скотча
    motor.straight(290) #возвращение в зону 

def one3():
    back_m.run_angle(200, 95) #запуск мотора для сбора ящиков
    front_m.run(-9999)
    move_speed_change(240, 400) #подъезд к теплице. Блок 1
    wait(200) # ожидание пока собирает ящики
    move_speed_change(-50, 200)
    move_speed_change(100, 400) #подъезд к теплице. Блок 2
    wait(200) # ожидание пока собирает ящики
    move_speed_change(-150,100)
    front_m.stop()
    motor.straight(-110)

def two():
    """заезд с пшеницей
    """
    motor.straight(-20)
    back_m.run_angle(100, -90,wait = 0)
    # поднятие лапы
    motor.straight(745)
    motor.turn(93)
    motor.straight(100)
    # подъезд к пшенице
    back_m.run_angle(1000, 82)
    # сбор ящика
    motor.straight(-10)
    motor.turn(-97)
    motor.straight(-900)
    # возвращение в зону
    
def three():
    """выполнение яблони с забором контейнера 
    """
    motor.straight(-30)
    motor.straight(280)
    # выезд из зоны
    motor.turn(-65)
    motor.straight(95)
    motor.turn(-30)
    move_speed_change(400, 280)
    # подъезд к яблокам
    motor.straight(-100)
    move_speed_change(400, 1000)
    # 
    wait(1000)
    motor.straight(-130)
    motor.turn(90)
    motor.straight(-270)
    # возвращение в зону

def four1():
    """переезд в красную зону, с картошкой, зернохранилищем и комбайном
    """
    front_m.run_angle(800, -7, wait=0)
    motor.straight(-10)
    motor.straight(355)
    turn_acc_change(87, rate=1000)
    # подъезд к зернохранилищу
    motor.straight(273)
    motor.straight(-140)
    motor.turn(-103)
    motor.straight(620)
    motor.turn(102)
    # сброс инновационного проекта
    front_m.run_angle(800, 50, wait=0)
    move_speed_change(-550, 400)
    # подъезд к картофелю
    motor.straight(60)
    motor.straight(-150)
    move_speed_change(129, 400)
    # подъезд к комбайну
    back_m.run_angle(800, -1560)
    back_m.run_angle(1000, 1760, wait=0)
    wait(500)
    motor.straight(73) 
    motor.turn(-87)
    # поворот к зоне
    motor.straight(1100)


def four2():
    """экстреный переезд
    """
    motor.straight(350)
    move_By_Color1(450, 500)
    motor.turn(-45)
    motor.straight(600)
    move_By_Color2(400, 300)
    motor.straight(200)

def front():
    """заезд в зону для тренировки красной зоны 
    """
    motor.straight(800)

def five():
    """выполняет виноградник и забирает трактор в синию зону
    """
    motor.straight(30)
    front_m.run_angle(1000, -3200, wait= 0)
    back_m.run_angle(1000, -600,  wait= 0)
    # опускание лапы и выдвежение шторок
    motor.straight(-690)
    motor.straight(150)
    motor.turn(90)
    wait(1500)
    motor.straight(170)
    # подъезд к трактору
    front_m.run_angle(3500, 1600)
    back_m.run_angle(1000, 600, wait=0)
    motor.turn(20)
    motor.straight(-160)
    front_m.run_angle(4000, 1000, wait=0)
    motor.turn(80)
    motor.straight(-800)
    # заезд в красную зону

    

# def six():
#     # front_m.run_angle(1000, -4000)
#     motor.straight(-8)
#     front_m.run_angle(500, 70, wait=0)
#     motor.straight(190)
#     motor.turn(90)
#     motor.straight(130)
#     front_m.run_angle(500, -85) # сбор рамки скотча
#     motor.turn(-30)
#     motor.straight(-220)

def seven():
    """задвижение подставки руллоника
    """
    motor.straight(-28)
    motor.straight(220)
    front_m.run_angle(240, 180)
    wait(500)
    move_By_Giro(600, -420, 25)
    # повторное задвижение по гироскопу
    wait(100)
    motor.straight(20)
    front_m.run_angle(240, -200)

def eight():
    """завоз руллоника
    """
    motor.straight(300)
    wait(3000)
    motor.straight(-600)
    motor.straight(300)


def nine1():
    """последний заезд с иновационном проектом
    """
    motor.straight(-40)
    motor.straight(1300)
    motor.turn(50)
    motor.straight(360)
    motor.turn(51)
    motor.straight(280) #контейнеры в овощебазу


def f():
    """завоз обарудования на поле
    """
    motor.straight(300)
    motor.straight(-300)

def power_down():
    while True:
        move_speed_change(1000, 1000, 1000)
    

# start([one, two, three, four, five, six, seven, f, eight])
start([[one1, one2, one3], [two], [three], [four1, front], [five], [seven], [eight], [nine1], [power_down]])
