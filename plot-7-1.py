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
        


plt.scatter(y1, x1)
plt.show()