from aiogram import Router, F
from aiogram.types import Message
from keyboards import fabric
from data.database.db_requests import select_one_user, get_one_sign, get_all_signs


router = Router()


@router.message(F.text.lower().in_(["выбрать знак", "изменить знак"]))
async def select_sign(message: Message):
    signs = await get_all_signs()
    await message.answer(text = f"{signs[0][1]}", reply_markup = fabric.paginator())


@router.message(F.text.lower() == "получить гороскоп")
async def send_horoscope(message: Message):
    user = await select_one_user(message.from_user.id)
    if user:
        sign_info = await get_one_sign(user.sign_id)
        await message.answer(text = f"{sign_info.sign_name}\n{sign_info.content}")
    else:
        print("error")