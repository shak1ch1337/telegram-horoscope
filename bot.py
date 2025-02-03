import asyncio
from config_reader import config
from aiogram import Bot, Dispatcher
from data.database.models import migration
from handlers import commands_handler, messages_handler
from callbacks import pagination_callback
from utils.parser import parsing


async def main():
    #await migration()   # First start programm
    #await parsing()

    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(
        commands_handler.router,
        messages_handler.router,
        pagination_callback.router
    )

    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())