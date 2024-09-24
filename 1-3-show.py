import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

if GPIO.input(21) == GPIO.HIGH:
    GPIO.output(20, 1)
else:
    GPIO.output(20, 0)