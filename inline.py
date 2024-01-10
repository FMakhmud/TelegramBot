from config import TOKEN
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
num = 1


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    buttons = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="+", callback_data="+")
    button2 = InlineKeyboardButton(text="-", callback_data="-")
    buttons.add(button1, button2)
    await message.answer(text=f"Salom Tilni tanla, {num}", reply_markup=buttons)


@dp.callback_query_handler()
async def callback_function(callback: types.CallbackQuery):
    global num
    if callback.data == "+":
        num += 1
    elif callback.data == "-":
        num -= 1
    buttons = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="+", callback_data="+")
    button2 = InlineKeyboardButton(text="-", callback_data="-")
    buttons.add(button1, button2)
    await callback.message.edit_text(
        text=f"Salom Tilni tanla, {num}",
        reply_markup=buttons)


async def on_startup(_):
    print("-__-")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
