import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🚀 CodeGrokBot жұмыс істеп тұр!\n\nҚандай код жазып берейін?")

@dp.message()
async def handle(message: types.Message):
    text = message.text.strip()
    await message.answer("🤖 Код жазып жатырмын...\n\n" + f"Сұрауың: {text}\n\nКод генерацияланды (қазір қарапайым нұсқа)!")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
