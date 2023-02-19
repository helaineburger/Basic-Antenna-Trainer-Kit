####################
## Import Modules ##
####################

import RPi.GPIO as GPIO
import mysql.connector
from time import sleep
import config_functions as cf

#####################################################
## Listen For Servo Axis Data Inputs From Database ##
#####################################################

def theta_axis(angle):
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
    
def phi_axis(angle):
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
    curr_ax = cf.servo_theta_phi_get() # get current axis data from database
    theta_axis_angle = curr_ax[0]
    # print(theta_axis_angle)
    phi_axis_angle = curr_ax[1] 
    # print(phi_axis_angle)
    theta_axis(theta_axis_angle) # set servo theta angle to value from database
    phi_axis(phi_axis_angle) # set servo phi angle to value from database
