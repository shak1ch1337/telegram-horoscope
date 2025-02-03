from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_one = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Выбрать знак"),
            KeyboardButton(text = "О боте")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)


start_two = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Изменить знак"),
            KeyboardButton(text = "О боте")
        ],
        [
            KeyboardButton(text = "Получить гороскоп"),
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)