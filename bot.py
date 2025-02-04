import asyncio
from config_reader import config
from aiogram import Bot, Dispatcher
from data.database.models import migration
from data.database.db_requests_user import get_all_users
from data.database.db_requests_signs import get_one_sign
from handlers import commands_handler, messages_handler
from callbacks import pagination_callback
from utils.parser import parsing
from utils.messages_sending import sending
from apscheduler.schedulers.asyncio import AsyncIOScheduler


bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()
scheduler = AsyncIOScheduler()


dp.include_routers(
    commands_handler.router,
    messages_handler.router,
    pagination_callback.router
)


async def sending():
    users = await get_all_users()
    for user in users:
        if user[2] == 1:
            sign_info = await get_one_sign(user[1])
            await bot.send_message(user[0], f"{sign_info.sign_name}\n{sign_info.content}")



scheduler.add_job(parsing, "cron", hour=4, minute=0)
scheduler.add_job(sending, "cron", hour=17, minute=59)


async def main():

    # Launching functions when the bot is launched for the first time

    #await migration()
    
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
