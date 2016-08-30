import emoji
from Plugin.MenuPrincipale import MenuPrincipale
from Plugin.MenuUpload import MenuUpload
from Plugin.MenuDownload import MenuDownload
from Plugin.MenuMeteo import MenuMeteo

from Plugin.Func import Verifica_Posizione

Tastiera_Upload = {'keyboard': [[emoji.emojize(':back_with_leftwards_arrow_above: Indietro')]], 'resize_keyboard' : True}  # [['Yes'], ['Maybe']]
Tastiera_Meteo = {'keyboard': [[emoji.emojize(':arrows_counterclockwise: Oggi', use_aliases=True),emoji.emojize(':round_pushpin: Modifica Citta')],[emoji.emojize(':back_with_leftwards_arrow_above: Indietro')]], 'resize_keyboard' : True}  # [['Yes'], ['Maybe']]
Tastiera_Download = {'keyboard': [[emoji.emojize(':back_with_leftwards_arrow_above: Indietro')], [emoji.emojize(':file_folder: Lista file')]], 'resize_keyboard' : True}

Nascondi_Tastiera = {'hide_keyboard': True}


help_mesage = """

:hourglass: /time - Visualizzare la data e l'ora
:globe_with_meridians: /ip - IP pubblico attuale
:sunny: /meteo - Informazioni meteo
:hotsprings: /temp - Temperatura RPi
:arrow_double_up: /send - Inviare File
:arrow_double_down: /down - Scaricare File
""" 


def Menu(user,text,bot,js):
	chat_id = user['chat_id']
	

	if( text == '/help'):
		
		if user['MenuPrincipale'] == 1:
			bot.sendMessage(chat_id, 
				emoji.emojize(":sos:", use_aliases=True) + ' Lista Comandi ' + emoji.emojize(":sos:", use_aliases=True) + emoji.emojize(help_mesage, use_aliases=True) , reply_markup=Nascondi_Tastiera )

		elif user['MenuUpload'] == 1:
			bot.sendMessage(chat_id,
				'Adesso puoi inviare :\n' + 
				emoji.emojize(":camera:", use_aliases=True) + ' Immagini\n' + 
				emoji.emojize(":page_facing_up:", use_aliases=True) + ' Documenti\n' +
				emoji.emojize(":video_camera:", use_aliases=True) + ' Video\n' +
				emoji.emojize(":round_pushpin:", use_aliases=True) + ' Posizioni GPS \n' +
				emoji.emojize(":microphone:", use_aliases=True) + ' Messaggi Vocali \n' +
				emoji.emojize(":bust_in_silhouette:", use_aliases=True) + ' Contatti' , 
				reply_markup=Tastiera_Upload)

		elif user['MenuDownload'] == 1:
			bot.sendMessage(chat_id,
				'Adesso puoi scaricare i file archiviati :\n',
				reply_markup=Tastiera_Download)

		elif user['MenuMeteo'] == 1:
			bot.sendMessage(chat_id,
				'Informazioni meteo: '+ str(user['Citta']),
				reply_markup=Tastiera_Meteo)
			


	elif(user['MenuPrincipale'] > 0):
		MenuPrincipale(user,text,bot,js)

	elif(user['MenuMeteo'] > 0):
		MenuMeteo(user,text,bot,js)

	elif(user['MenuUpload'] > 0):
		MenuUpload(user,text,bot,js)

	elif(user['MenuDownload'] > 0):
		MenuDownload(user,text,bot,js)
