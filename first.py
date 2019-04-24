import pyowm
import telebot

owm = pyowm.OWM ('40f2982c299cfd3cee2cc5ab4a749ff8')
bot = telebot.TeleBot ("805618208:AAEkp0Xat3eP3sFXGysRRU_aHTaBl_GFx7c")

@bot.message_handler (content_types = ["text"])
def send_echo (message):
	observation = owm.weather_at_place (message.text)
	w = observation.get_weather ()
	temp = w.get_temperature ('celsius')["temp"]

	answer = Привет!
	answer += str(temp)

	bot.send.message (message.chat.id, answer)
	
bot.polling (none_stop = True)
