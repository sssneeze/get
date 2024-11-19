import bloodFunctions as b
import time
import matplotlib.pyplot as plt


try:
    b.initSpiAdc()

    measure_time = 30.0

    data = []
    start = time.time()

    print("Measurements have been started. Wait for", measure_time, "seconds...")
    while time.time() - start < measure_time:
        data.append(b.getAdc())

    finish = time.time()
    print("Measurements have been finished.")

    file = open("/home/b03-405/Desktop/Liza/adc_before.txt", mode="w")
    for i in range(len(data)):
        s = str(data[i]) + "\n"
        file.write(s)
    file.close() 

    plt.plot(data)
    plt.show()

finally:
    b.deinitSpiAdc()