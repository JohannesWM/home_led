# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import modeFunctions


# PIXEL COLORS GBR format RBG

Black = (0, 0, 0)
colors = {"Black": (0, 0, 0), "Purple": (160, 240, 32)}
# END PIXEL COLORS

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
                pixels.fill(Black)
                pixels.show()
                break
            else:
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)

        if modeFunctions.get_current_mode() != "toggleRainbow":
            pixels.fill(Black)
            pixels.show()
            break
        pixels.show()
        time.sleep(wait)


def racer(length=10, color=colors["Purple"], delay_time=0.001):
    current_length = 0
    for led in range(num_pixels):

        if modeFunctions.get_current_mode() != "toggleRacer":
            break

        if current_length < length:
            current_length += 1
            pixels[led] = color

        elif led == 99:

            pixels[led] = color
            time.sleep(delay_time)

            for subled in range(current_length):
                pixels[led - current_length + subled] = colors["Black"]
                pixels.show()
                time.sleep(delay_time)

            pixels[99] = colors["Black"]
            pixels.show()

        elif current_length == length:
            pixels[led] = color
            pixels[led - current_length] = colors["Black"]

        pixels.show()
        time.sleep(delay_time)


def speed_racer(length=10, color=colors["Purple"], delay_time=0.01):
    current_length = 0
    for led in range(num_pixels):
        delay_time -= 0.0001

        if modeFunctions.get_current_mode() != "toggleSpeedRacer":
            break

        if current_length < length:
            current_length += 1
            pixels[led] = color

        elif led == 99:

            pixels[led] = color
            time.sleep(delay_time)

            for subled in range(current_length):
                pixels[led - current_length + subled] = colors["Black"]
                pixels.show()
                time.sleep(delay_time)

            pixels[99] = colors["Black"]
            pixels.show()

        elif current_length == length:
            pixels[led] = color
            pixels[led - current_length] = colors["Black"]

        pixels.show()
        time.sleep(delay_time)


def blink(color=colors["Purple"], exetus=False):

    pixels.fill(color)
    pixels.show()

    while not exetus:
        while pixels.brightness < 1 and (pixels.brightness + 0.1) <= 1:

            if modeFunctions.get_current_mode() != "toggleTimer60":
                exetus = True
                break

            pixels.brightness += 0.1
            pixels.fill(color)
            pixels.show()
            time.sleep(0.01)
        while pixels.brightness > 0 and (pixels.brightness - 0.1) >= 0:

            if modeFunctions.get_current_mode() != "toggleTimer60":
                exetus = True
                break

            pixels.brightness -= 0.1
            pixels.fill(color)
            pixels.show()
            time.sleep(0.01)


def hour_leds(color=colors["Purple"]):
    start_time = time.time() / 60 / 60
    exetus = False

    while time.time() / 60 / 60 - start_time < .01:

        if modeFunctions.get_current_mode() != "toggleTimer60":
            exetus = True
            break

        hour_diff = time.time() / 60 / 60 - start_time
        hour_diff_leds = (hour_diff * 100).__round__()

        if hour_diff_leds <= num_pixels:
            pixels[hour_diff_leds] = color
            pixels.show()
        else:
            break

    if exetus is False:
        blink(color=color, exetus=exetus)
    else:
        pass


def lights_server_link():
    while True:

        try:

            if pixels.brightness != 0.2:
                pixels.brightness = 0.2

            if modeFunctions.get_current_mode() == "toggleOFF":
                pixels.fill(colors["Black"])
                pixels.show()
            elif modeFunctions.get_current_mode() == "toggleRainbow":
                rainbow_cycle(.001)
            elif modeFunctions.get_current_mode() == "toggleRacer":
                racer()
            elif modeFunctions.get_current_mode() == "toggleTimer60":
                hour_leds()
            elif modeFunctions.get_current_mode() == "toggleSpeedRacer":
                speed_racer()
            else:
                print("ERROR")

        except KeyboardInterrupt:
            break
