from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🚀 **CodeGrokBot** дайын!\n\n"
        "Қандай код жазып берейін?\n"
        "Мысал: Flask сайт, Telegram бот, ToDo list, ойын т.б."
    )

@dp.message()
async def handle(message: types.Message):
    text = message.text.strip()

    await message.answer("🤖 Код жазып жатырмын...")

    code = f'''# CodeGrokBot generated
# Сұрау: {text}

print("✅ {text} дайын!")
print("Cloud-та жұмыс істеп тұр 🔥")

# Кодтың қалған бөлігі осында
'''

    with open("generated_code.py", "w", encoding="utf-8") as f:
        f.write(code)

    await message.answer(f"✅ Код сақталды!\nФайл: `generated_code.py`")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
