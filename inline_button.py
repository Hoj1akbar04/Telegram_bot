from aiogram import types
from main import Database


def create_prem_keyboard():
    prem_names_keyboard = types.InlineKeyboardMarkup()
    query = "SELECT name FROM premyera;"
    premiere_names = Database.connect(query, "select")
    for premiere_name in premiere_names:
        button = types.InlineKeyboardButton(text=premiere_name[0], callback_data=f"prem_{premiere_name[0]}")
        prem_names_keyboard.add(button)

    return prem_names_keyboard


def create_serial_keyboard():
    serial_names_keyboard = types.InlineKeyboardMarkup()
    query = "SELECT name FROM serial;"

    ser_names = Database.connect(query, "select")
    for ser_name in ser_names:
        button = types.InlineKeyboardButton(text=ser_name[0], callback_data=f"ser_{ser_name[0]}")
        serial_names_keyboard.add(button)

    return serial_names_keyboard


def create_cartoon_keyboard():
    cartoon_names_keyboard = types.InlineKeyboardMarkup()
    query = "SELECT name FROM cartoon;"
    cartoon_names = Database.connect(query, "select")
    for cartoon_name in cartoon_names:
        button = types.InlineKeyboardButton(text=cartoon_name[0], callback_data=f"cartoon_{cartoon_name[0]}")
        cartoon_names_keyboard.add(button)

    return cartoon_names_keyboard


def create_movie_keyboard():
    movie_names_keyboard = types.InlineKeyboardMarkup()
    query = "SELECT name FROM movie;"
    movie_names = Database.connect(query, "select")
    for movie_name in movie_names:
        button = types.InlineKeyboardButton(text=movie_name[0], callback_data=f"movie_{movie_name[0]}")
        movie_names_keyboard.add(button)

    return movie_names_keyboard


def create_admin_keyboard():
    admin_keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Info premyera", callback_data="admin")
    button2 = types.InlineKeyboardButton(text="Info serial", callback_data="admin")
    button3 = types.InlineKeyboardButton(text="Info movie", callback_data="admin")
    button4 = types.InlineKeyboardButton(text="Info multfilm", callback_data="admin")
    admin_keyboard.add(button1, button2, button3, button4)
    return admin_keyboard
