# Import libs
import time
from machine import*
import utime


time.sleep(0.1)
print("Hello, Raspberry Pi Pico W!")


# Déclaration d'une broche en sortie, à l'aide du constructeur Pin()
# Setting an output pin, using the Pin() constructor
led = Pin(3, Pin.OUT)


# Allumer la LED
# Turn on the LED
led.on()
utime.sleep(2)
led.off()

while True:
  led.off()
  utime.sleep(1)
  led.on()
  utime.sleep(1)
