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


def add_movie_db(title):
    connect = sqlite3.connect('movies_list.db')
    curs = connect.cursor()
    curs.execute("INSERT INTO movies (title) VALUES (?)", (title,))
    connect.commit()
    connect.close()


def get_movie_db():
    connect = sqlite3.connect('movies_list.db')
    curs = connect.cursor()
    curs.execute("SELECT title FROM movies")
    movies = [row[0] for row in curs.fetchall()]
    connect.close()
    return movies


@bot.message_handler(commands=['add'])
def add_movie(message):
    try:
        title = message.text.split(" ", 1)[1]
        add_movie_db(title)
        bot.reply_to(message, "با موفقیت در دیتابیس ذخیره شد ✅")
    except IndexError:
        bot.reply_to(message, "لطفا اسم فیلم را بعد از دستور /add بنویس")


@bot.message_handler(commands=["list"])
def list_movies(message):
    movies = get_movie_db()
    if movies:
        text = '\n'.join(movies)
    else:
        text = "هیچ فیلمی در دیتابیس ذخیره نشده ⭕"

    bot.reply_to(message, text)


bot.polling()
