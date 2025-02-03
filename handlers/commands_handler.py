from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import reply_kb
from data.database.db_requests import select_one_user, add_new_user, get_one_sign


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = await select_one_user(message.from_user.id)
    if user:
        sign = await get_one_sign(user.sign_id)
        if sign.sign_name.lower() == "нет знака":
            await message.answer(text = "Hello", reply_markup = reply_kb.start_one)
        else:
            await message.answer(text = "Hello", reply_markup = reply_kb.start_two)
    else:
        await add_new_user(message.from_user.id)
        await message.answer(text = "Welcome", reply_markup = reply_kb.start_one)



@router.message(Command("help"))
async def cmd_help(message: Message):
    pass


@router.message(Command("enable"))
async def cmd_enable(message: Message):
    pass


@router.message(Command("disable"))
async def cmd_disable(message: Message):
    pass