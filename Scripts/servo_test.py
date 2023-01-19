import RPi.GPIO as GPIO
from time import sleep

def angle(angle):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    pwm = GPIO.PWM(7,50)
    pwm.start(0)
    duty = angle/18+2.5 # Change 2.5 if not accurate
    GPIO.output(7, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(7, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()

while True:
    inp = input('Degrees: ')
    angle(int(inp))
    