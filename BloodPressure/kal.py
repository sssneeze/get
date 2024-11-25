import numpy as np
import matplotlib.pyplot as plt

f = open('kal.txt').readlines()
data = []
for line in f:
    s = line.split()
    data.append([float(s[0]), float(s[1])])
data = np.array(data)
x = data[:, 0]
y = data[:, 1]


def apx(I, U):
    IU = np.mean(I * U)
    I_sred = np.mean(I)
    U_sred = np.mean(U)
    I_sq_sred = np.mean(I * I)
    U_sq_sred = np.mean(U * U)
    k = (IU - I_sred * U_sred) / (I_sq_sred - I_sred ** 2)
    b = U_sred - k * I_sred
    sigma_k = len(I) ** (-0.5) * ((U_sq_sred - U_sred ** 2) / (I_sq_sred - I_sred ** 2) - k ** 2) ** (0.5)
    sigma_b = sigma_k * (I_sq_sred - I_sred ** 2) ** 0.5
    return k, b, sigma_b, sigma_k


k, b, sigma_b, sigma_k = apx(y, x)

# plt.xlim(0, 0.45)
# plt.ylim(0, 0.04)
plt.xlabel('Отчеты АЦП')
plt.ylabel('Давление [Па]')

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

plt.scatter(x, y, label='Измерения', linewidths=1, marker='*', color='blue')
plt.plot(x, y, label='P = 9.66 * N + 129.42 [Па]', linewidth=0.8, color='red')

# p1 = np.polyfit(x, y, 1)
# m1 = np.poly1d(p1)
# print(m1)
# plt.plot(x, m1(x), color='red') #сема посоветовал

print(f'Значение k = {k} ' + '\n' + f'Значение b = {b} ')
print(f'Погрешность k = {sigma_k} ' + '\n' + f'Погрешность b = {sigma_b} ')
plt.title('Калибровочный график зависимости показаний АЦП от давления')
plt.legend()
plt.savefig('kal.png')
plt.show()
