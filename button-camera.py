import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime as dt

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)

def my_callback(channel):
    now = str(dt.datetime.timestamp(dt.datetime.now()))
    fname = '/home/pi/image-'+now+'.jpg'
    camera.capture(fname)
    print('file {} saved'.format(fname))

GPIO.add_event_detect(4, GPIO.FALLING, callback=my_callback, bouncetime=300)
try:
    while(True):
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup() # clean up GPIO on CTRL+C exit
    exit(1)

GPIO.cleanup() # clean up GPIO on normal exit
