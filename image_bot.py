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


def save_image_path(path):
    connection = sqlite3.connect("images.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO image (path) VALUES (?)", (path,))
    connection.commit()
    connection.close()


def get_image_path():
    connection = sqlite3.connect("images.db")
    cursor = connection.cursor()
    cursor.execute("SELECT path FROM image")
    paths = [row[0] for row in cursor.fetchall()]
    connection.close()

    return paths


@bot.message_handler(commands=["save_pic"])
def get_picture(message):
    file_info = bot.get_file(message.photo-[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = file_info.file_path.split("/")[-1]
    file_path = os.path.join("image_bot_photos", file_name)

    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    save_image_path(file_path)

    bot.send_message(message.chat.id, 'تصویر مورد نظر با موفقیت در دیتابیس ذخیره شد ✅')


bot.infinity_polling()
