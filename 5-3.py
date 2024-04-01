import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14 
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def BIN(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    l = 0
    for i in range(7, -1, -1):
        l += 2**i
        GPIO.output(dac, BIN(l))
        time.sleep(0.05)
        if GPIO.input(comp) == 1:
            l -= 2**i
              
    return l
def led(s):
    for i in range(1, 9):
            if 2**i > s:
                g = [0]*(8-i//2)+[1]*(i//2)
                GPIO.output(leds, g)
                break
            if s == 255:
                g = [1, 1, 1, 1, 1, 1, 1, 1]
                GPIO.output(leds, g)
                break
try:
    while True:
        s = adc()
        k = led(s)
        print(s)
        v = int(s) / 256 * 3.3
        compval = GPIO.input(comp)
        if s != 0:
            print(s, "{:.2f}". format(v))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    
