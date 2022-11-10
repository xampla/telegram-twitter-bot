from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters

import tweepy
import time
import logging

#TELEGRAM
TELE_TOKEN = "CHANGE_ME"
channel_name = "CHANGE_ME"

#TWITTER
BEARER_TOKEN = "CHANGE_ME"
CONSUMER_TOKEN_KEY = "CHANGE_ME"
CONSUMER_SECRET = "CHANGE_ME"
ACCESS_TOKEN = "CHANGE_ME"
ACCESS_TOKEN_SECRET = "CHANGE_ME"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#-------------------------------TWITTER-------------------------------------------

client = tweepy.Client(
    consumer_key=CONSUMER_TOKEN_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

#---------------------------------------------------------------------------------

#-------------------------------TELEGRAM------------------------------------------
updater= Updater(token=TELE_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    print(update.channel_post.sender_chat.username)
    if update.channel_post.sender_chat.username == channel_name:
        print(update.channel_post.text)
        response = client.create_tweet(text=update.channel_post.text)
        print(f"https://twitter.com/user/status/{response.data['id']}")
        #context.bot.send_message(chat_id=update.effective_chat.id, text=update.channel_post.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
#---------------------------------------------------------------------------------
