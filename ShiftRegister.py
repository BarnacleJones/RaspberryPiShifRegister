#class to take care of initialising/defining/writing to the 74HC595 shift register
#TODO: Expand functionality and __init__ function for GPIO input

import  RPi.GPIO as GPIO
class ShiftRegister(object):
    def __init__(self, data_pin: int, latch_pin: int, clock_pin: int):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(data_pin, GPIO.OUT)
        GPIO.setup(latch_pin, GPIO.OUT)
        GPIO.setup(clock_pin, GPIO.OUT)
    
    """Writes data_string to the register"""
    def write(self, data_string: str):
        if len(data_string) != 8:
            raise ValueError("data_string must be 8 characters of 1's or 0's")
        GPIO.output(self.latch_pin, 0)
        for x in range(8):
            GPIO.output(self.data_pin, int(data_string[x-1]))
            GPIO.output(self.clock_pin, 1)
            GPIO.output(self.clock_pin, 0)
        GPIO.output(self.latch_pin, 1)

    """Turns off each pin and runs cleanup on GPIO"""
    def clear(self) -> None:
        self.write("00000000")
        GPIO.cleanup()
        




