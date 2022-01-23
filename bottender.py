import RPi.GPIO as GPIO
from motor_controller import MotorController
from drinks_controller import DrinksController

class BotTender:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        self.motors = [
            MotorController(23, 24) # define each motor here
        ]

        self.drinksController = DrinksController()    


    def set_drinks(self, drinks):
        self.drinksController.set_drinks(drinks)


        
    def validate(self, motor)
        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return False
        return True

    def calibrate_start(self, motor):
        if not self.validate(motor):
            return

        self.motors[motor].calibrate_start()

    def calibrate_end(self.motor):
        if not self.validate(motor):
            return
        self.motors[motor].calibrate_end()


    def dispense(self, motor, ms):
        if not self.validate(motor):
            return
        self.motors[motor].dispense(ms)
 
    def forward(self, motor):
        if not self.validate(motor):
            return
        self.motors[motor].forward()


    def reverse(self, motor):
        if not self.validate(motor):
            return
        self.motors[motor].reverse()

    def stop(self, motor):
        if not self.validate(motor):
            return
        self.motors[motor].stop()
    
    def __del__(self):
        for motor in self.motors:
            motor.stop()
        GPIO.cleanup()
        
