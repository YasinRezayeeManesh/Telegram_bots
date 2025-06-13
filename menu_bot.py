from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = TeleBot("8033272065:AAE3D4XCamABh_Cx4i7coXWYWD4bMCj9Sc0")


def main_menu():
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Menu 1', callback_data='menu 1')
    button_2 = InlineKeyboardButton('Menu 2', callback_data='menu 2')
    markup.add(button_1, button_2)
    return markup


def sub_menu_1():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('submenu 1-1', callback_data='submenu 1-1')
    button_2 = InlineKeyboardButton('submenu 1-2', callback_data='submenu 1-2')
    return_button = InlineKeyboardButton('back', callback_data='back to main menu')
    markup.add(button_1, button_2, return_button)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please Chose Menu", reply_markup=main_menu())


bot.infinity_polling()
