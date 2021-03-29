#This code sets the default stand up mode for the Raspclaws

import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

while(1):
#Front Left Leg
   #Rotate leg
   pwm.set_pwm(0, 0, 350)
   time.sleep(0.1)
   #Stand up or down
   pwm.set_pwm(1, 0, 350)
   time.sleep(0.1)

#Center Left Leg
   #Rotate leg
   pwm.set_pwm(2, 0, 350)
   time.sleep(0.1)
   #Stand up or down (0 is all the way up, 500 is all the way down)
   pwm.set_pwm(3, 0, 350)
   time.sleep(0.1)

#Back Left Leg
   #Rotate leg (0 is all the way left, 500 is all the way right)
   pwm.set_pwm(4, 0, 250)
   time.sleep(0.1)
   #Stand up or down
   pwm.set_pwm(5, 0, 350)
   time.sleep(0.1)

#Back Right Leg
   #Rotate leg (500 is all the way left, 0 is all the way right)
   pwm.set_pwm(6, 0, 350)
   time.sleep(0.1)
   #Stand up or down
   pwm.set_pwm(7, 0, 300)
   time.sleep(0.1)

#Center Right Leg
   #Rotate leg (500 is all the way left, 0 is all the way right)
   pwm.set_pwm(8, 0, 300)
   time.sleep(0.1)
   pwm.set_pwm(9, 0, 300) #This one is acting strange
   time.sleep(0.1)
   #Stand up or down

#Front Right Leg
   #Rotate leg (500 is all the way left, 0 is all the way right)
   pwm.set_pwm(10, 0, 200)
   time.sleep(0.1)
   #Stand up or down
   pwm.set_pwm(11, 0, 300)
   time.sleep(0.1)
   #time.sleep(1)


