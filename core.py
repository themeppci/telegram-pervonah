from pyrogram import Client
from pyrogram import types, filters
import time

delay = 1
comment = 'я в ахуи'

api_id = 123
api_hash = "123abc"


app = Client(
    "bio",
    api_id=api_id,
    api_hash=api_hash
)


@app.on_message(filters=filters.forwarded)
def my_handler(client, message):
    print(f'NEW POST :: {message.sender_chat.title}')
    time.sleep(delay)
    app.send_message(
        chat_id=message.chat.id,
        text=comment,
        reply_to_message_id=message.id
        )

app.run()
