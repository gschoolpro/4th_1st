# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

Sw520dPin = 18


def print_message():
    print('プログラムが動いています')


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Sw520dPin, GPIO.IN)


def main():
    print_message()
    while True:
        if(GPIO.input(Sw520dPin) == 0):
            print('*  検知しました!  *\n')
            time.sleep(1)
        else:
            print('*  検知できません...  *\n')
            time.sleep(1)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    main()
