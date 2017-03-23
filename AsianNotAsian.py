import Adafruit_BBIO.PWM as PWM
import time

class AsianNotAsian():
    def __init__(self,input):
        self.input=input
        PWM.start("P9_14", 0)


    def IsAsian(self):

        for i in range(0, 100):
            PWM.set_duty_cycle("P9_14", float(i))
            time.sleep(0.1)
        PWM.stop("P9_14")
        PWM.cleanup()


obj=AsianNotAsian(155)
obj.IsAsian()
print("ergezr")