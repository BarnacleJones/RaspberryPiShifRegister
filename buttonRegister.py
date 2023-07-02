#script to change shift register state on button press
from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep
import random
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
	
def button_held_event():
	while button.is_pressed:
		arr = []
		for x in range(8):
			pattern = str(random.randint(0,1))
			arr.append(pattern)
		combo = ''.join(arr)
		shift_register.write(combo)
		sleep(0.06)
	shift_register.write("00000000")

shift_register = ShiftRegister(data_pin=16, latch_pin=20, clock_pin=21)
#button.when_pressed = button_pressed_event
button.when_held = button_held_event
try:
	while True:
		sleep(0.1)

except KeyboardInterrupt:
	pass

finally:
	shift_register.clear()
	GPIO.cleanup()
