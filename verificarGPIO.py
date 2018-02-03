import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

if(GPIO.input(17)):
	print 'Led Encendido'
else:
	print 'Led Apagado'
