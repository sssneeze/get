import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

comp = 24
troyka = 13

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def binary(n):
    s = ''
    while n > 0:
        s = s + str(n % 2)
        n = n // 2
    res = [0] * 8
    for i in range(len(s)):
        res[7-i] = int(s[i])
    return res


try:
    while True:
        n = 0
        for i in range(8):
            n += 2 ** (7 - i)
            b = binary(n)
            GPIO.output(dac, b)
            time.sleep(0.01)
            # print(b, GPIO.input(comp))
            if GPIO.input(comp) > 0:
                n -= 2 ** (7 - i)
        result = (3.3 / 256) * n
        print("Число: ", n, " -> ", b,  "Напряжение: ", result)     

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()