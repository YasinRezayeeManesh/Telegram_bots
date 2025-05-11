import telebot


bot = telebot.TeleBot("7678641734:AAGoZYh-x0evr3NLReW0ZXUo-cQxNAEOx1w")


@bot.message_handler(commands=['start'])
def welcome(message):
    # send message
    # bot.send_message(message.chat.id, "welcome to my robot")

    # reply message
    bot.reply_to(message, 'hi friend')


bot.polling()
