# CombeLabo

### Blink led
The blinking led example is incorporated in the `gpio.py` file and runs when you launch it directly.
The LED has to be connected to physical pin 15 on the P9 header with a protection resistor of 330 Ohm in series and then to the GND pin of the BBB.

### Control of a Servo Motor
???

### Accelerometer
The accelerometer is connected through I2C (SCL + SDA), once the bus initialized we can read the x, y and z components.
