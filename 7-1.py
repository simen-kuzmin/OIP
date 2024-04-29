import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [7, 3, 4 ,17, 27, 22, 10, 9]
comp = 14 
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(17, GPIO.IN)

def BIN(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    l = 0
    for i in range(7, -1, -1):
        l += 2**i
        GPIO.output(dac, BIN(l))
        time.sleep(0.005)
        if GPIO.input(comp) == 1:
            l -= 2**i
    return l

try:
    c = 0
    while c == 0:
        lis = [] 
        start = time.time()
        GPIO.output(troyka, GPIO.HIGH)
        v = 0
        volt = int(v) / 256 * 3.3
        while volt <= 2.4:
            v = adc()
            volt = int(v) / 256 * 3.3
            lis.append(v)
            print(volt)
        print(lis)
        GPIO.setup(troyka, GPIO.OUT, initial = 0)
        end = time.time()
        ex = end - start
        with open ("data.txt", "w") as f:
            f.writelines(f"{item}\n" for item in lis)
        with open ("setting.txt", "w") as g:
            g.write(str(len(lis)/ex))
            g.write("\n")
            g.write(str(3.3/256))
        t = [i for i in range(len(lis))]
        plt.plot(t, lis)
        plt.show()
        c = 1
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()