import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

bot = telebot.TeleBot("7678641734:AAGoZYh-x0evr3NLReW0ZXUo-cQxNAEOx1w")


@bot.message_handler(commands=['start'])
def welcome(message):
    # send message
    # bot.send_message(message.chat.id, "welcome to my robot")

    # reply message
    bot.reply_to(message, 'hi friend')


# answering by type
@bot.message_handler(content_types=['audio', 'document'])
def audio(message):
    if message.audio:
        bot.reply_to(message, 'thank you for send me audio')
    elif message.document:
        bot.reply_to(message, 'thank you for send me document')


# search in message
@bot.message_handler(regexp='alfa')
def regexp(message):
    bot.reply_to(message, 'alfa is here')


# First conversation with a robot
@bot.message_handler(commands=['talk'])
def conversation(message):
    bot.reply_to(message, 'hello 👋 \nwhat is your name?')
    bot.register_next_step_handler(message, name)


def name(message):
    client_name = message.text
    bot.send_message(message.chat.id, f"Hello {client_name}! how old are you?")
    bot.register_next_step_handler(message, age)


def age(message):
    client_age = message.text
    bot.send_message(message.chat.id, f"you are {client_age} years old \nthank you!")


# create buttons
button1 = InlineKeyboardButton(text="alfa button", callback_data="alfa")
button2 = InlineKeyboardButton(text="beta button", callback_data="beta")
inline_keyboards = InlineKeyboardMarkup(row_width=1)
inline_keyboards.add(button1, button2)


# show buttons
@bot.message_handler(commands=['button'])
def buttons(message):
    bot.send_message(message.chat.id, 'button list 👇', reply_markup=inline_keyboards)


# callback buttons
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "alfa":
        bot.answer_callback_query(call.id, 'answer alfa', show_alert=True)
    elif call.data == "beta":
        bot.answer_callback_query(call.id, 'answer beta')


# Reply Button
reply_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_button.add("theta button", "lota button")


@bot.message_handler(commands=['keyboard_button'])
def keyboard_button(message):
    bot.reply_to(message, "Chose the button", reply_markup=reply_button)


@bot.message_handler(func=lambda message: True)
def callback_keyboard_btn(message):
    if message.text == "theta button":
        bot.reply_to(message, "you chose theta btn")
    elif message.text == "lota button":
        bot.reply_to(message, "you chose lota btn")
    else:
        bot.reply_to(message, f"your message is {message.text}")


bot.polling()
