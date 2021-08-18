# For Movement Logic Api's
from pybricks.ev3devices import Motor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools      import wait, StopWatch, DataLog
from math import *

motors = [Motor(Port.A), Motor(Port.B), Motor(Port.C)]

def spin(speed): # Speed in revs per second (Won't go faster than 3)
    for motor in motors: motor.run(speed * 360)

def stop():
    for motor in motors: motor.stop()

def spinfor(speed, seconds):
    spin(speed)
    wait(seconds * 1000)
    stop()

def move(angle):
    speed = 3
    angle = radians(angle)

    for motor, index in zip(motors, range(len(motors))):
       motorangle = radians( (index + 1) * 120 - 130)
       theta      = motorangle - angle
       motorspeed = speed * sin(theta) * 360 # 360 converts it to rps

       if motorspeed < 0.05: motorspeed /= 1.3 # ajust for the wierd friction

       motor.run(motorspeed)

def movefor(direction, seconds):
    move(direction)
    wait(seconds * 1000)
    stop()