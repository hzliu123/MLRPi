import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def my_callback(channel):
    print("falling edge detected on 4")

GPIO.add_event_detect(4, GPIO.FALLING, callback=my_callback, bouncetime=300)
try:
    while(True):
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup() # clean up GPIO on CTRL+C exit
    exit(1)

GPIO.cleanup() # clean up GPIO on normal exit
