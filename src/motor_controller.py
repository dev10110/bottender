
import RPi.GPIO as GPIO
import time

STOP = 0
FORWARD = 1
REVERSE = -1



class MotorController:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)

        GPIO.output(pinA, GPIO.LOW)
        GPIO.output(pinB, GPIO.LOW)

        self.start_timer = time.time()
        self.calibration = None
        
        self.stop()

    def stop(self):
        self.state = STOP
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)

    def forward(self):
        self.state = FORWARD
        GPIO.output(self.pinA, GPIO.HIGH)
        GPIO.output(self.pinB, GPIO.LOW)

    def reverse(self):
        self.state = REVERSE
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)      


    def dispense(self, ms):
        self.forward()
        time.sleep(ms*0.001)
        self.stop()

    def get_state(self):
        return self.state