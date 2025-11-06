from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Финансы 💰"),
            KeyboardButton(text="Инициативы 💡"),
        ],
        [
            KeyboardButton(text="О команде 👥"),
            KeyboardButton(text="Инициатива 3 🚀"),
        ],
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)

back_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="⏪ Назад")]],
    one_time_keyboard=True,
    resize_keyboard=True,
)
