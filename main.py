from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def greetings(message: types.Message):
    user = types.User.get_current()
    user_name = user['first_name']

    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="/help")
    button2 = KeyboardButton(text="/start")
    button3 = KeyboardButton(text="/pictures")
    button4 = KeyboardButton(text="/random_pictures")
    buttons.add(button1, button2, button4)
    buttons.add(button3)
    print(message.chat.id)

    await message.answer(f"Hello {user_name}!", reply_markup=buttons)


@dp.message_handler(commands=["help"])
async def get_instructions(message: types.Message):
    await message.answer(text="This bot get instructions about telegram")


@dp.message_handler(commands=['pictures'])
async def get_picture(message: types.Message):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="YES")
    button2 = KeyboardButton(text="NO")
    buttons.add(button1, button2)

    await bot.send_photo(chat_id=204396345,
                         photo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Hopetoun_falls.jpg/800px-Hopetoun_falls.jpg",
                         caption="Fresh!",
                         reply_markup=buttons)


@dp.message_handler(commands=["/random_pictures"])
async def get_random_images(message: types.Message):
    images = ["https://www.treehugger.com/natural-capital-and-natural-income-definition-and-examples-5186759",
              "https://media.geeksforgeeks.org/wp-content/uploads/20231103155807/Natural-Environment.webp",
              "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/24701-nature-natural-beauty.jpg/1280px-24701-nature-natural-beauty.jpg",
              "https://i.insider.com/5b5b8ad97708e9149c3e0555?width=1000&format=jpeg&auto=webp"]
    random_num = random.choice(images)
    await bot.send_photo(chat_id=message.chat.id, photo=random_num)


async def on_startup(_):
    print("-__-")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
