import os
from fcntl import ioctl

class Accelerometer():
    """
    Class abstracting the MMA7455L Accelerometer
    providing methods to retrieve the x, y and z acceleration components
    """

    def __init__(self):
        """initiates the communication on the I2C bus with the accelerometer"""
        self.adress = 0x1D
        self.i2c = os.open("/dev/i2c-2", os.O_RDWR)
        ioctl(self.i2c, 0x703, self.adress)

    def get_x(self):
        """get the x component of the acceleration"""
        os.write(self.i2c, bytes([0x00]))
        data = os.read(self.i2c, 2)
        return data[0] & (data[1] << 8)

    def get_y(self):
        """get the y component of the acceleration"""
        os.write(self.i2c, bytes([0x02]))
        data = os.read(self.i2c, 2)
        return data[0] & (data[1] << 8)

    def get_z(self):
        """get the z component of the acceleration"""
        os.write(self.i2c, bytes([0x04]))
        data = os.read(self.i2c, 2)
        return data[0] & (data[1] << 8)

# Test
if __name__ == '__main__':
    a = Accelerometer()
    print(a.get_x())
