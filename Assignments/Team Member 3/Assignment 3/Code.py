led blink program

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.FALSE) 

while True: 
 GPIO.output(7, GPIO.TRUE) 
 sleep(5) # Sleep for 5 second
 GPIO.output(8, GPIO.FALSE) 
 sleep(5) # Sleep for 5 second


#traffic light program


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT, initial=GPIO.FALSE) 
GPIO.setup(11, GPIO.OUT, initial=GPIO.FALSE)
GPIO.setup(13, GPIO.OUT, initial=GPIO.FALSE)
while True: 

#turn red light

 GPIO.output(8, GPIO.TRUE) 
 sleep(5) 
 GPIO.output(8, GPIO.FALSE) 
 sleep(5) 

#turn yellow light

 GPIO.output(10, GPIO.TRUE) 
 sleep(5)
 GPIO.output(10, GPIO.FALSE) 
 sleep(5) 

#turn green light

 GPIO.output(12, GPIO.TRUE)
 sleep(5) 
 GPIO.output(12, GPIO.FALSE) 
 sleep(5)
