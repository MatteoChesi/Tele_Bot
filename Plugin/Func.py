import os
import emoji
import time
import urllib2
import pyspeedtest

agent = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def traduci(to_translate, to_langage="auto", langage="auto"):
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
    request = urllib2.Request(link, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return result

def list_files(path):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files


def scarica_foto(msg,bot):
    #print('scarica_foto')
    file = msg['photo'][len(msg['photo'])-1]['file_id']
    t = time.strftime("%d%m%Y%H%M%S",time.localtime(msg['date']))
    bot.download_file(file , 'File/' + t +'.jpg')
    bot.sendMessage(msg['chat']['id'], 'Foto salvata!\n'+t)
    
def scarica_file(msg,bot):
    #print('scarica_file')
    file = msg['document']['file_id']
    bot.download_file(file ,'File/' + msg['document']['file_name'])
    bot.sendMessage(msg['chat']['id'], 'Documento salvato!\n'+msg['document']['file_name'])

def salva_GPS(msg,bot):
    #print('salva_GPS')
    t = time.strftime("%d%m%Y%H%M%S",time.localtime(msg['date']))
    file = open("File/GPS-"+t+"-"+msg['from']['first_name'] + ' ' +msg['from']['last_name']+".txt","w")
    file.write(str(msg['location']['latitude']) + ',' + str(msg['location']['longitude']))
    file.close()
    bot.sendMessage(msg['chat']['id'], 'Posizione salvata!\nGPS-'+t)
  
def scarica_video(msg,bot):
    file = msg['video']['file_id']
    t = time.strftime("%d%m%Y%H%M%S",time.localtime(msg['date']))
    bot.download_file(file , 'File/' + t +'.mp4')
    bot.sendMessage(msg['chat']['id'], 'Video salvato!\n'+t)
  
def scarica_voice(msg,bot):
    file = msg['voice']['file_id']
    t = time.strftime("%d%m%Y%H%M%S",time.localtime(msg['date']))
    bot.download_file(file , 'File/' + t +'.ogg')
    bot.sendMessage(msg['chat']['id'], 'Voce salvata!\n'+t)
    
def scarica_audio(msg,bot):
    file = msg['audio']['file_id']
    t = msg['audio']['title']+' - '+msg['audio']['performer']
    bot.download_file(file , 'File/' + t +'.mp3')
    bot.sendMessage(msg['chat']['id'], 'Audio salvato!\n'+t)
  
def scarica_contact(msg,bot):
    t = msg['contact']['first_name']
    file = open("File/"+t+".txt","w")
    file.write(str(msg['contact']['first_name'])+' - '+str(msg['contact']['phone_number']))
    file.close()
    bot.sendMessage(msg['chat']['id'], 'Contatto salvato!\n'+t)
    if(msg['contact']['user_id']):
        file = open("File/"+t+".txt","a")
        file.write(' - '+str(msg['contact']['user_id']))
        file.close()

def Crea_tastiera(N_t):
    l1 = []
    delimiter = '-'
    s = ''
    for i in range(N_t):
        #l1.append(str(i))
        s = s + str(i) + '-'
        
        if i%5 == 4:
            l1.append(s.split(delimiter))
            s = ''
    l1.append(s.split(delimiter))
    s = ''
    l1.append([emoji.emojize(':back_with_leftwards_arrow_above: Indietro')])
    return l1


def Verifica_Posizione(user):
    if len(user['Posizione']) == 0:
        return 0

def speed_test():
	st = pyspeedtest.SpeedTest()
	ping = str(st.ping())[:6]
	down = pyspeedtest.pretty_speed(st.download())
	up = pyspeedtest.pretty_speed(st.upload())
	return ping , down , up