from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = TeleBot("8033272065:AAE3D4XCamABh_Cx4i7coXWYWD4bMCj9Sc0")


def main_menu():
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Menu 1', callback_data='menu_1')
    button_2 = InlineKeyboardButton('Menu 2', callback_data='menu_2')
    markup.add(button_1, button_2)
    return markup


bot.infinity_polling()
