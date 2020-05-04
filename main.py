import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from get_ip import api_get_ip, get_ip_info
from func import start, echo, caps, help_info, get_ip, input_ip
from config import TOKEN


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
help_info_handler = CommandHandler('help', help_info)
echo_handler = MessageHandler(Filters.text, echo)
caps_handler = CommandHandler('caps', caps)
get_ip_handler = CommandHandler('url', get_ip)
input_ip_handler = CommandHandler('ip', input_ip)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_info_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(get_ip_handler)
dispatcher.add_handler(input_ip_handler)

updater.start_polling()
