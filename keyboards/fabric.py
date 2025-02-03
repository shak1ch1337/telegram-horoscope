from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class Pagination(CallbackData, prefix = "pag"):
    action: str
    page: int


def paginator(sign_id: int = 1, page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text = "⬅️⬅️⬅️", callback_data = Pagination(action = "prev", page = page).pack()),
        InlineKeyboardButton(text = "➡️➡️➡️", callback_data = Pagination(action = "next", page = page).pack()),
        InlineKeyboardButton(text = "Выбрать", callback_data = f"activeSign_{sign_id}"),
        width = 2
    )
    return builder.as_markup()