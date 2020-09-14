import telebot
import Randomizer

#AmuraChan = telebot.TeleBot('1268709960:AAFanrVm54FbLoNccGcrOkf1FFgFS8GqdOk')
AmuraChan = telebot.TeleBot(Randomizer.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Как дела?', 'тестПикча')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Случайная тян', 'Случайный этти', 'Случайный хентай')

@AmuraChan.message_handler(commands=['start'])
def start_message(message):
    AmuraChan.send_message(message.chat.id, 'Амура тян в здании', reply_markup=keyboard1)

@AmuraChan.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        AmuraChan.send_message(message.chat.id, Randomizer.random1(), reply_markup=keyboard1)
    if message.text == 'Как дела?':
        AmuraChan.send_message(message.chat.id, Randomizer.random2(), reply_markup=keyboard1)
    if message.text == 'тестПикча':
        AmuraChan.send_message(message.chat.id, Randomizer.random3(), reply_markup=keyboard1)

AmuraChan.polling()
