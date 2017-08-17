import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
try:
    while 1:
            GPIO.output(40, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(40, GPIO.LOW)
            time.sleep(0.1)
except:
    print("Either keypress, or something else happened")
    GPIO.output(40, GPIO.LOW)
GPIO.cleanup()
