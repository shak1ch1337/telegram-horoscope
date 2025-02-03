from aiogram import Router, F
from aiogram.types import CallbackQuery
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from keyboards import fabric, reply_kb
from data.database.db_requests import get_all_signs, update_user_sign


router = Router()


@router.callback_query(fabric.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabric.Pagination):
    signs = await get_all_signs()
    page_num = int(callback_data.page)
    if callback_data.action == "prev":
        page = page_num - 1 if page_num > 0 else 0
    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(signs) - 1) else 0
    with suppress(TelegramBadRequest):
        await call.message.edit_text(text = f"{signs[page][1]}", reply_markup = fabric.paginator(signs[page][0], page))
        await call.answer()


@router.callback_query(F.data.startswith("activeSign"))
async def selected_sign(call: CallbackQuery):
    sign_id = call.data.split("_")[1]
    result = await update_user_sign(call.from_user.id, sign_id)
    if result:
        await call.message.answer(text = "Знак Зодиака изменен", reply_markup = reply_kb.start_two)
        await call.answer()
    else:
        await call.message.answer(text = "Error")
        await call.answer()