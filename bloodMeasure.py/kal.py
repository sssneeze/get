import matplotlib.pyplot as plt

f = open('kal.txt').readlines()

x = []
y = []

for line in f:
    s = line.split()
    x.append(int(s[0]))
    y.append(int(s[1]))

plt.xlim(0, 1500)
plt.ylim(0, 145)
plt.plot(x, y)
plt.savefig('kal.png')
plt.show()