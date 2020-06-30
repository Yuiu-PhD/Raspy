import time
import RPi.GPIO as GPIO

# Pin definitions (No. 6th outside)
led_pin = 12

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Blink forever
while True:
    # Turn LED on
    GPIO.output(led_pin, GPIO.HIGH)
    # Delay for 1 second
    time.sleep(1)
    # Turn LED off
    GPIO.output(led_pin, GPIO.LOW)
    # Delay for 1 second
    time.sleep(1)
