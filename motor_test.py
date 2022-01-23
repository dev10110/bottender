import RPi.GPIO as GPIO
from time import sleep

in1 = 23
in2 = 24

try:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

    sleep(5)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

    sleep(5)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

except:
    pass
finally:
    GPIO.cleanup()
