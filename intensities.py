import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler


def luma(photoName):
    photo = imageio.imread(photoName)
    #background = photo[350:550, 600:745, 0:3].swapaxes(0, 1)

    cut = photo[300:570, 590:750, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    print(luma)
    # plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))
    #
    # fig = plt.figure(figsize=(10, 5), dpi=200)

    #plt.plot(rgb, label=['r', 'g', 'b'])
    # plt.plot(luma, 'w', label='I')
    # plt.legend()

    #plt.imshow(background, origin='lower')

    #plt.savefig(plotName)

    return luma

x = []
for i in range(385, 655):
    x.append(i)

luma_w = luma('photo_white.png')
luma_y = luma('photo_yellow.png')
luma_r = luma('photo_red.png')
luma_g = luma('photo_green.png')
luma_b = luma('photo_blue.png')

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
plt.gca().set_facecolor('grey')

plt.title('Отраженная интенсивность\n' + 'излучения лампы накаливания')
plt.xlabel('Длина волны, нм')
plt.ylabel('Яркость')

plt.plot(x, luma_w, 'w', label='Белый лист', color='white')
plt.plot(x, luma_y, 'w', label='Желтый лист', color='yellow')
plt.plot(x, luma_r, 'w', label='Красный лист', color='red')
plt.plot(x, luma_g, 'w', label='Зеленый лист', color='green')
plt.plot(x, luma_b, 'w', label='Синий лист', color='blue')

plt.legend()
plt.savefig('intensities.png')
plt.show()