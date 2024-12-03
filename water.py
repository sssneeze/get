import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
p = [0, 0, 0, 0, 0, 0, 0, 0]
numbers = []
deltas = []

button = 16
comp = 14
troyka = 13
N = 0

gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(leds, gpio.OUT)

def bin_list(n):
    a = []
    for i in range (8):
        a.append(n % 2)
        n //= 2
    return a[::-1]

def adc():
    l = 0
    r = 255
    while r - l > 1:
        m = (r + l) // 2
        gpio.output(dac, bin_list(m))
        time.sleep(0.005)
        n = gpio.input(comp)
        if n == 1:
            r = m
        else:
            l = m   
    return r

print(gpio.input(button))

try:
    #gpio.output(troyka, gpio.HIGH)
    while gpio.input(button) < 1:
        pass
    start = time.time()
    t = time.time()
    while (t - start) < 15:
        n = adc()
        result = n
        numbers.append(result)
        print(result)
        t = time.time()

  
finally:
    finish = time.time()
    delta_t = finish - start
    deltas.append(delta_t)

    plt.ylim(0, 256)
    plt.plot(numbers)
    plt.show()

    numbers_str = [str(item) for item in numbers]
    with open("exp_40.txt", "w") as outfile:
        outfile.write("\n".join(numbers_str)) 
    deltas_str = [str(item) for item in deltas]
    with open("deltasexp_40.txt", "w") as outfile:
        outfile.write("\n".join(deltas_str))
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()


