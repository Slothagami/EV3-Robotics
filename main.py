#!/usr/bin/env pybricks-micropython
from movement import *
from sensors  import *
from random   import randrange
from pybricks.hubs  import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

class State:
    @staticmethod
    def test():
        # movefor(randrange(360), 1)
        ev3.screen.clear()
        ev3.screen.draw_text(10, 10, compass_read())
        wait(0.1)

while True: State.test()