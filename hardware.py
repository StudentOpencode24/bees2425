from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
# Create your objects here.
ev3 = EV3Brick()
# импорт библиотек

# Write your program here.
lmot = Motor(Port.B, gears=[28, 20])
rmot = Motor(Port.C, gears=[28, 20])
front_m = Motor(Port.A, gears=[12, 20])
back_m = Motor(Port.D, gears=[12, 20])
motor = DriveBase(lmot, rmot, 49.5, 119)
gyro = GyroSensor(Port.S3)
colorRight = ColorSensor(Port.S2)
colorLeft = ColorSensor(Port.S1)

# задаём порты 

turn_acceleration = 500
straight_acceleration = 600


motor.settings(straight_speed=1000, straight_acceleration=straight_acceleration, turn_rate=200, turn_acceleration=turn_acceleration)
# настройки моторов

def t(l = 50, r = 50, speed = 500):
    lmot.run_angle(speed, l, 0, wait=0)
    rmot.run_angle(speed, r, 0, wait=0)

def arc(speed, speed_trun, angle):
    motor.stop()
    motor.reset()
    motor.drive(-speed, speed_trun)
    while abs(motor.angle()) < angle:
       pass  
    motor.stop()
    

def turn_acc_change(ang, rate = 1000, acc = turn_acceleration):
    motor.stop()
    motor.settings(turn_rate=rate, turn_acceleration=acc)
    motor.turn(ang)
    motor.stop()
    motor.settings(turn_rate=1000, turn_acceleration = turn_acceleration)
    
# функция поворота 

def move_speed_change(distance, speed=1000, acc=straight_acceleration):
    motor.stop()
    motor.settings(straight_speed=speed, straight_acceleration=acc)
    motor.straight(distance)
    motor.stop()
    motor.settings(straight_speed=1400, straight_acceleration = straight_acceleration)

# функция проезда с задомаемой скоростью и возможностью плавного тормажения и ускорения 

def turn_by_giro(turn_distance, speed=100):
    gyro.reset_angle(0)
    motor.reset()
    motor.drive(0,speed)
    g = gyro()
    if g == turn_distance():
        motor.stop()

# функция поорота по гироскопу

def move_By_Giro(distance, speed=1000, kp=10, kd=2):
    gyro.reset_angle(0)
    motor.reset()
    last_error = 0
    time = 0.01
    while abs(motor.distance()) < abs(distance):
        e = -gyro.angle()
        # print(e)
        d = (e - last_error) / time
        value = e * kp + d * kd
        motor.drive(speed, value)
        wait(time * 1000)
    motor.stop()

def travel_and_lines(speed):
    while colorLeft.reflection() <= 7:
        motor.drive(speed)

def move_By_giro_F_S(speed, kd = 0.01, kp = 0.4):
    gyro.reset_angle(0)
    motor.reset()
    last_error = 0
    time = 0.01
    def valL():
        return colorLeft.reflection()
    def valR():
        return colorRight.reflection()
    l = valL()
    r = valR()
    while l < 45 or r < 50:
        e = -gyro.angle()
        d = (e - last_error) / time
        value = e * kp + d * kd
        motor.drive(speed, value)
        l = valL()
        r = valR()
        wait(time * 1000)
    motor.stop()
    print("Exit from move_By_giro_F_S on values ", l, r)

# функция езды по гироскопу
def move_By_ColorLeft(distance, speed = 200, kp = 0.5, kd = 0.1):
    motor.reset()
    last_e = 0
    time = 0.05
    normal = 35
    while abs(motor.distance()) < abs(distance):
        error = normal - colorLeft.reflection()
        d = (error - last_e) / time
        value = error * kp + d * kd
        motor.drive(speed, -value)
        last_e = error
        wait(time * 1000)
    motor.stop()
    
# езда по первому датчика цвета

def move_By_ColorRight(distance, speed = 200, kp = 0.5, kd = 0.1):
    motor.reset()
    last_e = 0
    time = 0.05
    normal = 35
    while abs(motor.distance()) < abs(distance):
        error = normal - colorRight.reflection()
        d = (error - last_e) / time
        value = error * kp + d * kd
        motor.drive(speed, value)
        last_e = error
        wait(time * 1000)
    motor.stop()

def f_l(speed = 100, turn_rate = 10):
    motor.reset()
    motor.drive(speed, turn_rate)
    while colorLeft.reflection() < 10:
        pass
    motor.stop()
        
