import RPi.GPIO as GPIO

GPIO.setwarnings(False)

from motor_controller import MotorController
from drinks_controller import DrinksController

class BotTender:

    def __init__(self):

        dispense_per_five_sec = [
            0.71,
            0.81,
            0.72,
            0.78,
            0.60,
            0.62,
            0.63,
            0.58
        ]
        
        self.POUR_CONSTS = [5000 / s for s in dispense_per_five_sec];
        
        GPIO.setmode(GPIO.BCM)

        self.switch = 17
        GPIO.setup(17, GPIO.IN)

        self.messages = []
        
        self.motors = [ # define each motor here
            MotorController(21, 20), #M1 
            MotorController(16, 12), #M2
            MotorController(26, 19), #M3
            MotorController(11, 13), #M4
            MotorController(23, 18), #M5 
            MotorController(24, 25), #M6
            MotorController(22, 27), #M7
            MotorController(10, 9) #M8
        ]

        self.drinksController = DrinksController()    

        


    def check_switch(self):
        return GPIO.input(self.switch) == 1

    def pour(self, drink_id):
        d = self.find_drink(drink_id)
        poured = ""

        for ing in d.ingredients.keys():
            print(" ** checking " + ing)
            if self.is_available(ing):
                mot = self.which_motor(ing)
                print(" ** "+ ing + " is at motor " + str(mot) + ". Dispensing")
                self.dispense_oz(mot, d.ingredients[ing])
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
        return self.drinksController.get_menu()

    def set_drinks(self, drinks):
        return self.drinksController.set_drinks(drinks)

    def get_loaded_drink(self, motor_ind):
        return self.drinksController.drinks[motor_ind]
    
    def all_ingredients(self):
        return self.drinksController.get_all_ingredients()
 
    def num_motors(self):
        return len(self.motors)
        
    def validate(self, motor):

        if not self.check_switch():
            print("SWITCH IS LOW")
            return False

        if motor > len(self.motors)-1:
            print("WARNING: COMMANDING UNINITIALISED MOTOR")
            return False

        return True

    def dispense(self, motor, ms):
        if not self.validate(motor):
            return
        self.motors[motor].dispense(ms)

    def dispense_oz(self, motor, oz):
        if not self.validate(motor):
            return
        self.motors[motor].dispense(self.POUR_CONSTS[motor] * oz)
 
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
        
