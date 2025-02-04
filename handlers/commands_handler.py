from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import reply_kb
from data.database.db_requests_user import select_one_user, add_new_user, update_user_send_state
from data.database.db_requests_signs import get_one_sign
from data.message_answers import START_MESSAGE, ABOUT_BOT


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = await select_one_user(message.from_user.id)
    if user:
        sign = await get_one_sign(user.sign_id)
        if sign.sign_name.lower() == "нет знака":
            await message.answer(text = START_MESSAGE, reply_markup = reply_kb.start_one)
        else:
            await message.answer(text = START_MESSAGE, reply_markup = reply_kb.start_two)
    else:
        await add_new_user(message.from_user.id)
        await message.answer(text = START_MESSAGE, reply_markup = reply_kb.start_one)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text = ABOUT_BOT)


@router.message(Command("enable"))
async def cmd_enable(message: Message):
    user = await select_one_user(message.from_user.id)
    if user.send_state == 0:
        state = await update_user_send_state(message.from_user.id, 1)
        await message.answer(text = "Вы включили рассылку")
    else:
        await message.answer(text = "У вас уже включена рассылка")


@router.message(Command("disable"))
async def cmd_disable(message: Message):
    user = await select_one_user(message.from_user.id)
    if user.send_state == 1:
        state = await update_user_send_state(message.from_user.id, 0)
        await message.answer(text = "Вы отключили рассылку", reply_markup = reply_kb.start_two)
    else:
        await message.answer(text = "Вы не вкючали рассылку", reply_markup = reply_kb.start_two)