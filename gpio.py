import os

def Write(chemin, val1):
    with open(chemin, "w") as f:
        f.write(val1)

def GPIO(pin, port):
    """
    Chose a pin between 1 and 46
    Chose a port, the port 9 is 1 and the port 8 is 2.
    """

    # To check if the pin is already with an information
    if not os.path.exists("/sys/class/gpio/export"):
        #If not, we have to write in 4 register
        Write("/sys/class/gpio/export", str(32 * port + pin)) #To define wich pin
        Write("/sys/class/gpio/direction", "out")#To choose between IN/OUT
        Write("/sys/class/gpio/value", 1)#To active the pin
        Write("/sys/class/gpio/unexport", str(32 * port + pin))#To liberate the pin
