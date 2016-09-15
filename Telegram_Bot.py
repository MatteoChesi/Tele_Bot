import telepot
import json
import time
import emoji
import MySQLdb

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



		val = "'"+str(msg['message_id'])+"','"+str(msg['from']['id'])+"','"+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(msg['date'])))+"','"+str(content_type)+"'"

		conn = MySQLdb.connect (host = "localhost",user="root",passwd="matte95",db="Telegram_Bot")
		cursor = conn.cursor()

		if content_type == 'text':
			val = val + ",'"+str(emoji.demojize(msg['text'])).decode("utf-8")+"'"
			cursor.execute ("insert into Log value("+val+")")
		else:
			cursor.execute ("insert into Log (idMessaggio,idUser,Data,TipoContenuto) value("+val+")")

		cursor.close()
		conn.commit()
		conn.close()


		print (time.strftime("%d/%m/%Y %H:%M:%S",time.gmtime(msg['date'])) + '[' + content_type + '] ' + msg['from']['first_name'] + ' ' +msg['from']['last_name']+ ' ' + str(chat_id) + ' -->'),


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
			#print (msg['text'])
			print str(emoji.demojize(msg['text'])).decode("utf-8")
			M.Menu(self.utente,str(emoji.demojize(msg['text'])),bot,js)

		if (self.utente['RicezioneFile'] == 1):
			if (content_type == 'photo'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.jpg'))
					F.scarica_foto(msg,bot)

			elif (content_type == 'document'):
				if self.utente['MenuUpload'] == 1:
					print (msg['document']['file_name'])
					F.scarica_file(msg,bot)

			elif (content_type == 'location'):
				if self.utente['MenuUpload'] == 1:
					print ('GPS')
					F.salva_GPS(msg,bot)
				elif self.utente['MenuMeteo'] == 2:
					print ('GPS')
					LOG_file.write('GPS' + '\r\n')
					M.Menu(self.utente,'/citta',bot,js)


			elif (content_type == 'video'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.mp4'))
					F.scarica_video(msg,bot)

			elif (content_type == 'voice'):
				if self.utente['MenuUpload'] == 1:
					print (str(time.strftime("%d%m%Y%H%M%S",time.gmtime(msg['date'])) + '.ogg'))
					F.scarica_voice(msg,bot)

			elif (content_type == 'audio'):
				if self.utente['MenuUpload'] == 1:
					print (msg['audio']['title']+' - '+msg['audio']['performer']+'.mp3')
					F.scarica_audio(msg,bot)

			elif (content_type == 'contact'):
				if self.utente['MenuUpload'] == 1:
					print (msg['contact']['first_name'])
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
