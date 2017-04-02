import os

def GPIO(pin, port):
    """
    Chose a pin between 1 and 46
    Chose a port, the port 9 is 1 and the port 8 is 2.
    """

    # Internal function to make code DRY
    def write_gpio(path, value):
        with open(path, "w") as f:
            f.write(value)

    # To check if the pin is already with an information
    if not os.path.exists("/sys/class/gpio/export"):
        # If not, we have to write in 4 register
        write_gpio("/sys/class/gpio/export", str(32 * port + pin))#To define wich pin
        write_gpio("/sys/class/gpio/direction", "out")#To choose between IN/OUT
        write_gpio("/sys/class/gpio/value", 1)#To active the pin
        write_gpio("/sys/class/gpio/unexport", str(32 * port + pin))#To liberate the pin

