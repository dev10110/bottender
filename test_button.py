import RPi.GPIO as GPIO
from time import sleep


LEDPIN=4
BTNPIN=3

GPIO.setmode(GPIO.BCM)


GPIO.setup(BTNPIN, GPIO.IN)
GPIO.setup(LEDPIN, GPIO.OUT)


try:
    while True:

        if GPIO.input(BTNPIN) == GPIO.LOW:
            GPIO.output(LEDPIN, GPIO.HIGH)
        else:
            GPIO.output(LEDPIN, GPIO.LOW)        

except:
    pass
finally:
    GPIO.cleanup()


        
