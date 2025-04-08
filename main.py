import telebot

# Bot tokeningizni shu yerga kiriting
TOKEN = '7612699378:AAF0tD70RD9Gr2_0ofYDPQB5X-BSU4Z7tW4'
bot = telebot.TeleBot(TOKEN)

# /start buyrug‘iga javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men oddiy Telegram botman. Xabar yozing — men uni sizga qaytaraman.")

# Har qanday matnli xabarga javob
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Botni ishga tushirish
bot.polling()