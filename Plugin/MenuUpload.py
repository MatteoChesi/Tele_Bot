import Menu as M
import emoji

def MenuUpload(user,text,bot,js):

	if (text == ':back_with_leftwards_arrow_above: Indietro' and user['MenuUpload'] == 1):
		user['MenuPrincipale'] = 1
		user['MenuUpload'] = 0
		user['RicezioneFile'] = 0
		M.Menu(user,'/help',bot,js)


	#------------------------------echo
	else:
		M.Menu(user,'/help',bot,js)