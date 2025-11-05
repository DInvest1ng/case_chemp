from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router, types
from . import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте, уважаемые члены жюри. Вас приветсвуте команда 'Кофе, Кола, MVP', номер команды 1979. С чем бы вы хотели ознакомится?",
        reply_markup=kb.main_keyboard,
    )

@router.callback_query(F.data == "finance")
async def cmd_start(callback: CallbackQuery):
    await callback.message.answer(
        f"Ознакомится с финансами вы можете по этой ссылке https://docs.google.com/spreadsheets/d/1JvBXwL3f5_X-j_O8IeRddz9zy9e5fvzhys3Ra7kTPaA/edit?gid=0#gid=0",
        reply_markup=kb.back_keyboard,
    )
    await callback.answer()

