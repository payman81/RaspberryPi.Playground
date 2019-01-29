import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
 
while True:
     if GPIO.input(17):
          GPIO.output(4, GPIO.HIGH)
     else:
          GPIO.output(4, GPIO.LOW)
 
GPIO.cleanup()
