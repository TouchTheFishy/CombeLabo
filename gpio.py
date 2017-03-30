def Write(chemin, val1):
    with open(chemin, "w") as f:
        f.write(val1)

def GPIO(pin, port):
    """
    Chose a pin between 1 and 46
    Chose a port, the port 9 is 1 and the port 8 is 2.
    """

    Write("sys/class/gpio/export", 32 * port + pin)
# On peut toujours tapper une exception s'il mets un autre port ou une autre pin et n'importe quoi d'autre

    Write("/sys/class/gpio/direction", "out")
    Write("/sys/class/gpio/value", 1)
    Write("/sys/class/gpio/unexport", 32 * port +pin)

