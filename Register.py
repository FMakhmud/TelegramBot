from aiogram import Bot, types, Dispatcher, executor
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class Register(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    phone_number = State()
    location = State()


@dp.message_handler(commands=["start"])
async def get_register(message: types.Message):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="/register")
    buttons.add(button1)

    await message.answer(text="/register knopkasini bosing",
                         reply_markup=buttons)


@dp.message_handler(commands=["register"])
async def start_register(message: types.Message):
    await message.answer(text="Ismingizni kiriting")
    await Register.first_name.set()


@dp.message_handler(state=Register.first_name)
async def set_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer(text="Familiyangizni kiriting")
    await Register.next()


@dp.message_handler(state=Register.last_name)
async def set_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Yoshingizni kiriting")
    await Register.next()


@dp.message_handler(state=Register.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Share a number", request_contact=True)
    buttons.add(button)

    await message.answer(text="Telefoningizni kiriting", reply_markup=buttons)
    await Register.next()


@dp.message_handler(content_types=['phone_number'], state=Register.phone_number)
async def set_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact)

    buttons1 = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="Location", request_location=True)
    buttons1.add(button1)

    await message.answer("Send location", reply_markup=buttons1)
    await Register.next()


@dp.message_handler(content_types=['location'], state=Register.location)
async def set_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.location)

    data = await state.get_data()
    inform = f"{data['first_name']}, {data['last_name']}, {data['age']}, {data['phone_number']}"
    await bot.send_location(chat_id=message.chat.id, latitude=data['location'].latitude,
                            longitude=data['location'].longitude)
    await bot.send_contact(chat_id=message.chat.id, phone_number=data['phone_number'])

    await message.answer(text=inform)
    await state.finish()


async def on_startup(_):
    print("-__-")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
