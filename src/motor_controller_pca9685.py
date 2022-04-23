import os

dummy_mode = False
if os.environ.get("DUMMY_MODE") == "TRUE":
    dummy_mode=True

if not dummy_mode:
    import board
    import busio
    import adafruit_pca9685
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c)
    pca.frequency = 60
import time

STOP = 0
FORWARD = 1
REVERSE = -1



class MotorController:

    def __init__(self, ch): 
        self.ch = ch
        self.start_timer = time.time()
        self.calibration = None
        
        self.stop()

    def stop(self):
        self.state = STOP
        if not dummy_mode:
            pca.channels[self.ch].duty_cycle = 0

    def forward(self):
        self.state = FORWARD
        if not dummy_mode:
            pca.channels[self.ch].duty_cycle = 0xffff

    def reverse(self):
        self.stop()
        # self.state = REVERSE
        # if not dummy_mode:
        #     pca.channels[self.ch].duty_cycle = 0    


    def dispense(self, ms):
        self.forward()
        time.sleep(ms*0.001)
        self.stop()

    def get_state(self):
        return self.state