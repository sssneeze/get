import matplotlib.pyplot as plt

f = open('adc_after.txt').readlines()
y = []
x = []
x1 = [6.34, 9.44]
y1 = [73.9, 51.8]
for line in f:
    y.append((9.66 * int(line) + 129.42)/133.3)
length = len(y)

step = 30 / length

f = 0
for i in range(length):
    x.append(f)
    f += step

plt.xlim(5,13)
plt.ylim(40, 80)
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
plt.plot(x, y, label='Давление', linewidth=0.5, color='blue')
plt.title('Артериальное давление после физической нагрузки')
plt.text(6.34, 73.9, 'Systole', fontsize=9)
plt.text(9.44, 51.8, 'Diastole', fontsize=9)
plt.legend()
plt.savefig('workout-pressure.png')
plt.plot()
plt.show()