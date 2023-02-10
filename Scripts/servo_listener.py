import RPi.GPIO as GPIO
import mysql.connector
from time import sleep
import config_functions as cf

def x_axis(angle):
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
    
def y_axis(angle):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)

    pwm = GPIO.PWM(13,50)
    pwm.start(0)
    duty = angle/18+2.5 # Change 2.5 if not accurate
    GPIO.output(13, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(13, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()

while True:
    curr_ax = cf.servo_x_y_get()
    x_axis_angle = curr_ax[0]
    # print(x_axis_angle)
    y_axis_angle = curr_ax[1]
    # print(y_axis_angle)
    x_axis(x_axis_angle)
    y_axis(y_axis_angle)
