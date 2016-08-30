import Menu as M
import emoji
import requests
import time
import Func as F



def MenuMeteo(user,text,bot,js):
	
	chat_id = user['chat_id']

	if (text == ':back_with_leftwards_arrow_above: Indietro' and user['MenuMeteo'] == 1):
		user['MenuPrincipale'] = 1
		user['MenuMeteo'] = 0
		user['RicezioneFile'] = 0
		M.Menu(user,'/help',bot,js)

	elif (text == '/citta'):
		if len(user['Citta']) == 0 and len(user['GPS']) == 0:
			user['RicezioneFile'] = 1
			user['MenuMeteo'] = 2
			bot.sendMessage(chat_id,'Inserire una Citta o inviare la tua posizione GPS',reply_markup={'keyboard': [[{'request_location': True, 'text': 'Invia Posizione'}]], 'resize_keyboard' : True})
		else :

			if len(user['GPS']) != 0 :
				Aggiorna_Citta(user,js)
			else:
				Aggiorna_GPS(user,js)

			user['RicezioneFile'] = 0
			user['MenuMeteo'] = 1
			M.Menu(user,'/help',bot,js)

	elif (user['MenuMeteo'] == 2):
		if text.isalpha() == False :
			M.Menu(user,'/citta',bot,js)
		else:
			url = str(js['Geocoding']['Url_Citta'])+ str(text) + '&key=' + str(js['Geocoding']['KEY'])
			#print url
			page = requests.get(url)
			page = page.json()
			#print page['status']
			
			if str(page['status']) == 'OK':
				user['Citta'] = text
				user['MenuMeteo'] = 1
				M.Menu(user,'/citta',bot,js)
			else:
				bot.sendMessage(chat_id,'Citta insesitente')

	elif (text == ':round_pushpin: Modifica Citta'):
		user['Citta'] = ''
		user['GPS'] = ''
		M.Menu(user,'/citta',bot,js)
	
	elif (text == ':anticlockwise_downwards_and_upwards_open_circle_arrows: Oggi'):
		bot.sendChatAction(chat_id,'typing')
		page = requests.get(str(js['Meteo']['Url']) + str(js['Meteo']['KEY']) +'/'+ str(user['GPS']) + '?units=si')
		page = page.json()
		#print user['Citta']
		#print user['GPS']
		#print str(time.strftime("%H:%M:%S",time.localtime(page['currently']['time'])))
		Meteo_text = F.traduci(str(page['currently']['summary'].encode('utf8')),to_langage="it")
		Icon = str(page['currently']['icon'].encode('utf8'))
		Possibilita_pioggia = str(page['currently']['precipProbability'])[3:] + '%'
		Temp = str(page['currently']['temperature']) + ' C'
		Umidita = str(page['currently']['humidity'])[3:] + '%'
		Pressione = str(page['currently']['pressure']) + ' mbar'
		Prossime_ore = F.traduci(str(page['hourly']['summary'].encode('utf8')),to_langage="it").encode('utf8')
		Prossimi_giorni = F.traduci(str(page['daily']['summary'].encode('utf8')),to_langage="it").decode("utf8")
		Alba = str(time.strftime("%H:%M:%S",time.localtime(page['daily']['data'][0]['sunriseTime'])))
		Tramonto = str(time.strftime("%H:%M:%S",time.localtime(page['daily']['data'][0]['sunsetTime'])))

		# clear-day
		# clear-night
		# rain
		# snow
		# sleet
		# wind
		# fog
		# cloudy
		# partly-cloudy-day
		# partly-cloudy-night

		bot.sendMessage(chat_id,
			Meteo_text +'  -' + Icon+'-' +'\n'+
			u'\U00002614'+'*Possibilita pioggia*:  '+Possibilita_pioggia+'\n'+
			u'\U0001F321'+'*Temperatura*:  '+Temp+'\n'+
			u'\U0001F4A7'+'*Umidita*:  '+Umidita+'\n'+
			u'\U0001F4A8'+'*Pressione*: '+Pressione+'\n'+
			u'\U0001F305'+'*Alba*: '+Alba+'\n'+
			u'\U0001F304'+'*Tramonto*: '+Tramonto+'\n'+
			u'\U000025B6'+'*Prossime ore*: \n_'+Prossime_ore+'_\n'+
			u'\U000023E9'+'*Prossimi giorni*: \n_'+Prossimi_giorni+'_'
			,parse_mode='Markdown')


	elif (text == '/Aggiorna' and user['MenuMeteo'] == 1):
		print user['Citta']
		print user['GPS']




def Aggiorna_Citta(user,js):
	url = str(js['Geocoding']['Url_GPS'])+str(user['GPS'])+'&key='+str(js['Geocoding']['KEY'])
	page = requests.get(url)
	page = page.json()
	user['Citta'] = str(page['results'][0]['address_components'][2]['long_name']).encode('utf-8')

def Aggiorna_GPS(user,js):
	url = str(js['Geocoding']['Url_Citta'])+str(user['Citta'])+'&key='+str(js['Geocoding']['KEY'])
	page = requests.get(url)
	page = page.json()
	user['GPS'] = str(page['results'][0]['geometry']['location']['lat']) +','+ str(page['results'][0]['geometry']['location']['lng'])
