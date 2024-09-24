import RPi.GPIO as GPIO

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
        print(s[i])
    return res
    

try:
    while True:
        n = input("Введите число от 0 до 255: ")
        if n == 'q':
            break
        n = int(n) 
        b = binary(n)
        GPIO.output(dac, b)
        result = (3.3 / 256) * n
        print("Предполагаемое напряжение: ", result)
 

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