def draw_digits(value): 
    global ev3
    ev3.screen.clear() 
    disp_offset =15
    sig_len = 40
    sig_width = 7
    dig_space = 20
    sig_space = 6
 
    def show_sigment(num, digit): 
        #     
        #  0 ——— 
        # 5 |   | 1
        #  3 ———
        # 4 |   | 2
        #  6 ———
        #  
        global ev3
        x_offset = 178 - (disp_offset + (sig_len + sig_width * 2) * (digit + 1) + dig_space * digit) 
        y_offset = 0 + disp_offset 
        if num == 0 or num == 3 or num == 6: 
            x1 = x_offset + sig_width 
            x2 = x_offset + sig_width + sig_len 
            y1 = (y_offset + (0 if num == 0 else 
                (sig_len + sig_width) if num == 6 else 
                ((sig_len + sig_width) * 2))) 
            y2 = (y_offset + sig_width + (0 if num == 0 else  
                (sig_len + sig_width) if num == 6 else 
                ((sig_len + sig_width) * 2) )) 
        elif num == 1 or num == 5: 
            x1 = x_offset + ((sig_len + sig_width) if num == 1 else 0 ) 
            x2 = x_offset + sig_width + ((sig_len + sig_width ) if num == 1 else 0 ) 
            y1 = y_offset + sig_width 
            y2 = y_offset + sig_width + sig_len 
        elif num == 2 or num == 4: 
            x1 = x_offset + ((sig_len + sig_width) if num == 2 else 0 ) 
            x2 = x_offset + sig_width + ((sig_len + sig_width) if num == 2 else 0) 
            y1 = y_offset + sig_width * 2 + sig_len 
            y2 = y_offset + sig_width * 2 + sig_len * 2 
        ev3.screen.draw_box(x1, y1, x2, y2, fill = True)
 
# 

    digits_sigments = { 
        0: [0, 1, 2, 3, 4, 5], 
        1: [1, 2], 
        2: [0, 1, 3, 4, 6], 
        3: [0, 1, 2, 3, 6], 
        4: [1, 2, 5, 6], 
        5: [0, 2, 3, 5, 6], 
        6: [0, 2, 3, 4, 5, 6], 
        7: [0, 1, 2], 
        8: [0, 1, 2, 3, 4, 5, 6], 
        9: [0, 1, 2, 3, 5, 6] 
    } 
 
#

    digs = [int(v) for v in str(abs(value))] 
    digs.reverse() 
    num = 0 
    for dig in digs: 
        for sigment in digits_sigments[dig]: 
            show_sigment(sigment, num) 
        num += 1 
 
# функция для прорисовки больших символов на смарт хаб
    
def start(races):
    click = 1
    podzaezd = 0
    draw_digits(click * 10 + podzaezd)
    while True:
        while not Button.CENTER in ev3.buttons.pressed():
            if Button.LEFT in ev3.buttons.pressed():
                ev3.screen.clear()
                podzaezd = 0
                click -= 1
                if click < 1:
                    click = len(races)
                draw_digits(click)
                draw_digits(click * 10 + podzaezd)
                while Button.LEFT in ev3.buttons.pressed():
                    pass
            if Button.RIGHT in ev3.buttons.pressed():
                ev3.screen.clear()
                podzaezd = 0
                click += 1
                if click > len(races):
                    click = 1
                draw_digits(click * 10 + podzaezd)
                while Button.RIGHT in ev3.buttons.pressed():
                    pass
            if Button.UP in ev3.buttons.pressed():
                ev3.screen.clear()
                podzaezd += 1
                if podzaezd > len(races[click - 1]) - 1:
                    podzaezd = 0
                draw_digits(click * 10 + podzaezd)
                while Button.UP in ev3.buttons.pressed():
                    pass
            if Button.DOWN in ev3.buttons.pressed():
                ev3.screen.clear()
                podzaezd -= 1
                if podzaezd < 0:
                    podzaezd = len(races[click - 1]) - 1
                draw_digits(click * 10 + podzaezd)
                while Button.DOWN in ev3.buttons.pressed():
                    pass
            wait(100)

        if Button.CENTER in ev3.buttons.pressed():
            races[click - 1][podzaezd]()
            click += 1
            podzaezd = 0
            draw_digits(click * 10 + podzaezd)

# функция для запуска с кнопок на смарт хабе 
