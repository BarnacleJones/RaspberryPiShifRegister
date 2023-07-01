import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21
BLINK_SPEED = 0.2
GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def setOutput(ledpattern):
	GPIO.output(PIN_LATCH, 0)
	for x in range(8):
		GPIO.output(PIN_DATA, int(ledpattern[x-1]))
		GPIO.output(PIN_CLOCK, 1)
		GPIO.output(PIN_CLOCK, 0)
	GPIO.output(PIN_LATCH, 1)
	
for i in range(10):
	setOutput("01010101")
	time.sleep(BLINK_SPEED)
	setOutput("10101010")
	time.sleep(BLINK_SPEED)
	setOutput("10001000")
	time.sleep(BLINK_SPEED)
	setOutput("01000100")
	time.sleep(BLINK_SPEED)
	setOutput("00100010")
	time.sleep(BLINK_SPEED)
	setOutput("00010001")
	time.sleep(BLINK_SPEED)
	setOutput("10000001")
	time.sleep(BLINK_SPEED)
	setOutput("01000010")
	time.sleep(BLINK_SPEED)
	setOutput("00100100")
	time.sleep(BLINK_SPEED)
	setOutput("00011000")
	time.sleep(BLINK_SPEED)
	setOutput("10000001")
	time.sleep(BLINK_SPEED)
	setOutput("11000011")
	time.sleep(BLINK_SPEED)
	setOutput("11111111")
	time.sleep(BLINK_SPEED + BLINK_SPEED)

setOutput("00000000")
