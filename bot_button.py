from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main import Database

menu_button = ReplyKeyboardMarkup([
    [KeyboardButton("Premyera"), KeyboardButton("Kinolar")],
    [KeyboardButton("Serial"), KeyboardButton("Multfilm")],
], resize_keyboard=True)


prem_button = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM premyera"
for i in Database.connect(query, "select"):
    prem_button.add(KeyboardButton(i[1]))
prem_button.add(KeyboardButton("Back"))


ser_button = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM serial"
for i in Database.connect(query, "select"):
    ser_button.add(KeyboardButton(i[1]))
ser_button.add(KeyboardButton("Back"))


movie_button = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM movie"
for i in Database.connect(query, "select"):
    movie_button.add(KeyboardButton(i[1]))
movie_button.add(KeyboardButton("Back"))


cartoon_button = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM cartoon"
for i in Database.connect(query, "select"):
    cartoon_button.add(KeyboardButton(i[1]))
cartoon_button.add(KeyboardButton("Back"))

