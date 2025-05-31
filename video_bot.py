import telebot
import sqlite3
import os

bot = telebot.TeleBot("8073560883:AAHxkl3eCKT5sh_ZatEyouRtBr3ZFSdMuP4")


def create_db():
    connection = sqlite3.connect("videos.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS video(
            id integer primary key,
            path text
        )
    """)
    connection.commit()
    connection.close()


create_db()


bot.infinity_polling()
