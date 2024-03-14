import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


from bot_button import *
from main import Database

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)

    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        await message.answer(f"Hello👋 @{username}", reply_markup=menu_button)

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        await message.answer(f"Hello👋 @{username}", reply_markup=menu_button)


@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Hello👋  @{data[0][3]}

        First Name: {data[0][1]}
        Last Name: {data[0][2]}
        Chat ID: {data[0][4]}
        Create Date: {data[0][5]}
        """)


@dp.message_handler(lambda message: message.text == "◾️ Premyera ◾️️")
async def show_prem(message: types.Message):
    await message.answer("Premyeralardan birini tanlang:", reply_markup=prem_button)


@dp.message_handler(lambda message: message.text == "◾️ Serial◾️ ")
async def show_ser(message: types.Message):
    await message.answer("Seriallardan birini tanlang:", reply_markup=ser_button)


@dp.message_handler(lambda message: message.text == "◾️ Kinolar ◾️")
async def show_movie(message: types.Message):
    await message.answer("Kinolardan birini tanlang:", reply_markup=movie_button)


@dp.message_handler(lambda message: message.text == "◾️ Multfilm ◾️")
async def show_cartoon(message: types.Message):
    await message.answer("Multfilmlardan birini tanlang:", reply_markup=cartoon_button)


@dp.message_handler(lambda message: message.text == "🔙")
async def back(message: types.Message):
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=menu_button)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)