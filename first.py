import telebot
import pyowm

from telebot import apihelper
 
apihelper.proxy = {'https':'https://162.243.163.60:8080'}

owm = pyowm.OWM ('40f2982c299cfd3cee2cc5ab4a749ff8')
bot = telebot.TeleBot ("805618208:AAEkp0Xat3eP3sFXGysRRU_aHTaBl_GFx7c")

@bot.message_handler (content_types = ["text"])
def send_echo (message):
	observation = owm.weather_at_place (message.text)
	w = observation.get_weather ()
	temp = w.get_temperature ('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + ". Влажность воздуха " + str(hum) + "%." + "\n"
	answer += "Температура " + str(temp) + "°С, скорость ветра " + str(wind) + " м/c."

	bot.send.message (message.chat.id, answer)
	
bot.polling (none_stop = True)
