#led blink program

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(6, GPIO.HIGH) 
 sleep(10) # Sleep for 10 second
 GPIO.output(6, GPIO.LOW) 
 sleep(10) # Sleep for 10 second


#traffic light program


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
while True: 

#turn red light

 GPIO.output(9, GPIO.HIGH) 
 sleep(7) 
 GPIO.output(9, GPIO.LOW) 
 sleep(7) 

#turn yellow light

 GPIO.output(10, GPIO.HIGH) 
 sleep(7)
 GPIO.output(10, GPIO.LOW) 
 sleep(7) 

#turn green light

 GPIO.output(11, GPIO.HIGH)
 sleep(7) 
 GPIO.output(11, GPIO.LOW) 
 sleep(7)
