from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 15

# open preview window
camera.start_preview()

#for i in range(100):
#    camera.annotate_text = "Brightness: %s" % i
#    camera.brightness = i
#    sleep(0.1)
#camera.brightness = 50

camera.annotate_text = "Hello world!"

# sleep for at least 2 seconds before capturing,
# to give the sensor time to set its light levels.
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')

camera.start_recording('/home/pi/video.h264')

# record video for 10 secs
sleep(10)

camera.stop_recording()
camera.stop_preview()

