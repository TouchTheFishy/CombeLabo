import os
from fcntl import ioctl

# Sensor does not work, code doesn't either ;)

class RGBSensor():
    """docstring for RGBSensor."""

    def __init__(self, int_pin):
        self.adress = 0x29
        self.int_pin = int_pin

        self.i2c = os.open("/dev/i2c-2", os.O_RDWR)
        ioctl(self.i2c, 0x703, self.adress)

    def get_color(self):
        data = os.read(self.i2c, 8)
        print(data)
