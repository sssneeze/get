import time
import RPi.GPIO as gpio

leds = [2, 3, 4, 17, 27, 22, 10, 9]

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)

for i in range (3):
    for j in leds:
        gpio.output(j, 1)
        time.sleep(0.2)
        gpio.output(j, 0)


gpio.output(leds, 0)
gpio.cleanup()
