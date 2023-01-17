import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

pwm = GPIO.PWM(16,50)
pwm.start(0)

def angle(angle):
    duty = angle/18+2.5 # Change 2.5 if not accurate
    GPIO.output(16, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(16, False)
    pwm.ChangeDutyCycle(0)

while True:
    inp = input('Degrees: ')
    angle(int(inp))
    pwm.stop()
    GPIO.cleanup()
