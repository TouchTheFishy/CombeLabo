import Adafruit_BBIO . PWM as PWM
import time

class AsianNotAsian():
    def __init__(self,input):
        self.input=input

    def IsAsian(self):
        PWM.start(" P9_14 ", 0)
        for i in range(0, 100):
            PWM.set_duty_cycle(" P9_14 ", float(i))
        time.sleep(1)
        PWM.stop(" P9_14 ")
        PWM.cleanup()

