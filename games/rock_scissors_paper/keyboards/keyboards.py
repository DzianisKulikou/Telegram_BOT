from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from games.rock_scissors_paper.lexicon.lexicon_ru import lexicon_ru

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=lexicon_ru['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=lexicon_ru['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!". one_time_keyboard=True - сворачивает клавиатуру
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
                                            one_time_keyboard=True,
                                            resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=lexicon_ru['rock'])
button_2: KeyboardButton = KeyboardButton(text=lexicon_ru['scissors'])
button_3: KeyboardButton = KeyboardButton(text=lexicon_ru['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3]],
                                    resize_keyboard=True)
