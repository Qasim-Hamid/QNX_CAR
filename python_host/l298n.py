import RPi.GPIO as gpio
import time

#Input 1 and Input 2 control spin direction of left motor
#Input 3 and Input 4 control spin direction of right motor

#    GND -> Pin 34
#Input 1 -> Pin 11 (GPIO 17)
#Input 2 -> Pin 15 (GPIO 22)
#Input 3 -> Pin 16 (GPIO 23)
#Input 4 -> Pin 18 (GPIO 24)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    return True

def forward(sec):
    if (init()):
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, True)
        gpio.output(24, False)
        time.sleep(sec)
        gpio.cleanup()

def reverse(sec):
    if (init()):
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, False)
        gpio.output(24, True)
        time.sleep(sec)
        gpio.cleanup()

def left_turn(sec):
    if (init()):
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, True)
        gpio.output(24, False)
        time.sleep(sec)
        gpio.cleanup()

def right_turn(sec):
    if (init()):
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, False)
        gpio.output(24, True)
        time.sleep(sec)
        gpio.cleanup()

def main():
    duration = 3
    time.sleep(duration)
    print("Forward")
    forward(duration)
    time.sleep(1)

    print("right")
    right_turn(duration)
    time.sleep(1)

    print("left")
    left_turn(duration)
    time.sleep(1)

    print("reverse")
    reverse(duration)
    time.sleep(1)

main()

