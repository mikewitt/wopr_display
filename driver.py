"""
Code originally by 'aforsberg' on Printables, retrieved from:
https://www.printables.com/model/1167457-1u-rack-mount-wopr-leds-enclosure
Previously licensed under CC-BY-4.0

Modified by Mike Witt, 2025
"""

from machine import Pin, SPI
import max7219
import random
from time import sleep

MATRIX_LENGTH = 4

spi = SPI(0, sck=Pin(2), mosi=Pin(3))
cs = Pin(5, Pin.OUT)

print("Setup SPI")

display = max7219.Matrix8x8(spi, cs, MATRIX_LENGTH)
display.brightness(0)

while True:
    for y in range(8):
        for x in range(MATRIX_LENGTH * 8):
            flip = random.randint(0, 1)
            if flip == 0:
                flipp = random.randint(0, 1)
                if flipp == 0:
                    display.pixel(x, y, 1)
                else:
                    display.pixel(x, y, 0)
            else:
                pass
    display.show()
    timeflip = random.randint(0, 3)
    if timeflip == 0:
        sleep(1)
    elif timeflip == 1:
        sleep(1.5)
    elif timeflip == 2:
        sleep(2)
    else:
        sleep(0.5)
