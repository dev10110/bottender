import RPi.GPIO as GPIO



class Motor:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)

        GPIO.output(pinA, GPIO.LOW)
        GPIO.output(pinB, GPIO.LOW)

    def stop(self):

        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)

    def forward(self):
        GPIO.output(self.pinA, GPIO.HIGH)
        GPIO.output(self.pinB, GPIO.LOW)

    def reverse(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)      


class BotTender:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        self.motors = [
            Motor(23, 24) # define each motor here
        ]    
 
    def forward(self, motor):
        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return
        self.motors[motor].forward()


    def reverse(self, motor):
        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return
        self.motors[motor].reverse()


    def stop(self, motor):
        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return
        self.motors[motor].stop()
    
    def __del__(self):
        for motor in self.motors:
            motor.stop()
        GPIO.cleanup()
        
