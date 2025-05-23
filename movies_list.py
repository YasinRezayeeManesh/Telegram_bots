import telebot

bot = telebot.TeleBot("7967925856:AAFfzJpNV8R7iTwcHvWY-3XDEepV3zEumog")


@bot.message_handler(commands=['add'])
def add_movie(message):
    pass


@bot.message_handler(commands=["list"])
def list_movies(message):
    pass


bot.polling()
