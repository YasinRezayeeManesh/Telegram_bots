import telebot
import sqlite3
import os

bot = telebot.TeleBot("8073560883:AAHxkl3eCKT5sh_ZatEyouRtBr3ZFSdMuP4")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "خوش آمدید 👋 \n\n 💠 برای ذخیره ویدیو های خود کافیست آن را بدون هیچ پسوند یا پیشوندی ارسال کنید \n\n 💠 دستور /videos ==> برای دریافت ویدیو های ذخیره شده کافیست از این دستور استفاده کنید")


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


def save_video_path(path):
    connection = sqlite3.connect('videos.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO video(path) VALUES (?)", (path,))
    connection.commit()
    connection.close()


@bot.message_handler(content_types=["video"])
def get_video(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    file_name = file_info.file_path.split('/')[-1]
    file_path = os.path.join('videos', file_name)

    os.makedirs("videos", exist_ok=True)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    save_video_path(file_path)

    bot.send_message(message.chat.id, "ویدیو مورد نظر با موفقیت در دیتابیس ذخیره شد ✅")


@bot.message_handler(commands=["videos"])
def send_videos(message):
    connection = sqlite3.connect('videos.db')
    cursor = connection.cursor()
    cursor.execute("SELECT path FROM video")
    videos = cursor.fetchall()
    connection.close()

    if videos:
        for video in videos:
            video_path = video[0]
            with open(video_path, 'rb') as video_file:
                bot.send_video(message.chat.id, video_file)
    else:
        bot.send_message(message.chat.id, "هیچ ویدیویی در دیتابیس ذخیره نشده است ⭕")


bot.infinity_polling()
