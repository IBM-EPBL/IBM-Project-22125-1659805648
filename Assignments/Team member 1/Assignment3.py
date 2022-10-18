#led blink program

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT, initial=GPIO.0) 

while True: 
 GPIO.output(5, GPIO.HIGH) 
 sleep(3) # Sleep for 3 second
 GPIO.output(7, GPIO.LOW) 
 sleep(3) # Sleep for 3 second


#traffic light program


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(5, GPIO.OUT, initial=GPIO.0) 
GPIO.setup(7, GPIO.OUT, initial=GPIO.0)
GPIO.setup(12, GPIO.OUT, initial=GPIO.0)
while True: 

#turn red light

 GPIO.output(8, GPIO.1) 
 sleep(3) 
 GPIO.output(8, GPIO.0) 
 sleep(3) 

#turn yellow light

 GPIO.output(10, GPIO.1) 
 sleep(3)
 GPIO.output(10, GPIO.0) 
 sleep(3) 

#turn green light

 GPIO.output(12, GPIO.1)
 sleep(3) 
 GPIO.output(12, GPIO.0) 
 sleep(3)
