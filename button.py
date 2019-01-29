from gpiozero import Button
from gpiozero import LED
from time import sleep
from signal import pause
from gpiozero import Buzzer

button = Button(2)
led = LED(4)
buzzer = Buzzer(17)

button.when_pressed = led.on
button.when_released = led.off

while True:
	buzzer.beep()
