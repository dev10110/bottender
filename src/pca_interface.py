import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
import time

pca.frequency = 60

for i in range(12):
    # start = time.time()
    print(i)
    pca.channels[i].duty_cycle = 0xffff
    time.sleep(2)
    pca.channels[i].duty_cycle = 0
    time.sleep(1)
    