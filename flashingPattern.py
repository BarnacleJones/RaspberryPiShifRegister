import time

from ShiftRegister import ShiftRegister

shift_register = ShiftRegister(data_pin=16, latch_pin=20, clock_pin=21)
	
pattern = ["01010101",
		   "10101010",
		   "10001000",
		   "01000100",
		   "00100010",
		   "00010001",
		   "10000001",
		   "01000010",
		   "00100100",
		   "00011000",
		   "10000001",
		   "11000011",
		   "11111111"]

for x in [pattern]:
	shift_register.write(x)
	time.sleep(0.5)

print("wowwee")
time.sleep(1)
shift_register.clear()