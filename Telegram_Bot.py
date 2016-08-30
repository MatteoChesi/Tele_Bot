import telepot
import json
import time
import emoji

import Plugin.Menu as M
import Plugin.Func as F


class YourBot(telepot.Bot):
	def __init__(self, *args, **kwargs):
		super(YourBot, self).__init__(*args, **kwargs)
		
		self.utenti = dict(Prova=dict(
			chat_id=159940058,
			
			MenuPrincipale = 1,
			MenuMeteo = 0,
			MenuLCD = 0,
			MenuUtenti = 0,
			MenuTorrent = 0,
			MenuUpload = 0,
			MenuDownload = 0,

			RicezioneFile = 0,

			grado_U = 2, #Admin

			Citta = '',
			GPS = ''
			))
		
		self.utente = dict
		

	def on_chat_message(self, msg):
		
		content_type, chat_type, chat_id = telepot.glance(msg)
		user = str(msg['from']['first_name']) + '_' + str(msg['from']['last_name'])

		LOG_file = open("LOG.txt","a")

		print (time.strftime("%d/%m/%Y %H:%M:%S",time.gmtime(msg['date'])) + '[' + content_type + '] ' + msg['from']['first_name'] + ' ' +msg['from']['last_name']+ ' ' + str(chat_id) + ' -->'),
		LOG_file.write(time.strftime("%d/%m/%Y %H:%M:%S",time.gmtime(msg['date'])) + '[' + content_type + '] ' + msg['from']['first_name'] + ' ' +msg['from']['last_name'] + ' ' + str(chat_id)  + ' --> ')



		if str(user) not in self.utenti:
			
			self.utenti[str(user)] = dict(
				chat_id = chat_id ,
			
				MenuPrincipale = 1,
				MenuMeteo = 0,
				MenuLCD = 0,
				MenuUtenti = 0,
				MenuTorrent = 0,
				MenuUpload = 0,
				MenuDownload = 0,

				RicezioneFile = 0,

				grado_U = 1, #User

				Citta = '',
				GPS = ''
				) 

		self.utente = self.utenti[str(user)]

		

		
		
		if (content_type == 'text'):
			print (msg['text'])
			LOG_file.write(str(emoji.demojize(msg['text'])).decode("utf-8") + '\r\n')
			LOG_file.close()
			print str(emoji.demojize(msg['text'])).decode("utf-8")
			M.Menu(self.utente,str(emoji.demojize(msg['text'])),bot,js)

		if (self.utente['RicezioneFile'] == 1):
			if (content_type == 'photo'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.jpg'))
					LOG_file.write(str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.jpg') + '\r\n')
					LOG_file.close()
					F.scarica_foto(msg,bot)           

			elif (content_type == 'document'):
				if self.utente['MenuUpload'] == 1:
					print (msg['document']['file_name'])
					LOG_file.write(msg['document']['file_name'] + '\r\n')
					LOG_file.close()
					F.scarica_file(msg,bot)
					
			elif (content_type == 'location'):
				if self.utente['MenuUpload'] == 1:
					print ('GPS')
					LOG_file.write('GPS' + '\r\n')
					LOG_file.close()
					F.salva_GPS(msg,bot)
				elif self.utente['MenuMeteo'] == 2:
					print ('GPS')
					LOG_file.write('GPS' + '\r\n')
					LOG_file.close()
					self.utente['GPS'] = str(msg['location']['latitude']) + ',' + str(msg['location']['longitude'])
					M.Menu(self.utente,'/citta',bot,js)

					
			elif (content_type == 'video'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.mp4'))
					LOG_file.write(str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.mp4') + '\r\n')
					LOG_file.close()
					F.scarica_video(msg,bot)
					
			elif (content_type == 'voice'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.ogg'))
					LOG_file.write(str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.ogg') + '\r\n')
					LOG_file.close()
					F.scarica_voice(msg,bot)
			
			elif (content_type == 'audio'):
				if self.utente['MenuUpload'] == 1:
					print (msg['audio']['title']+' - '+msg['audio']['performer']+'.mp3')
					LOG_file.write(msg['audio']['title']+' - '+msg['audio']['performer']+'.mp3'+ '\r\n')
					LOG_file.close()
					F.scarica_audio(msg,bot)
					
			elif (content_type == 'contact'):
				if self.utente['MenuUpload'] == 1:
					print (msg['contact']['first_name'])
					LOG_file.write(msg['contact']['first_name'] + '\r\n')
					LOG_file.close()
					F.scarica_contact(msg,bot)
				
			


File_Config = 'CONFIG'


f = open(File_Config , 'r')
js = json.loads(f.read())
f.close()

TOKEN = str(js['KEY Telegram'])
Key_METEO = str(js['Meteo']['KEY'])
Admin = str(js['Admin'])

bot = YourBot(TOKEN)
bot.message_loop()

bot.sendMessage(Admin, 'Raspberry avviato... ')
while 1:
	time.sleep(10)
