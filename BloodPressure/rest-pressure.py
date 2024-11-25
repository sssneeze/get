import numpy as np
import matplotlib.pyplot as plt

f = open('adc_before.txt').readlines()
y = []
x = []
x1 = [16.97, 20.71]
y1 = [76.3, 65.0]
for line in f:
    y.append((9.66 * int(line) + 129.42)/133.3)
length = len(y)
print(length)
step = 30 / length

for i in range(len(y)):
    if y[i] > 76.3:
        print(i)
        if y[i] < 65.0:
            break

f = 0
for i in range(length):
    x.append(f)
    f += step

plt.xlim(14,22)
plt.ylim(55, 100)
plt.xlabel('Время [С]')
plt.ylabel('Давление [мм рт. ст.]')

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
plt.scatter(x1, y1, linewidths=2, marker='*', color='red')
plt.plot(x, y, label='Давление', linewidth=0.4, color='blue')
plt.title('Артериальное давление до физической нагрузки')
plt.text(16.97, 77.0, 'Systole', fontsize=9)
plt.text(20.71, 66.0, 'Diastole', fontsize=9)
plt.legend()
plt.savefig('rest-pressure.png')
plt.plot()
plt.show()