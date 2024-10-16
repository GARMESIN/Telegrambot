import telebot
from telebot import types
from telebot.apihelper import stop_poll

bot = telebot.TeleBot('8086657410:AAEQvumrkNC7Av8e8ufMsKOvXJRk38VIvAA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('share')
    markup.row(btn)
    bot.send_message(message.chat.id, 'do you want to share?', reply_markup=markup)

@bot.message_handler(content_types=['text', 'photo', 'document', 'audio', 'video'])
def main(message):
    if message.text == 'share':
        bot.send_message(message.chat.id, 'send')
    else:
        bot.forward_message(chat_id=-1002484956892, from_chat_id=message.chat.id, message_id=message.message_id)

bot.polling(none_stop = True)