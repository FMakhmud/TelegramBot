from aiogram import Bot, types, Dispatcher, executor
from integrations import get_weather_data

bot = Bot("5677756493:AAFxIsGxpmF4h8nabX_cdX6xx4hNDkwLpz0")
dp = Dispatcher(bot=bot)


# async def is_subscribe(user_id):
#     chat_id = "https://t.me/road_to_the_dream1"
#     try:
#         member = await bot.get_chat_member(chat_id, int(user_id))
#         if member.status == types.ChatMemberStatus.MEMBER or member.status == types.ChatMemberStatus.CREATOR:
#             return True
#     except Exception as e:
#         return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # if await is_subscribe(message.chat.id):
     await message.answer(text="🌆Name the city you want to know")
    # await message.answer("Botimizadan foydalan oylmaysiz")


@dp.message_handler()
async def weather_city(message: types.Message):
    city = message.text
    text = get_weather_data(city)
    await message.answer(text, parse_mode="HTML")

async def on_startup(_):
    print("-__-")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
