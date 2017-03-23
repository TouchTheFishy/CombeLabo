import Adafruit_BBIO.PWM as PWM
import time

class AsianNotAsian():
    def __init__(self,input):
        self.input=input
        PWM.start("P9_14", 0)


    def IsAsian(self):


        time.sleep(3)
        PWM.set_duty_cycle("P9_14", 50)
        PWM.stop("P9_14")
        PWM.cleanup()


obj=AsianNotAsian(155)
obj.IsAsian()
print("ergezr")