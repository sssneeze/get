import matplotlib.pyplot as plt
import numpy as np
import csv

x = []

with open ("deltas.txt", "r") as delta:
    tmp = [float(i) for i in delta.read().split("\n")]

data_array = np.loadtxt("test.txt", dtype = int)

k = len(data_array)
mx = max(data_array)
ind = 0

for i in range(k):
  if data_array[i] == mx:
    ind = i
    break

time_zar = ind * tmp[0]
time_zar = round(time_zar, 2)
time_raz = k*tmp[0] - time_zar
time_raz = round(time_raz, 2)

data_array = data_array * (3.3/256)

for i in range(k):
  x.append(i * tmp[0])

fig, ax = plt.subplots(figsize=(6, 4), dpi = 200)
ax.plot(x, data_array, color='pink', marker='o', markersize = 3, label='V(t)', markevery = 20)
plt.legend(fontsize=14)
plt.xlabel('Время, c') 
plt.ylabel('Напряжение, В') 
#plt.title('Процесс заряда и разряда конденсатора в RC-цепи') 

plt.minorticks_on()

ax.grid(which = 'major', color='0.7', linestyle='-', linewidth=0.5)
ax.grid(which = 'minor', color='0.8', linestyle='--', linewidth=0.3)

plt.xlim(0, 5)
plt.ylim(0, 3)

# s1_template="Время заряда = {ind} с"
# ind1 = str(time_zar)
# s1 = s1_template.format(ind=ind1)

# s2_template="Время разряда = {ind} с"
# ind2 = str(time_raz)
# s2 = s2_template.format(ind=ind2)

# plt.text(8, 1, s1, fontsize = 6)
# plt.text(8, 0.5, s2, fontsize = 6)

fig.savefig("vika_sasha.svg")
plt.show()

