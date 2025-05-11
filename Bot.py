import telebot


bot = telebot.TeleBot("7678641734:AAGoZYh-x0evr3NLReW0ZXUo-cQxNAEOx1w")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to my robot")


bot.polling()
