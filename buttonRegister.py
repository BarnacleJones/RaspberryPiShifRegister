#script to change shift register state on button press
from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep
from ShiftRegister import ShiftRegister
GPIO.setmode(GPIO.BCM)
	#globals
button = Button(12)
button_flag = False

def button_pressed_event():
	global button_flag
	if button_flag:
		shift_register.write("11111111")
	else:
		shift_register.clear()
	button_flag = not button_flag

shift_register = ShiftRegister(data_pin=16, latch_pin=20, clock_pin=21)
button.when_pressed = button_pressed_event
try:
	while True:
		sleep(0.1)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
