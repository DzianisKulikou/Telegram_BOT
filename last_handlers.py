from aiogram import Router
from aiogram.types import Message
from games.guess_the_number.guess_the_number import users


router100: Router = Router()


# Этот хэндлер будет срабатывать на остальные любые сообщения
@router100.message()
async def process_other_text_answers(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Не отвлекайтесь пожалуйста)')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')
