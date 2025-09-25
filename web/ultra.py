#!/usr/bin/python3
# File name   : ultra.py
# Description : Detection distance and tracking with ultrasonic
# Author      : BLONWINER
# Date        : 2024/03/10

from gpiozero import DistanceSensor
from time import sleep


sensor = DistanceSensor(echo=8, trigger=11, max_distance=2) # Maximum detection distance 2m. 

def checkdist():
   return (sensor.distance) *100 # Unit: cm

if __name__ == "__main__":
   while True:
       distance = checkdist() 
       print("%.2f cm" %distance)
       sleep(0.05)
