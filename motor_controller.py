
import RPi.GPIO as GPIO
from time import sleep, now


class MotorController:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)

        GPIO.output(pinA, GPIO.LOW)
        GPIO.output(pinB, GPIO.LOW)

        self.start_timer = time.now()
        self.calibration = None

    def stop(self):

        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)

    def forward(self):
        GPIO.output(self.pinA, GPIO.HIGH)
        GPIO.output(self.pinB, GPIO.LOW)

    def reverse(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)      


    def dispense(self, ms):
        self.forward()
        time.sleep(ms*0.001)
        self.stop()

    def calibrate_start(self, ms):
        self.
