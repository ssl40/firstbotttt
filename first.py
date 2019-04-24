import pyowm
import telebot

owm = pyowm.OWM ("8111322c1d237a4929d7f80ed44865b6")
bot = telebot.TeleBot ("805618208:AAEkp0Xat3eP3sFXGysRRU_aHTaBl_GFx7c")

@bot.message_handler (content_types = ["text"])
def send_echo (message):
	observation = owm.weather_at_place (message.text)
	w = observation.get_weather ()
	temp = w.get_temperature ("celsius")["temp"]

	answer = w
	answer += str(temp)

bot.polling (none_stop = True)
