from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Угадай число')
button_2: KeyboardButton = KeyboardButton(text='Камень, ножницы, бумага')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)

