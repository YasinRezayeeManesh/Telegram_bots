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


def submenu_1_1():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('Button 1-1', callback_data='button')
    return_button = InlineKeyboardButton('back', callback_data='back to submenu 1')
    markup.add(button_1, return_button)
    return markup


def submenu_1_2():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('Button 1-2', callback_data='button')
    return_button = InlineKeyboardButton('back', callback_data='back to submenu 1')
    markup.add(button_1, return_button)
    return markup


def sub_menu_2():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('submenu 2-1', callback_data='submenu 2-1')
    button_2 = InlineKeyboardButton('submenu 2-1', callback_data='submenu 2-2')
    return_button = InlineKeyboardButton('back', callback_data='back to main menu')
    markup.add(button_1, button_2, return_button)
    return markup


def submenu_2_1():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('button 2-1', callback_data='button')
    return_button = InlineKeyboardButton('back', callback_data='back to submenu 2')
    markup.add(button_1, return_button)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please Chose Menu", reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'menu 1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You are in Menu 1', reply_markup=sub_menu_1())
    elif call.data == 'submenu 1-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Your are in submenu 1-1', reply_markup=submenu_1_1())
    elif call.data == 'submenu 1-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='you are in submenu 1-2', reply_markup=submenu_1_2())
    elif call.data == 'back to main menu':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='please chose menu', reply_markup=main_menu())
    elif call.data == 'back to submenu 1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You are in Menu 1', reply_markup=sub_menu_1())


bot.infinity_polling()
