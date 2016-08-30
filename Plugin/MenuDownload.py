import Menu as M
import Plugin.Func as F

def MenuDownload(user,text,bot,js):

	chat_id = user['chat_id']

	if (text == ':back_with_leftwards_arrow_above: Indietro' and user['MenuDownload'] == 1):
		user['MenuPrincipale'] = 1
		user['MenuDownload'] = 0
		M.Menu(user,'/help',bot,js)

	elif (text == ':file_folder: Lista file' and user['MenuDownload'] == 1):
		#f_send = open('File/' + file , 'rb')
		#bot.sendDocument(chat_id,f_send)
		elenco_file = F.list_files('File/')

		Mess_Lista_File = ''
		count = 0
		for i in elenco_file:
			Mess_Lista_File = Mess_Lista_File + '\n' + str(count) + ' - ' + i 
			count = count +1

		Numero_tasti = len(elenco_file)

		Tasti = F.Crea_tastiera(Numero_tasti)

		Tastiera_File = {'keyboard': Tasti , 'resize_keyboard' : True}
		user['MenuDownload'] = 2
		bot.sendMessage(chat_id,str(Mess_Lista_File),reply_markup=Tastiera_File)

	elif (user['MenuDownload'] == 2):
		elenco_file = F.list_files('File/')
		if text == ':back_with_leftwards_arrow_above: Indietro':
			user['MenuDownload'] = 0
			user['MenuPrincipale'] = 1
			M.Menu(user,'/help',bot,js)
			return

		if text.isdigit() == False :
			bot.sendMessage(chat_id,'Inserire solo numeri')
			return

		if int(text) > len(elenco_file):
			bot.sendMessage(chat_id,'File non esiste')
			return
        

		file = elenco_file[int(text)]
		f_send = open('File/' + file , 'rb')
		if file[0:3] == 'GPS':
			GPS = open('File/' + file,"r")
			P = GPS.read()
			delimiter = ','
			L = []
			L = P.split(delimiter)

			bot.sendLocation(chat_id,L[0],L[1])
		else:
			bot.sendDocument(chat_id,f_send)


	#------------------------------echo
	else:
		M.Menu(user,'/help',bot,js)