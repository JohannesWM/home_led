# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import modeFunctions
import psutil


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

purple = (160, 32, 240)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):

            if modeFunctions.get_current_mode() != "toggleRainbow":
                pixels.fill((0, 0, 0))
                pixels.show()
            else:
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def Racer(color=purple):
    front = 0
    length = 0

    for i in range(num_pixels):
        if length < 50:
            length += 1
            pixels[i] = color
        elif length >= 50:
            front = i
            pixels[front - 49] = (0, 0, 0)
        else:
            print("error")
        pixels.show()
        time.sleep(0.01)




# Get the current process ID
pid = psutil.Process()


while True:

    # Get the memory information
    memory_info = pid.memory_info()

    # Access different memory attributes
    memory_usage = memory_info.rss  # Current resident set size in bytes
    memory_usage_mb = memory_usage / (1024 * 1024)  # Convert to megabytes

    print(f"Current memory usage: {memory_usage_mb:.2f} MB")

    if modeFunctions.get_current_mode() == "toggleOFF":
        pixels.fill((0, 0, 0))
        pixels.show()
    elif modeFunctions.get_current_mode() == "toggleRainbow":
        rainbow_cycle(0.01)  # rainbow cycle with 1ms delay per step
    elif modeFunctions.get_current_mode() == "toggleRacer":
        Racer(purple)
    elif modeFunctions.get_current_mode() == "toggleTimer60":
        print("toggleTimer60")
        time.sleep(1)
    elif modeFunctions.get_current_mode() == "toggleSpeedRacer":
        print("toggleSpeedRacer")
        time.sleep(1)
    else:
        print("ERROR")

