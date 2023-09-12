from pyrogram import Client
from pyrogram import types, filters
import time
import random
import telebot
import pickle
import os


try: os.system('clear')
except: None
try: os.system('cls')
except: None

global comments
global user_chat_id
global is_working

# SETTINGS

delay = 1
comments = ['comment1', 'comment2', 'comment3'] # list of comments to be randomly chosen 
api_id = 123  # api id from my.telegram.org/auth
api_hash = "abc"   # api hash from my.telegram.org/auth
bot_api_hash = "123:abc"  # bot api hash from BotFather in telegram

# SETTINGS


no_pkl = False

# load user_chat_id var from pickle file
try:
    with open('data.pkl', 'rb') as f:
        user_chat_id = pickle.load(f)
    
    if user_chat_id == '' or user_chat_id == None:
        no_pkl = True
except:
    no_pkl = True

try:
    bot = telebot.TeleBot(bot_api_hash) # telegram bot client
except Exception as e:
    print(f'Exception  occured: {e}.\n\n[!] Check your bot token')
    time.sleep(10)
    exit(1)


if no_pkl:
    print('Getting your user chat id through telegram bot...')
    print('[!] Send \"/start\" to your bot')
    @bot.message_handler(commands=['start'])
    def start(message):
        print(f'Your user chat id is: {message.chat.id}')

        print('Saving to pkl file...')
        with open('data.pkl', 'wb') as f:
            pickle.dump(message.chat.id, f)

        print('Saved your chat id to pkl file, restart program')
        time.sleep(5)
        exit(0)

    bot.infinity_polling()


print('[#] Successfully loaded your chat.id from pkl file, starting...')



app = Client(   # telegram user client
    "bio",
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters=filters.forwarded)
def my_handler(client, message):
    random_comment = random.choice(comments)
    time.sleep(delay)

    try:
        app.send_message(
            chat_id=message.chat.id,
            text=random_comment,
            reply_to_message_id=message.id
            )
        result = f'Sent: {random_comment}\n\nTo: {message.sender_chat.title}'
    except Exception as x:
        result = f'Error occured:\n\n{x}\n\n\n[!] Bot stopped'
        bot.send_message(user_chat_id, result)
        input('Bot stopped due to error, press any key to skip and continue')


    bot.send_message(user_chat_id, result)

bot.send_message(user_chat_id, 'Waiting for new posts in channels...')
print('Started')
app.run()
