import telebot
import sqlite3

bot = telebot.TeleBot("7967925856:AAFfzJpNV8R7iTwcHvWY-3XDEepV3zEumog")


with sqlite3.connect('movies_list.db') as connection:
    curser = connection.cursor()
    curser.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id integer primary key,
            title text
        );
    """)


def get_movie_db():
    connect = sqlite3.connect('movies_list.db')
    curs = connect.cursor()
    curs.execute("Select title From movies_list")
    movies = [row[0] for row in curs.fetchall()]
    connect.close()
    return movies


@bot.message_handler(commands=['add'])
def add_movie(message):
    pass


@bot.message_handler(commands=["list"])
def list_movies(message):
    pass


bot.polling()
