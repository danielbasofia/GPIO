import sys
import datetime
import time
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print 'Got command: %s' % command
	if command == '/tonl':
		if(GPIO.input(17)==True):
			bot.sendMessage(chat_id,'Las Luces Ya Estan Encendidas')
		else:
			bot.sendMessage(chat_id,'Encendiendo las Luces...')
			GPIO.output(17,True)
			bot.sendMessage(chat_id, 'Luces Encendidas')
	elif command == '/tofl':
		if(GPIO.input(17) == True):
			bot.sendMessage(chat_id, 'Apagando Luces...')
			GPIO.output(17,False)
			bot.sendMessage(chat_id, 'Luces Apagadas')
		else:
			bot.sendMessage(chat_id, 'Las Luces Ya estan Apagadas')
	else:
		bot.sendMessage(chat_id, 'Opcion Invalida')

bot = telepot.Bot('token')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)
