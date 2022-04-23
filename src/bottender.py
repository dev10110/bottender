import os
import uuid
import random

dummy_mode = False
if os.environ.get("DUMMY_MODE") == "TRUE":
    print("SETTING DUMMY MODE TRUE")
    dummy_mode=True
    
if not dummy_mode:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
import time


from motor_controller_pca9685 import MotorController
from drinks_controller import DrinksController

class BotTender:

    def __init__(self):

        dispense_per_five_sec = [
            0.71,
            0.63,
            0.64,
            0.63,
            0.786,
            0.787,
            0.80,
            0.817,
            0.6, 
            0.565, 
            0.58,
            0.655
        ]

        ## TEMPORARY!
        # dispense_per_five_sec = [s*10 for s in dispense_per_five_sec]
        
        self.POUR_CONSTS = [5000 / s for s in dispense_per_five_sec];
        
        # if not dummy_mode:
        #     GPIO.setmode(GPIO.BCM)

        # self.switch = 17
        # if not dummy_mode:
        #     GPIO.setup(self.switch, GPIO.IN)

        self.messages = []
        
        # self.motors = [ # define each motor here
        #     MotorController(21, 20), #M1 
        #     MotorController(16, 12), #M2
        #     MotorController(26, 19), #M3
        #     MotorController(11, 13), #M4
        #     MotorController(23, 18), #M5 
        #     MotorController(24, 25), #M6
        #     MotorController(22, 27), #M7
        #     MotorController(10, 9) #M8
        # ]
        self.motors = [MotorController(i) for i in range(12)]

        self.drinksController = DrinksController()    

        self.drink_queue = []
        self.drink_history_uuid = []
        self.drink_history_name = []


    def generate_uuid(self):
        
        return uuid.uuid4().hex

    
    def random_drink_id(self):
        menu = self.drinksController.get_menu()
        choice = random.choice(menu)
        print("THE CHOICE IS ", choice)
        return choice

    def enque(self, drink_id, uuid):

        if uuid in self.drink_history_uuid:
            print("WARN: drink uuid was already enqueued before. SKIPPING. ")
            return

        # NEW DRINK, so append to drink queue and history
        self.drink_queue.append((drink_id, uuid))
        self.drink_history_name.append(drink_id)
        self.drink_history_uuid.append(uuid)

    """ 
    remove first element from the drink queue
    """
    def deque(self, uuid):
        if len(self.drink_queue) >= 0:
            self.drink_queue.pop(0)

        return


    def get_next_drink_name(self):
        if len(self.drink_queue) >= 1:

            return self.find_drink(self.drink_queue[0][0]).name
        return "[Nothing Queued]"

    def get_next_drink_uuid(self):
        if len(self.drink_queue) >= 1:
            return self.drink_queue[0][1]
        else:
            return None


    def check_switch(self):
        if dummy_mode:
            return True
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

    def pour_parallel_next(self):
        if len(self.drink_queue) >= 1:
            drink_id, uuid_id = self.drink_queue.pop(0) # also removes it from the list
            self.pour_parallel(drink_id)


    def pour_parallel(self, drink_id):
        d = self.find_drink(drink_id)
        poured = ""
        
        plan = []
        for ing in d.ingredients.keys():
            if self.is_available(ing):
                mot = self.which_motor(ing)
                oz = d.ingredients[ing]
                t = self.POUR_CONSTS[mot] * oz
                plan.append([mot, t, False])
                poured = poured + ing + " "
        
        maxT = max([p[1] for p in plan])

        print(plan)

        start = time.time()
        # start the motors
        for m in [p[0] for p in plan]:
            self.motors[m].forward()
            print(f"Starting motor {m}")
        
        done = False
        while not done:
            t = (time.time() - start)*1000
            for i in range(len(plan)):
                if not plan[i][2]: # if not done
                    if t > plan[i][1]: # now is done
                        self.motors[plan[i][0]].stop()
                        print(f"*******************Stopping motor {plan[i][0]}")
                        plan[i][2] = True
            done = all([p[2] for p in plan])
            # time.sleep(0.05)
            print(t)

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

        # if not self.check_switch():
        #     print("SWITCH IS LOW")
        #     return False

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

        if motor == -1:
            for motor in self.motors:
                motor.forward()
            return

        if not self.validate(motor):
            return
        self.motors[motor].forward()


    def reverse(self, motor):

        if motor == -1:
            for motor in self.motors:
                motor.reverse()
            return

        if not self.validate(motor):
            return
        self.motors[motor].reverse()

    def stop(self, motor):

        if motor == -1:
            for motor in self.motors:
                motor.stop()
            return


        if not self.validate(motor):
            return
        self.motors[motor].stop()
    
    def __del__(self):
        for motor in self.motors:
            motor.stop()
        GPIO.cleanup()
        
