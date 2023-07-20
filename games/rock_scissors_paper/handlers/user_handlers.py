from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message
from games.rock_scissors_paper.keyboards.keyboards import game_kb, yes_no_kb
from games.rock_scissors_paper.lexicon.lexicon_ru import lexicon_ru
from games.rock_scissors_paper.services.services import get_bot_choice, get_winner
from keyboards.set_menu import keyboard

router2: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router2.message(Text(text='Камень, ножницы, бумага'))
async def process_start_command(message: Message):
    await message.answer(text=lexicon_ru['start_rsp'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router2.message(Text(text=lexicon_ru['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=lexicon_ru['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router2.message(Text(text=lexicon_ru['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=lexicon_ru['no'])
    await message.answer(text='Выбери игру:', reply_markup=keyboard)


# Этот хэндлер срабатывает на любую из игровых кнопок
@router2.message(Text(text=[lexicon_ru['rock'],
                            lexicon_ru['paper'],
                            lexicon_ru['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{lexicon_ru["bot_choice"]} '
                              f'- {lexicon_ru[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=lexicon_ru[winner], reply_markup=yes_no_kb)
