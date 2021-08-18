#!/usr/bin/env pybricks-micropython
from movement import *
from sensors  import *
from random   import randrange
from pybricks.hubs  import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()
pCompass = 0

class State:
    @staticmethod
    def test():
        compass = compassRead()#updateSensors()

        ev3.screen.clear()
        ev3.screen.draw_text(10, 10, compassSensor.read("AC"))
        
        movefor(compass, 1.5)
        wait(2)

while True: State.test()