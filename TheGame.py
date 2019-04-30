from gpiozero import LED, Button
import time 
from time import sleep
from random import uniform
import sys 

led = LED(4)
right_button = Button(15)
left_button = Button(14)
#assigning the hardware to the respective GPIO pins

while True:
    led.on()
    if(right_button.is_pressed or left_button.is_pressed):
        led.off()
        sys.exit("You pressed too early") #ends the game
        
    sleep(uniform(2, 5))
    led.off() #tuns the LED off after anywhere between 2-5 seconds
    break

float start = time.time() #starts the timer

while True:
    if right_button.is_pressed: 
        float elapsed = time.time() - start #calculates reaction time
        print("Right player wins, your reaction time was " + elapsed + " seconds")
        break
    else if left_button.is_pressed:
                float elapsed = time.time() - start #calculates reaction time
        print("Left player wins, your reaction time was " + elapsed + " seconds")
        break
