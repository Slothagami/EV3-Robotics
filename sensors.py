from pybricks.iodevices  import Ev3devSensor
from pybricks.parameters import Port

compass = Ev3devSensor(Port.S4)

def compass_read(): return compass.read("DC")[0]