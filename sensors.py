from pybricks.iodevices  import Ev3devSensor
from pybricks.parameters import Port

compassSensor = Ev3devSensor(Port.S4)
compass = 0
prevCompass = 0

def compassRead(): return compassSensor.read("DC")[0]
def updateSensors():
    global prevCompass, compass
    compass    += compassRead() - prevCompass
    prevCompass = compassRead()

    # normalize to 0-9 converting other angles to equiv in range 0-9
    if compass < 0: compass = 9 + compass
    if compass > 9: compass = compass % 9

    # convert 0-9 to degrees
    compass *= 360 / 9
    compass += 0 # offset

    return 360 - compass