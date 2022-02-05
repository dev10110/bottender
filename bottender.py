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

    def pour(self, drink_id):
        d = self.find_drink(drink_id)
        poured = ""

        for ing in d.ingredients.keys():
            print(" ** checking " + ing)
            if self.is_available(ing):
                mot = self.which_motor(ing)
                print(" ** "+ ing + " is at motor " + str(mot) + ". Dispensing")
                duration_ms= 1000
                self.dispense(mot, duration_ms)
                print(" ** Done dispensing")
                poured = poured + ing + " "
            else:
                print(" ** " + ing + " is NOT available")
        return poured
    
    def is_available(self, ing):
        return ing in self.drinksController.drinks

    def which_motor(self, ing):
        return self.drinksController.drinks.index(ing)



    def find_drink(self, drink_id):
        for d in self.all_drinks():
            if d.id == drink_id:
                return d

    
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
        
