import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def binary(n):
    s = ''
    while n > 0:
        s = s + str(n % 2)
        n = n // 2
    res = [0] * 8
    for i in range(len(s)):
        res[7-i] = int(s[i])
    return res


T = int(input("Введите период: "))
try:
    while True:
        n = 0
        GPIO.output(dac, 0)
        while n < 255:
            n += 1
            b = binary(n)
            GPIO.output(dac, b)
            print((3.3 / 256) * n)
            time.sleep(T / 510)
        while n > 0:
            n -= 1
            b = binary(n)
            GPIO.output(dac, b)
            print((3.3 / 256) * n)
            time.sleep(T / 510)



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()