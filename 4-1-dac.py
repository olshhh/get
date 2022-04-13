import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

for i in range (8): GPIO.setup(dac[i], GPIO.OUT)

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def binary2decimal (a):
    val = 0
    for i in range (8): val += a[7 - i] * pow (2, i)
    return val

try:
    while True:
        a = input()
        if (a.isdigit() == False):
            print("Enter value!\n")
            continue
        a = int (a)
        if a < 0:
            print("Enter positive value!")
            continue
        if str (a) == "q":
            break
        a = decimal2binary(a)
        for i in range (8): GPIO.output(dac[i], a[i])
        print (binary2decimal(a)/ 256 * 3.3)
finally:
    for i in range (8): GPIO.output(dac[i], 0)
    GPIO.cleanup()