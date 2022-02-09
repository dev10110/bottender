import time


class MotorController:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        self.start_timer = time.time()
        self.calibration = None

    def stop(self):
        return

    def forward(self):
        return

    def reverse(self):    
        return


    def dispense(self, ms):
        self.forward()
        time.sleep(ms*0.001)
        self.stop()
