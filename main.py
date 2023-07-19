from environs import Env                             # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter
from games.guess_the_number import guess_the_number
from games.rock_scissors_paper import rock_scissors_paper
from keyboards.set_menu import keyboard


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_id: int) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_id


env = Env()              # Создаем экземпляр класса Env
env.read_env()           # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

config = load_config('.env>')
admin_ids = env.int('admin_ids')   # Преобразуем значение переменной окружения к типу int
                                  # и сохраняем в переменной admin_id

# Создаем объекты бота и диспетчера
bot: Bot = Bot(config.tg_bot.token)
dp: Dispatcher = Dispatcher()


# Регистрируем роутеры в диспетчере
dp.include_router(guess_the_number.router1)
dp.include_router(rock_scissors_paper.router2)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
     await message.answer(text='Выбери игру:', reply_markup=keyboard)


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила ?')



if __name__ == '__main__':
    dp.run_polling(bot)
