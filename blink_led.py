#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
# loop through 50 times, on/off for 1 second
for i in range(5):
    GPIO.output(4,True)
    time.sleep(1)
    GPIO.output(4,False)
    time.sleep(1)
GPIO.cleanup()
