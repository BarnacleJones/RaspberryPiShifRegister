#script to turn off the shift register outputs
from ShiftRegister import ShiftRegister

shift_register = ShiftRegister(data_pin=16, latch_pin=20, clock_pin=21)

shift_register.clear();

