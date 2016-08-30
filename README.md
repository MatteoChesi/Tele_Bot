# Tele_Bot
Telegram bot usando la libreria Telepot

## Dipendenze
* emoji
* psutil
* requests
* RPi.GPIO
* smbus
* telepot
* urllib3

## Come installare
* Sacaricare la repository
```shell
git clone --recursive https://github.com/pharia95/Tele_Bot && cd Tele_Bot
```
* Sacaricare e aggionare dipendenze python
```shell
pip install -r requirements.txt
```
* Configurare file "CONFIG"
```json
{
	"KEY Telegram": "YOUR-KEY",            <---
	"Admin": "YOUR-chat_id",               <---
	"Meteo" : {
		"KEY" : "YOUR-KEY",                <---
		"Url" : "https://api.forecast.io/forecast/"
	},
	"Geocoding" : {
		"KEY" : "YOUR-KEY",                <---
		"Url_Citta" : "https://maps.googleapis.com/maps/api/geocode/json?address=",
		"Url_GPS" : "https://maps.googleapis.com/maps/api/geocode/json?latlng="
	}
}
```
* Lanciare il Bot
```shell
python Telegram_Bot.py
```
* Comandi disponibili
![](http://i.imgur.com/TxIlSnE.jpg)
