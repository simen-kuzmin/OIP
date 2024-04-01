import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def BIN(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        a = input()
        if a == "q":
            sys.exit()
        elif a.isdigit() and int(a)%1 == 0 and 0 <= int(a) <= len(dac) -1:
            GPIO.output(dac, BIN(int(a)))
        elif not a.isdigit() or int(a)%1 != 0 or int(a) < 0 or int(a) > 255:
            print("Error 0 - 255")
except ValueError:
    print("input 0 - 255")
except KeyboardInterrupt:
    print("...")

finally:
    print(BIN(0))
    GPIO.output(dac, 0)
    GPIO.cleanup()
    