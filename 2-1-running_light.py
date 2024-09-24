import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


# GPIO.setup(3, GPIO.OUT)
# GPIO.output(3, 0)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)

for k in range(3):
    for gpio in leds:
        GPIO.output(gpio, 1)
        time.sleep(0.2)
        GPIO.output(gpio, 0)

GPIO.output(leds, 0)

GPIO.cleanup()