import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime as dt

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)

def my_callback(channel):
    now = str(dt.datetime.timestamp(dt.datetime.now()))
    fname = '/home/pi/image-'+now+'.jpg'
    i = 0

    while True:
        GPIO.output(18, 1)
        sleep(0.5)
        GPIO.output(18, 0)
        sleep(0.5)
        i += 1
        if i >= 2:
            break

    camera.capture(fname)
    print('file {} saved'.format(fname))

GPIO.add_event_detect(4, GPIO.FALLING, callback=my_callback, bouncetime=500)
try:
    while(True):
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup() # clean up GPIO on CTRL+C exit
    exit(1)

GPIO.cleanup() # clean up GPIO on normal exit
