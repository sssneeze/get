import matplotlib.pyplot as plt
import numpy as np

f = open('nums.txt').readlines()
x = []
for line in f:
    x.append(int(line))

f1 = open('data.txt').readlines()
delta = float(f1[1])

n = 0
y = []
while n < 19.2:
    y.append(n)
    n += delta
# x = np.array(x)
# y = np.array(y)

x1 = []
y1 = []
for i in range(len(x)):
    if x[i] != 1:
        x1.append(x[i])
        y1.append(y[i])

for i in range(len(x1)):
    x1[i] = 0.013 * x1[i]

plt.minorticks_on()
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')

plt.xlim(0, 19.4)
plt.ylim(0, 3.0)

plt.grid(
    visible=True,
    which='major',
    linestyle='-',
    linewidth=1,
    color='0.7') #основные линии

plt.grid(
    visible=True,
    which='minor',
    linestyle='--',
    linewidth=0.6,
    color='0.8') #побочные линии

plt.text(7, 1, 'время зарядки 12.24 с', fontsize=9)
plt.text(7, 0.8, 'время разрядки 7.02 с', fontsize=9)

plt.title(label='Процесс заряда и разряда конденсатора в RC-цепочке')

plt.scatter(y1, x1,
            s=3,
            label='U(t)',
            linewidths=0.1,
            color='green')

plt.legend(fontsize=14)
plt.savefig('test.svg')
plt.show()