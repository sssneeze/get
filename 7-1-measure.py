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


def adc(n):
    b = binary(n)
    GPIO.output(dac, b)

measured_nums = []

start = time.time()

try:
    while True:
        for num in range(256):
            adc(num)
            # print(b, GPIO.input(comp))

            if GPIO.input(comp) == 1:
                #result = (3.3 / 256) * num
                if num == 0:
                    break
                if num == 224:
                    GPIO.setup(troyka, GPIO.OUT, initial=0)
                else:
                    measured_nums.append(num)
                    print(num)
                    break


finally:
    final = time.time()
    measured_time = final - start
    delta_t = str(measured_time / len(measured_nums))
    with open("data.txt", "w") as outfile:
        outfile.write(delta_t)

    measured_nums_str = [str(item) for item in measured_nums]

    with open("nums.txt", "w") as outfile:
        outfile.write("\n".join(measured_nums_str))

    GPIO.output(dac, 0)
    GPIO.cleanup()
