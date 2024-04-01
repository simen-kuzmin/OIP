import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14 
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN, initial = GPIO.HIGH)

def BIN(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc(v):
    s = BIN(v)
    GPIO.output(dac, s)
    return s
try:
    while True:
        for i in range(256):
            s = adc(i)
            v = i / 256 * 3.3
            compval = GPIO.input(comp)
            if compval == 1:
                print("adc value = {:^3} -> (), input voltage = {:.2f}". format(i, BIN(i), v))
except KeyboardInterrupt:
    print("keyboard")
else:
    print("no exeptions")

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    