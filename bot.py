from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

app = Client("my_bot",

api_id= int(os.environ.get("APP_ID"))
api_hash= os.environ.get("API_HASH")
bot_token=os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

@app.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(results=[
        InlineQueryResultArticle(
            title="Installation",
            input_message_content=InputTextMessageContent(
                "Here's how to install **Pyrogram**"),
            url="https://docs.pyrogram.org/intro/install",
            description="How to install Pyrogram",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "Open website",
                    url="https://docs.pyrogram.org/intro/install")
            ]])),
        InlineQueryResultArticle(
            title="Usage",
            input_message_content=InputTextMessageContent(
                "Here's how to use **Pyrogram**"),
            url="https://docs.pyrogram.org/start/invoking",
            description="How to use Pyrogram",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "Open website",
                    url="https://docs.pyrogram.org/start/invoking")
            ]]))
    ],
                              cache_time=1)


app.run()  # Automatically start() and idle()
