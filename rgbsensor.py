class RGBSensor():
    """docstring for RGBSensor."""

    def __init__(self, int_pin):
        self.adress = 0x29
        self.int_pin = int_pin

        with open("/dev/i2c-2", "rb+") as i2c:
            i2c.write(self.adress << 1 | 1)
            i2c.write(0x00)
            i2c.write(0b00000011)

    def get_color():
        with open("/dev/i2c-2", "rb+") as i2c:
            i2c.write(bytes(self.adress << 1) + bytes(0x14))
            data = i2c.read(8)
            print(data)
