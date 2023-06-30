from bot_token import bot_token
from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # чтобы фильтровать апдейты по наличию в них команд (начинающихся со знака "/")
from aiogram.types import Message  # Апдейты этого типа мы будем ловить эхо-ботом

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = bot_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
print('Я ЖИВ!')


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Инструкция выполнится, если файл с программой будет исполняемым, то есть точкой входа в бот. А если этот файл будет
# использован в качестве модуля для какого-то другого проекта, то инструкция выполняться не будет.
if __name__ == '__main__':
    dp.run_polling(bot)  # Запускает поллинг, то есть постоянный опрос сервера Telegram на наличие апдейтов для бота.
                         # В качестве аргумента в метод диспетчера run_polling нужно передать объект бота.
