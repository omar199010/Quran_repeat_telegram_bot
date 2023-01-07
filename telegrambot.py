import logging 
# which allows you to log messages from your application

from telegram import Update 
# An Update represents an incoming update from the Telegram API
from telegram import InlineQueryResultArticle 
# This class represents a single result of an inline query
from telegram import InputTextMessageContent 
# This class represents the content of a text message to be sent as the result of an inline query
from telegram.ext import filters 
# This module provides various filters that can be used to determine if a update should be passed to a handler
from telegram.ext import MessageHandler 
# This class is used to handle updates that contain messages
from telegram.ext import ApplicationBuilder 
# This class is used to create and configure a Telegram bot
from telegram.ext import CommandHandler
# The CommandHandler class is used to handle updates that contain commands
from telegram.ext import ContextTypes 
#  the ContextTypes object contains constants that represent the different types of context that a command can be run in
from telegram.ext import InlineQueryHandler 
# This class is used to handle updates that contain inline queries
from telegram.ext import ConversationHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
    text='''
هذا البرنامج لاختيار أيات متتالية او سور محددة للتلاوة  لمختلف القراء 
و يقدمها لك كقائمة تشغيل يمكن تشغيلها على جهازك 
تطلب انترنت لتعمل 

البرنامج قيد التجريب
ننصح بإستخدام برنامج VLC
أرسل  /Ayat لاختيار أيات محددة
أرسل /Sura  لإختيار سور محددة
أرسل  /Radio لاختيار البث المباشر

This program to play certain Ayat or Souar continously
with diffrent readers 
we recommend to use VLC player 

send /Ayat for ayat  
send /Sura for complete suar
send /Radio for stream list
''')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
    text='''
هذا البرنامج لاختيار أيات متتالية او سور محددة للتلاوة  لمختلف القراء 
و يقدمها لك كقائمة تشغيل يمكن تشغيلها على جهازك 
تطلب انترنت لتعمل 

البرنامج قيد التجريب
ننصح بإستخدام برنامج VLC
أرسل  /Ayat لاختيار أيات محددة
أرسل /Sura  لإختيار سور محددة
أرسل  /Radio لاختيار البث المباشر

This program to play certain Ayat or Souar continously
with diffrent readers 
we recommend to use VLC player 

send /Ayat for ayat  
send /Sura for complete suar
send /Radio for stream list
''')

async def ayat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)     

async def suar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_path = '/path/to/your/file.txt'
    await context.bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))

async def radio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_radio = ''' we recommend to use 
https://www.atheer-radio.com/'''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_radio)
    #todo this list need to be modified 
    file_path = 'mp3QuranList_Generator\RadioList.m3u'
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, 'rb'))

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
   

if __name__ == '__main__':
    application = ApplicationBuilder().token('5296769845:AAHSNpG_pPfECfa_wTXuot4FUhERxlfQDlU').build()

    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)
    radio_handler = CommandHandler('radio', radio)
    application.add_handler(radio_handler)

    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

#last handler
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo) 
    application.add_handler(echo_handler)         
    
    application.run_polling()