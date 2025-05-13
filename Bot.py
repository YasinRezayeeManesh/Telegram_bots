import telebot


bot = telebot.TeleBot("7678641734:AAGoZYh-x0evr3NLReW0ZXUo-cQxNAEOx1w")


@bot.message_handler(commands=['start'])
def welcome(message):
    # send message
    # bot.send_message(message.chat.id, "welcome to my robot")

    # reply message
    bot.reply_to(message, 'hi friend')


# answering by type
@bot.message_handler(content_types=['audio', 'document'])
def audio(message):
    if message.audio:
        bot.reply_to(message, 'thank you for send me audio')
    elif message.document:
        bot.reply_to(message, 'thank you for send me document')


# search in message
@bot.message_handler(regexp='alfa')
def regexp(message):
    bot.reply_to(message, 'alfa is here')


bot.polling()
