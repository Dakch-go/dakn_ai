import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Token Railway-дан алады
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🚀 **CodeGrokBot** Cloud-та жұмыс істеп тұр!\n\n"
        "Қандай код жазып берейін?\n\n"
        "Мысалдар:\n"
        "• Flask сайт жаса\n"
        "• Telegram бот жаз\n"
        "• Python ToDo list\n"
        "• Калькулятор\n"
        "• React компонент"
    )

@dp.message()
async def generate(message: types.Message):
    user_text = message.text

    await message.answer("🤖 Grok код жазып жатыр...")

    # Қарапайым код генерациясы
    response_code = f"""# CodeGrokBot - {user_text}
# Generated in Cloud

print("✅ Сенің сұрауың: {user_text}")
print("Cloud Pro-да жұмыс істеп тұрмын! 🔥\\n")

# Негізгі код
def main():
    print("Бұл жерге толық код келеді.")
    print("Мысал: Hello, World!")

if __name__ == "__main__":
    main()
"""

    # generated_code.py файлына сақтайды
    with open("generated_code.py", "w", encoding="utf-8") as f:
        f.write(response_code)

    await message.answer(
        f"✅ **Код дайын!**\n\n"
        f"📁 `generated_code.py` сақталды\n\n"
        f"```python\n{response_code[:600]}...\n```"
    )

# Ботты іске қосу
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
