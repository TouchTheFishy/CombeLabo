import os
from enum import Enum

class Direction(Enum):
    """docstring for ."""
    IN = 0
    OUT = 1


class GPIO:
    """
    Abstraction around GPIO pins of the Beagle Bone Black.
    """

    def __init__(self, port, pin, direction):
        """
        Chose a pin between 1 and 46
        Chose a port, the port 9 is 1 and the port 8 is 2.
        """
        self.pin = 32 * port + pin
        self.direction = "out" if direction == Direction.OUT else "in"
        self.value = 0

        # Check if the pin is already exported
        if not os.path.exists("/sys/class/gpio/export"):
            # Write the values to the appropriate files
            __write_gpio("/sys/class/gpio/export", str(self.pin))
            __write_gpio("/sys/class/gpio/direction", self.direction)
            __write_gpio("/sys/class/gpio/value", str(self.value))
            __write_gpio("/sys/class/gpio/unexport", str(self.pin))

    def set(self, value):
        if not os.path.exists("/sys/class/gpio/export"):
            __write_gpio("/sys/class/gpio/export", str(self.pin))
            __write_gpio("/sys/class/gpio/value", str(self.value))
            __write_gpio("/sys/class/gpio/unexport", str(self.pin))

    # Internal function to make code DRY
    def __write_gpio(path, value):
        with open(path, "w") as f:
            f.write(value)


if __name__ == '__main__':
    import time

    led = GPIO(1, 48, Direction.OUT)

    while(1):
        led.set(1)
        time.sleep(1)
        led.set(0)
        time.sleep(1)
