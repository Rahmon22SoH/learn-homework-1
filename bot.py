import logging
from turtle import title
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Импортируем нужные компоненты
import ephem




logging.basicConfig(
    level=logging.INFO,
    filename = 'bot.log',
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

# С любым прокси выдаёт ошибку PROXY = IndentationError: unexpected indent


# Функция, которая соединяется с платформой Telegram
def planet_user (update,context):
    print('Вызван /planet')
    message =  update.message.text.split()[1]
    print(message)

    if message =='Venus':
        update.message.reply_text(ephem.constellation(ephem.Venus('04.06.2022')))
    elif message == 'Mars':
        update.message.reply_text(ephem.constellation(ephem.Mars('04.06.2022')))
    elif message == 'Mercury':
         update.message.reply_text(ephem.constellation(ephem.Mercury('04.06.2022')))
    elif message == 'Jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter('04.06.2022')))
    elif message == 'Saturn':
         update.message.reply_text(ephem.constellation(ephem.Saturn('04.06.2022')))
    elif message == 'Uranus':
         update.message.reply_text(ephem.constellation(ephem.Uranus('04.06.2022')))
    elif message == 'Neptune':
         update.message.reply_text(ephem.constellation(ephem.Neptune('04.06.2022')))
    elif message == 'Pluto':
         update.message.reply_text(ephem.constellation(ephem.Pluto('04.06.2022')))
    else:
        update.message.reply_text('Напиши планеты солнечной системы')

def greet_user(bot, update):
    print('Вызван /start') # написать в консоле
    #print(update) # информация о пользователе 
    update.message.reply_text('Здравствуй,пользователь!') #написать пользователю

def talk_to_me(update,context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():

    mybot = Updater(settings.API_KEY, use_context = True) 
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   
    logging.info('Бот стартовал')

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()




# Экранируем вызов main() 
# 'Вызов функций прямо на верхнем уровне считается плохим стилем и в дальнейшем вызовет проблемы'

main()