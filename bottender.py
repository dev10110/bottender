import RPi.GPIO as GPIO

GPIO.setwarnings(False)

from motor_controller import MotorController
from drinks_controller import DrinksController

class BotTender:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        self.motors = [
            MotorController(14, 15), # define each motor here
            MotorController(23, 24),
            MotorController(25, 8),
            MotorController(7, 1)
        ]

        self.drinksController = DrinksController()    
    
    def all_drinks(self):
        return self.drinksController.menu

    def set_drinks(self, drinks):
        self.drinksController.set_drinks(drinks)

    def get_loaded_drink(self, motor_ind):
        return self.drinksController.drinks[motor_ind]
    
    def all_ingredients(self):
        return self.drinksController.get_all_ingredients()
 
    def num_motors(self):
        return len(self.motors)
        
    def validate(self, motor):
        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return False
        return True

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
        
