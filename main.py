from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.filters import CommandStart
import functions
import states
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message("admin_id", "Bot Ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message("admin_id", "Bot ishdan to'xtadi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(functions.start_command_answer, CommandStart())
    dp.message.register(functions.get_user_name_answer, states.get_user_name.name)
    dp.message.register(functions.get_ref_link_answer, F.text == "Referal havola")
    dp.message.register(functions.get_user_ball_answer, F.text == "Mening ballarim")
    dp.shutdown.register(shutdown_answer)
    bot = Bot("bot_token")
    await dp.start_polling(bot)

run(start())
