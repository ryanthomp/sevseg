#!/usr/bin/python

import RPi.GPIO as GPIO
one = 14
two = 15
three = 18
four = 2
five = 3
six = 4
seven = 23
eight = 24
nine = 17
ten = 27
eleven = 22
twelve = 25
pinlist = (one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for z in pinlist:
    GPIO.setup(z, GPIO.OUT)
    GPIO.output(z, GPIO.LOW)


class Main:
    def __init__(self):
        pass

    def write(self, digit):
        pass

    def num(self, number, x):
        pass


class SevSeg(Main):
    def num(self, number, x):
        place = {1: twelve, 2: nine, 3: eight, 4: six}
        numbers = {1: (four, seven), 2: (eleven, seven, five, one, two), 3: (eleven, seven, five, four, two),
                   4: (ten, five, seven, four), 5: (eleven, ten, five, four, two),
                   6: (eleven, ten, five, one, two, four), 7: (eleven, seven, four),
                   8: (eleven, ten, five, seven, one, two, four), 9: (eleven, ten, five, seven, four)}
        place = place[x]
        print(place)
        num = int(number)
        pins = numbers[num]
        print(pins)
        GPIO.output(place, GPIO.HIGH)
        GPIO.output((pins), GPIO.HIGH)

    def write(self, digit):
        dig = str(digit)
        dig = list(dig)
        print(dig)
        x = 0
        for i in dig:
            x += 1
            SevSeg.num(SevSeg(), i, x)
