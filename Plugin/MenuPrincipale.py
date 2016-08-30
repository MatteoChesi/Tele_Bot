import subprocess
import emoji
import time
import psutil

import Func as F
import Menu as M

def MenuPrincipale(user,text,bot,js):

	chat_id = user['chat_id']

	if(text == '/time'):
		bot.sendMessage(chat_id, emoji.emojize(':date: ' + str(time.strftime("%d/%m/%Y",time.localtime())) + '\n \n' + ':hourglass:' +str(time.strftime("%H:%M:%S %d/%m/%Y",time.localtime())) + ':hourglass_flowing_sand:', use_aliases=True) ) #:date:
    
	elif (text == '/temp'):
		comand = subprocess.check_output(['vcgencmd measure_temp '],shell=True)
		comand = str(comand[5:9])
		bot.sendMessage(chat_id,'Temperatura CPU = ' + str(comand) + 'C')

	elif (text == '/ip'):
		IP_PUB = subprocess.check_output(['curl ident.me'],shell=True)
		IP_LAN = psutil.net_if_addrs()['eth0'][0][1]
		bot.sendMessage(chat_id, emoji.emojize(":globe_with_meridians:", use_aliases=True) + ' IP Pubblico : \n' + IP_PUB + '\n' + emoji.emojize(":computer:", use_aliases=True) + ' IP Locale : \n' + IP_LAN) 
		bot.sendMessage(chat_id,'Speed test in corso ...')
		bot.sendChatAction(chat_id,'typing')
		P , D, U = F.speed_test()
		bot.sendMessage(chat_id,'Ping: '+P +' ms\n'+'Download: '+D+'\nUpload: '+U)

	elif (text == '/send'):
		user['MenuPrincipale'] = 0
		user['MenuUpload'] = 1
		user['RicezioneFile'] = 1
		M.Menu(user,'/help',bot,js)

	elif (text == '/meteo'):
		user['MenuPrincipale'] = 0
		user['MenuMeteo'] = 1
		M.Menu(user,'/citta',bot,js)
		#M.Menu(user,'/Citta',bot,js)

	elif (text == '/down'):
		user['MenuPrincipale'] = 0
		user['MenuDownload'] = 1
		M.Menu(user,'/help',bot,js)

	elif (text == '/reset' and str(chat_id) == str(js['Admin']) ):
		bot.sendMessage(chat_id,'reset...' )
		comand = subprocess.check_output(['sudo shutdown -r 1'],shell=True)

	#------------------------------echo
	else:
		M.Menu(user,'/help',bot,js)