import telebot

bot = telebot.TeleBot ("805618208:AAEkp0Xat3eP3sFXGysRRU_aHTaBl_GFx7c")

@bot.message_handler (content_types = ["text"])
def send_echo (message):
	bot.send_message (message.chat.id, message.text)

bot.polling (none_stop = True)