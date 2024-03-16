import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from inline_button import *

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

current_section = {}


@dp.message_handler(lambda message: message.text == "🔥 Premyera 🔥")
async def show_prem(message: types.Message):
    prem_names_keyboard = create_prem_keyboard()
    await message.answer("Premyeralardan birini tanlang:", reply_markup=prem_names_keyboard)
    current_section[message.chat.id] = "premyera"


@dp.callback_query_handler(lambda callback_query: callback_query.data == "back")
async def back_button_handler(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    section = current_section.get(chat_id)

    if section == "premiere":
        prem_names_keyboard = create_prem_keyboard()
        await callback_query.message.answer("Premyeralardan birini tanlang:", reply_markup=prem_names_keyboard)
    if section == "serial":
        serial_names_keyboard = create_serial_keyboard()
        await callback_query.message.answer("Seriallardan birini tanlang:", reply_markup=serial_names_keyboard)

    if section == "movie":
        movie_names_keyboard = create_movie_keyboard()
        await callback_query.message.answer("Kinolardan birini tanlang:", reply_markup=movie_names_keyboard)

    if section == "cartoon":
        cartoon_names_keyboard = create_cartoon_keyboard()
        await callback_query.message.answer("Multfillardan birini tanlang:", reply_markup=cartoon_names_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('prem_'))
async def data_premiere(callback_query: types.CallbackQuery):
    prem_name = callback_query.data.split('_')[1]
    query = f"SELECT photo_url, continue_prem, create_country FROM premyera WHERE name = '{prem_name}';"
    prem_info = Database.connect(query, "select")

    if prem_info:
        photo_url, continue_prem, create_country = prem_info[0]
        message_text = f"{prem_name}\nContinue: {continue_prem}\nCountry: {create_country}"

        back_button = types.InlineKeyboardButton(text="🔙 Back", callback_data="back")
        back_keyboard = types.InlineKeyboardMarkup().add(back_button)

        await bot.send_photo(callback_query.message.chat.id, photo=photo_url, caption=message_text,
                             reply_markup=back_keyboard)
        current_section[callback_query.message.chat.id] = "premiere"

    else:
        await callback_query.message.answer("Ma'lumot topilmadi")


@dp.message_handler(lambda message: message.text == "🔥 Serial 🔥")
async def show_serial(message: types.Message):
    serial_names_keyboard = create_serial_keyboard()
    await message.answer("Seriallardan birini tanlang:", reply_markup=serial_names_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('ser_'))
async def data_ser(callback_query: types.CallbackQuery):
    ser_name = callback_query.data.split('_')[1]
    query = f"SELECT photo_url, continue_prem, create_country, serial_part FROM serial WHERE name = '{ser_name}';"
    ser_info = Database.connect(query, "select")

    if ser_info:
        photo_url, continue_prem, create_country, serial_part = ser_info[0]
        message_text = f"{ser_name}\nContinue: {continue_prem}\nCountry: {create_country}\nQismlar soni: {serial_part}"

        back_button = types.InlineKeyboardButton(text="🔙 Back", callback_data="back")
        back_keyboard = types.InlineKeyboardMarkup().add(back_button)

        await bot.send_photo(callback_query.message.chat.id, photo=photo_url, caption=message_text,
                             reply_markup=back_keyboard)
        current_section[callback_query.message.chat.id] = "serial"

    else:
        await callback_query.message.answer("Ma'lumot topilmadi")


@dp.message_handler(lambda message: message.text == "🔥 Kinolar 🔥")
async def show_movie(message: types.Message):
    movie_names_keyboard = create_movie_keyboard()
    await message.answer("Kinolardan birini tanlang:", reply_markup=movie_names_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('movie_'))
async def data_movie(callback_query: types.CallbackQuery):
    movie_name = callback_query.data.split('_')[1]
    query = f"SELECT photo_url, continue_prem, create_country FROM movie WHERE name = '{movie_name}';"
    movie_info = Database.connect(query, "select")

    if movie_info:
        photo_url, continue_prem, create_country = movie_info[0]
        message_text = f"{movie_name}\nContinue: {continue_prem}\nCountry: {create_country}"

        back_button = types.InlineKeyboardButton(text="🔙 Back", callback_data="back")
        back_keyboard = types.InlineKeyboardMarkup().add(back_button)

        await bot.send_photo(callback_query.message.chat.id, photo=photo_url, caption=message_text,
                             reply_markup=back_keyboard)
        current_section[callback_query.message.chat.id] = "movie"

    else:
        await callback_query.message.answer("Ma'lumot topilmadi")


@dp.message_handler(lambda message: message.text == "🔥 Multfilm 🔥")
async def show_cartoon(message: types.Message):
    cartoon_names_keyboard = create_cartoon_keyboard()
    await message.answer("Multfilmlardan birini tanlang:", reply_markup=cartoon_names_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cartoon_'))
async def data_cartoon(callback_query: types.CallbackQuery):
    cartoon_name = callback_query.data.split('_')[1]
    query = f"SELECT photo_url, continue_prem, create_country FROM cartoon WHERE name = '{cartoon_name}';"
    cartoon_info = Database.connect(query, "select")

    if cartoon_info:
        photo_url, continue_prem, create_country = cartoon_info[0]
        message_text = f"{cartoon_name}\nContinue: {continue_prem}\nCountry: {create_country}"

        back_button = types.InlineKeyboardButton(text="🔙 Back", callback_data="back")
        back_keyboard = types.InlineKeyboardMarkup().add(back_button)

        await bot.send_photo(callback_query.message.chat.id, photo=photo_url, caption=message_text,
                             reply_markup=back_keyboard)
        current_section[callback_query.message.chat.id] = "cartoon"

    else:
        await callback_query.message.answer("Ma'lumot topilmadi")


@dp.message_handler(commands=['send_image'])
async def send_image(message: types.Message):
    photo_url = 'https://kuda-mo.ru/uploads/2a16d60edcbd9ef63623d6a7c36ef2f6.jpg'
    caption = 'Sizning rasmingiz'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)


@dp.message_handler(commands=['admin'])
async def admin_command(message: types.Message):
    photo_url = ('https://kartinki.pibig.info/uploads/posts/2023-04/1682457797_kartinki-pibig-info-p-adminka-kartinka-'
                 'arti-krasivo-1.jpg')
    caption = 'Admin account'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)
    if message.from_user.id in [2074717977]:
        await message.reply("Hello admin👋")
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)