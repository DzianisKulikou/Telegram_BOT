from environs import Env  # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from aiogram import Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, BaseFilter
from games.guess_the_number import guess_the_number
from games.rock_scissors_paper.handlers import user_handlers
import last_handlers
from keyboards.set_menu import keyboard
from lexicon.lexicon_ru import lexicon_ru

router: Router = Router()


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_id: int) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_id


env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

config = load_config('.env>')
admin_ids = env.int('admin_ids')  # Преобразуем значение переменной окружения к типу int
# и сохраняем в переменной admin_id

# Создаем объекты бота и диспетчера
bot: Bot = Bot(config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()

# Регистрируем роутеры в диспетчере
dp.include_router(router)
dp.include_router(guess_the_number.router1)
dp.include_router(user_handlers.router2)
dp.include_router(last_handlers.router100)


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запусти меня с начала!'),
        BotCommand(command='/help',
                   description='Справка по работе бота!'),
        BotCommand(command='/cancel',
                   description='Выйти из игры в стартовое меню!')]

    await bot.set_my_commands(main_menu_commands)


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text='Выбери игру:', reply_markup=keyboard,
                         input_field_placeholder='Разверните клавиатуру снизу!')

# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_ru['/help'])


if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)
