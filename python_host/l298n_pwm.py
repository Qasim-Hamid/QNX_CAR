import RPi.GPIO as GPIO

input_1 = 17
input_2 = 27
enable_a = 4

GPIO.setmode(GPIO.BCM)

def init():
    GPIO.setup(input_1, GPIO.out)
    GPIO.setup(input_2, GPIO.out)
    GPIO.setup(enable_a, GPIO.out)

    power_a = GPIO.pwm(enable_a, 100)
    power_a.start(20)

    GPIO.output(input_1, GPIO.low)
    GPIO.output(input_2, GPIO.low)

def cw():
    init()
    GPIO.output(input_1, GPIO.high)
    GPIO.output(input_2, GPIO.low)
    GPIO.cleanup()

def ccw():
    init()
    GPIO.output(input_1, GPIO.low)
    GPIO.output(input_2, GPIO.high)
    GPIO.cleanup()
