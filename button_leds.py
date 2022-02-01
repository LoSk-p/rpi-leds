import RPi.GPIO as GPIO
import time
import board
import neopixel

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
pixels = neopixel.NeoPixel(board.D18, 30)

leds_green = False
while True:
    if not GPIO.input(4):
        print("Button is pressed")
        if leds_green:
            pixels.fill((255, 0, 0))
            leds_green = False
        else:
            pixels.fill((0, 255, 0))
            leds_green = True
        time.sleep(2)
