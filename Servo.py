import Adafruit_BBIO.PWM as PWM
import time
"""
Library used to control a servo going from -90° to 90° controlled with PWM
"""

class Servo():
    """
    When started, the library puts the servo at -90°
    """
    def __init__(self,pin):
        self.__pin=pin
        PWM.start(self.__pin, 0) #PWM set at 0% so the servo goes to -90° (50% = 0° and 100%= 90°)
        PWM.stop(self.__pin)#Close the PWM connection
        PWM.cleanup()

    """
    When started, the library puts the servo at -90°
    """
    def SetAngle(self,input):

        PWM.set_duty_cycle(self.__pin, input)
        PWM.stop(self.__pin)
        PWM.cleanup()

	"""
	starts at a given angle and goes all the way to 90° at 1° per sec
	"""
    def SwipeFromAngle(self,angle):

        i=angle
        while i<100:
            PWM.set_duty_cycle(self.__pin, angle)
            time.sleep(1)
            i+=1
        PWM.stop(self.__pin)
        PWM.cleanup()