#script to change shift register state on button press
from tkinter import BUTT
from gpiozero import Button
from time import sleep
from ShiftRegister import ShiftRegister

def main(): 
	#globals
	shift_register = ShiftRegister(data_pin=16, latch_pin=20, clock_pin=21)
	button = Button(12)
	button_flag = False

	def button_pressed_event():
		global button_flag
		if button_flag:
			shift_register.write("11111111")
		else:
			shift_register.clear()
		button_flag = not button_flag

	button.when_pressed = button_pressed_event
	pass

main()



