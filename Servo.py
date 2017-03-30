import Adafruit_BBIO.PWM as PWM
import time

class Servo():
    def __init__(self,pin):
        self.__pin=pin
        PWM.start(self.__pin, 0)
        PWM.stop(self.__pin)
        PWM.cleanup()


    def SetAngle(self,input):

        PWM.set_duty_cycle(self.__pin, input)
        PWM.stop(self.__pin)
        PWM.cleanup()

    def SwipeFromAngle(self,angle):

        i=angle
        while i<100:
            PWM.set_duty_cycle(self.__pin, angle)
            time.sleep(1)
            i+=1
        PWM.stop(self.__pin)
        PWM.cleanup()