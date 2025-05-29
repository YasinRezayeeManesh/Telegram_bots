import telebot
import os
import sqlite3

bot = telebot.TeleBot("8173824325:AAH1HRs2brPz8HXVHRE6SKm2ssxRTxqLhII")


if not os.path.exists("image_bot_photos"):
    os.makedirs("image_bot_photos")


def create_db():
    connection = sqlite3.connect("images.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS image(
            id INTEGER PRIMARE KEY,
            path TEXT
        )
    """)
    connection.commit()
    connection.close()


create_db()


bot.infinity_polling()
