import telebot
bot = telebot.TeleBot('1558588326:AAGZ-OO0CAOa-FtU70SliQH6-NfR_OaU410')

@bot.message_handler(commands=['/start'])
def fovno_message(message):
	bot.send_message(message.chat.id, message.chat.id)

bot.polling()