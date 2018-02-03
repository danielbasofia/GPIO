import sys
import time
import random
import datetime
import telepot

def handle(msg):
	#bot.sendMessage(chat_id,'Bienvenido a Daniel Monitoreo Bot')
	chat_id=msg['chat']['id']
	command=msg['text']
	print 'Got command: %s' % command
	
	#bot.sendMessage(chat_id,'Bienvenido a Daniel Monitoreo Bot \n\n A continuacion las opciones\n\n /grettins: Saludo \n /time: Hora del Dispositivo')

	if command == '/saludo':
		bot.sendMessage(chat_id, "Hola Invitado")
	elif command == '/time':
		bot.sendMessage(chat_id,'La hora del dispositivo es '+str(datetime.datetime.now()))
	elif command == '/tpic':
		#bot.sendMessage(chat_id,'Menu:\n /grettings: saludo \n /time:hora de raspberry')
		 bot.sendChatAction(chat_id, 'upload_photo')
		 r = bot.sendPhoto(chat_id, open('/home/pi/Pictures/pi-mathematical-value-135@1x.jpg', 'rb'))
		 bot.sendPhoto(chat_id,r)

def examine(result, type):
    try:
        print 'Examining %s ......' % type

        nt = type(**result)
        assert equivalent(result, nt), 'Not equivalent:::::::::::::::\n%s\n::::::::::::::::\n%s' % (result, nt)

        if type == telepot.namedtuple.Message:
            print 'Message glance: %s' % str(telepot.glance(result, long=True))

        pprint.pprint(result)
        pprint.pprint(nt)
        print
    except AssertionError:
        traceback.print_exc()
        answer = raw_input('Do you want to continue? [y] ')
        if answer != 'y':
            exit(1)


bot = telepot.Bot('token')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)
