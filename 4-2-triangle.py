import RPi.GPIO as GPIO
import time

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
    a = input()
    c = float (input())
    while True:
        if a.isdigit() == False:
            print("Enter value!\n")
            continue
        a = int (a)
        if a < 0:
            print("Enter positive value!")
            continue
        if str (a) == "q":
            break
        break
    b = 0
    j = 0
    while j < 256:
        for i in range (8): GPIO.output(dac[i], decimal2binary(b)[i])
        time.sleep (c/512)
        b += a
        j = j + 1
    b = 255
    j = 255
    while j > 0:
        for i in range (8): GPIO.output(dac[i], decimal2binary(b)[i])
        time.sleep (c/512)
        b -= a
        j = j - 1
finally:
    for i in range (8): GPIO.output(dac[i], 0)
    GPIO.cleanup()