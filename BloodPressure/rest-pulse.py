import numpy as np
import matplotlib.pyplot as plt

f = open('adc_before.txt').readlines()
y = []
x = []
y1 = []

for line in f:
    y.append((9.66 * int(line) + 129.42)/133.3)
length = len(y)
step = 30 / 75

f = 0
for i in range(0, length, length // 75):
    x.append(f)
    y1.append((y[i + 1] - y[i]) / step)
    f += step

# i1, i2 = 0, 0
# for i in range(len(x)):
#     if x[i] > 14:
#         i1 = i
#         break
# for i in range(len(x)):
#     if x[i] > 22:
#         i2 = i
#         break
# print(i1, i2)
# step = 16 / 10
# for i in range(i1, i2, (i2 - i1) // 16):
#     y1.append(y[i])
#     x1.append(x[i])
#
# for i in range(len(y1) - 1):
#     y1[i] = (y1[i + 1] - y1[i]) / step


plt.xlim(0, 30)
plt.xlabel('Время t')
plt.ylabel('Изменение давления от времени dP/dt')

plt.minorticks_on()
plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1,
         color='0.7')  # основные линии

plt.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=0.6,
         color='0.8')  # побочные линии

plt.plot(x, y1, linewidth=0.8, color='green')
plt.title('График зависимости изменения давления по времени от времени \n до физической активности')
plt.savefig('rest-pulse.png')
plt.plot()
plt.show()