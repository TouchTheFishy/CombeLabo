import Adafruit_BBIO.PWM as PWM
import time

#
class Servo():
    """
    Library used to control a servo going from -90° to 90° controlled with PWM
    """
    def __init__(self,pin):
        """
        When started, the library puts the servo at -90°
        """
        self.__pin=pin
        PWM.start(self.__pin, 0) #PWM set at 0% so the servo goes to -90° (50% = 0° and 100%= 90°)
        PWM.stop(self.__pin)#Close the PWM connection
        PWM.cleanup()



    def SetAngle(self,input):
        """
        Recieve an input from 0 to 100 and sets the position following this input
        """

        PWM.set_duty_cycle(self.__pin, input)
        PWM.stop(self.__pin)
        PWM.cleanup()

    def SwipeFromAngle(self,angle):
        """
        starts at a given angle and goes all the way to 90° at 1° per sec
        """

        i=angle
        while i<100:
            PWM.set_duty_cycle(self.__pin, angle)
            time.sleep(1)
            i+=1
        PWM.stop(self.__pin)
        PWM.cleanup()
		
if __name__ == '__main__':
    import time

    servo = Servo("P19_14")

    while(1):
        servo.SetAngle(50)
        time.sleep(5)
        servo.SwipeFromAngle(30)
