import sys
import time
import random
import datetime
import telepot
from picamera import PiCamera

def handle(msg):
	#bot.sendMessage(chat_id,'Bienvenido a Daniel Monitoreo Bot')
	chat_id=msg['chat']['id']
	command=msg['text']
	print 'Got command: %s' % command
	
	#bot.sendMessage(chat_id,'Bienvenido a Daniel Monitoreo Bot \n\n A continuacion las opciones\n\n /grettins: Saludo \n /time: Hora del Dispositivo')

	if command == '/saludo':
		bot.sendMessage(chat_id, "Hola Invitado")
	elif command == '/time':
		bot.sendMessage(chat_id,'La hora del dispositivo es '+(time.strftime("%H:%M:%S"))+' del '+ time.strftime("%d/%m/%y"))
	elif command == '/tpic':
		 camera=PiCamera()
		 camera.start_preview()
		 time.sleep(2)
		 camera.capture('/home/pi/Proyectos/TelegramBot/image.jpg')
		 camera.stop_preview()
		#bot.sendMessage(chat_id,'Menu:\n /grettings: saludo \n /time:hora de raspberry')
		 bot.sendChatAction(chat_id, 'upload_photo')
		 r = bot.sendPhoto(chat_id, open('/home/pi/Proyectos/TelegramBot/image.jpg', 'rb'))
		 examine(r, telepot.namedtuple.Message)	

bot = telepot.Bot('token')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)
