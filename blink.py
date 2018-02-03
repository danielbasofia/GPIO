import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def blink():
	print 'Ejecucion iniciada'
	GPIO.output(17,True)	

blink()
