# RaspberryPiShifRegister
The place I store my scripts for interfacing with a 74HC595 shift register


I have written a class for code reusability, ShiftRegister.py


<code>
from ShiftRegister import ShiftRegister
shift_register = ShiftRegister(data_pin=PIN#1, latch_pin=PIN#2, clock_pin=PIN#3)
</code>

