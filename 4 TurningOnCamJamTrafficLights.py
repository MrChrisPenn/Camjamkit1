#hacked together version to be triggered from Minecraft by @ChrisPenn84

#import minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

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

mc = minecraft.Minecraft.create()
woolId = 46

def Light_Sequence():
    mc.postToChat("Cam Jam Edukit 1 Minecraft / Breadboard Traffic Lights :)")
    time.sleep(1)
    mc.postToChat("red on")
    red.on()
    time.sleep(4)
    red.off()
    mc.postToChat("red off")
    time.sleep(0.5)
    mc.postToChat("yellow on")
    yellow.on()
    time.sleep(4)
    mc.postToChat("yellow off")
    yellow.off()
    time.sleep(0.5)
    mc.postToChat("Green on")
    green.on()
    time.sleep(4)
    mc.postToChat("Green off")
    green.off()
    time.sleep(1)
    mc.postToChat(("LEDs off")

evs = mc.events.pollBlockHits()
    for e in evs:
        pos = e.pos


        b = mc.getBlock(pos.x,pos.y,pos.z)
        if b == 46:
            Light_Sequence()
