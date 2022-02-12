import time


STOP = 0
FORWARD = 1
REVERSE = -1

class MotorController:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        self.start_timer = time.time()
        self.calibration = None
        self.stop()

    def stop(self):
        self.state = STOP
        return

    def forward(self):
        self.state = FORWARD
        return

    def reverse(self):  
        self.state = REVERSE  
        return


    def dispense(self, ms):
        self.forward()
        time.sleep(ms*0.001)
        self.stop()

    def get_state(self):
        return self.state
