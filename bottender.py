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
        
