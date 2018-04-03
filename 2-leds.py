 # CamJam EduKit 1 - Basics
# Worksheet 2 - LEDs

# Import Libraries
import time  # A collection of time related commands
from gpiozero import LED  # The LED functions from GPIO Zero
from gpiozero import Button
# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
#green = LED(24)
Switch = Button(3)


    
while True:
    Switch.wait_for_press()
    print("red on")
    red.on()
    time.sleep(4)
    red.off()
    print("red off")
    time.sleep(0.5)
    print("yellow on")
    yellow.on()
    time.sleep(4)
    print("yellow off")
    yellow.off()
    time.sleep(0.5)
#green.on()



#print("LEDs off")

#time.sleep(4)
#green.off()
