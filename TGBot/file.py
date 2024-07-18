from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor
import asyncio
from datetime import datetime
import config
import random

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
days = 0
time = '00:00:00'
inline_btn_1 = types.InlineKeyboardButton(config.NAME, url=config.URL)
inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full = types.InlineKeyboardMarkup(row_width=2).add(inline_btn_1)

with open('settings.txt', 'r') as file:
    data = file.read()
    if not data:
        days = int(input('days: '))
        time = input('time in hh:mm:ss: ')
    else:
        days, time = data.split()

with open('settings.txt', 'w') as file:
    file.write(f'{days} {time}')


@dp.message_handler(commands=['start'])
async def command_start(message):
    global days
    while True:
        await asyncio.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == time:
            days += 1
            await bot.send_message(message.chat.id, f'{random.choice(config.PHRASES)} {str(days)}')


@dp.message_handler(commands=['get_link'])
async def get_link(message):
    await bot.send_message(message.chat.id, 'CLICK ON THIS LINK', reply_markup=inline_kb1)


executor.start_polling(dp, skip_updates=True)
