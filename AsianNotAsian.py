import Adafruit_BBIO.PWM as PWM
import time

class AsianNotAsian():
    def __init__(self,input):
        self.input=input


    def IsAsian(self):
        PWM.start("P8_13", 0)
        PWM.set_duty_cycle("P8_13", 90)
        for i in range(0, 100):
            PWM.set_duty_cycle("P8_13", float(i))
            time.sleep(1)
        PWM.stop("P8_13")
        PWM.cleanup()

obj=AsianNotAsian(155)
obj.IsAsian()