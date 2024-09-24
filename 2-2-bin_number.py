import RPi.GPIO as GPIO
import time
import random


GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [] * 8

GPIO.setup(dac, GPIO.OUT)
for k in range(8):
    number.append(random.randint(0, 1))

GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])

time.sleep(15)

GPIO.output(dac, 0)

GPIO.cleanup()
