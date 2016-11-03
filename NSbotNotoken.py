#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# NS fietsenstalling bot
"""
This Bot uses the Updater class to handle the bot.

Then, the bot is started and runs until we press Ctrl-C on the command line.
"""
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardHide
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import time
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


    
logger = logging.getLogger(__name__)
adminid = 
userlog = []
linkingActive = []

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi! Deze bot staat momenteel op debug mode \nHij zal berichten terug sturen')
    if update.message.chat_id not in userlog:
        userlog.append(update.message.chat_id)
    bot.sendMessage(update.message.chat_id, "Welkom bij de NS fietsenstalling bot \n \nom te beginnnen kan je het aantal plaatsen vrij bekijken. \n voor het zien van personlijke informatie kan je je telegram doorlinken met je stallings ID", reply_markup=ReplyKeyboardMarkup([["Link account"], ["Aantal plaatsen vrij"]]))

def antwoordja(bot, update):
    update.message.reply_text('NEE')

def reply(bot, update):
    if update.message.chat_id not in userlog:
        userlog.append(update.message.chat_id)
        print(userlog)
    if update.message.chat_id in linkingActive:
        linking(bot, update)
    elif update.message.text == "Link account":
        link(bot, update)
    elif update.message.text == "Aantal plaatsen vrij":
        vrij(bot, update)
    elif update.message.text == "help":
        help(bot, update)
    else:
        answer(bot, update)

def link(bot, update):
    print(update.message.chat_id, "Linking..")
    linkingActive.append(update.message.chat_id)

    bot.sendMessage(update.message.chat_id, "Voer nu je ID in met getallen 0-9", reply_markup=ReplyKeyboardHide(hide_keyboard=True, selective=False))
def linking(bot, update):
    print(linkingActive)
    telegramID = update.message.chat_id
    stallingID = update.message.text
    #ik weet nog niet wat de range is
    print(stallingID)
    try:
        stallingID = int(stallingID)
        if stallingID > 99999 and stallingID < 1000000:

            linkingActive.remove(update.message.chat_id)
            bot.sendMessage(update.message.chat_id, "Je account is gelinked", reply_markup=ReplyKeyboardMarkup([["Aantal plaatsen vrij"]]))
            #store telegram id en stalling id
        else:
            update.message.reply_text('De invoer was niet correct. Probeer opnieuw \nOf gebruik /stoplinking om linken te stoppen')
            update.message.reply_text("Voer nu je ID in met getallen 0-9")
    except:
        update.message.reply_text('De invoer was niet correct. Probeer opnieuw \nOf gebruik /stoplinking om linken te stoppen')
        update.message.reply_text("Voer nu je ID in met getallen 0-9")
        print(linkingActive)
    
    
def stoplinking(bot, update):
    linkingActive.remove(update.message.chat_id)
    update.message.reply_text("linken gestopt \n om account te linken gebuik dan /link")
    
    
def vrij(bot, update):
    plaatsenVrij = 750
    #hier moet hij nog kunnen opvragen hoeveel plek er is
    update.message.reply_text(plaatsenVrij)
    
def answer(bot, update):
    if update.message.text == "hoi":
        update.message.reply_text("Hallo")
    elif update.message.text == "info":
        info(bot, update)
    elif update.message.text == "help":
        help(bot, update)
    else:
        update.message.reply_text("Hier kan ik niks mee probeer een van de opties")
        print(update.message.text)

def why(bot, update):
    update.message.reply_text('Deze bot is gemaakt voor HU door\nOlivier Verwoerd\nLars van Kleef\nYounes Bannany\nCody heij\nJelle Dekker')
def broadcast(bot, update):
    #zogd dat de admin berichten kan sturen naar alle gebruikers
    if update.message.chat_id == adminid:
        print("ADMIN")
        broadcastMessage = update.message.text[11:]
        update.message.reply_text('sending messages to all')
        for id in userlog:
            bot.sendMessage(chat_id=id, text=broadcastMessage)
    else:
        update.message.reply_text('Je hebt geen bevoegdheid tot het verzenden van Broadcast berichten')

def test(bot, update):
    #tijdelijk voor het proberen van diversen en het versturen van debug data
    print("Test")
    print(update)
    print(update.message.text)
    print(update.message.date)
    print(update.message.chat_id)
    print(update.message.chat)
    bot.sendMessage(19311809, "Test", reply_markup=ReplyKeyboardMarkup([["one", "two"], ["three", "four"]]))
    
    
def info(bot, update):
    update.message.reply_text('info is send')

    
    


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # bot token
    updater = Updater("")

    # dispatcher voor het registreren commandos
    dp = updater.dispatcher

    # commmand handeler - zorgd voor het verwijzen van een command naar een def
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("antwoordja", antwoordja))
    dp.add_handler(CommandHandler("why", why))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("broadcast", broadcast))
    dp.add_handler(CommandHandler("link", link))
    dp.add_handler(CommandHandler("stoplinking", stoplinking))
    dp.add_handler(CommandHandler("vrij", vrij))
    

    # zorgt voor het handelen van berichten
    dp.add_handler(MessageHandler(Filters.text, reply))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # zorgd dat control+c het script stopt,

    updater.idle()


if __name__ == '__main__':
    main()
