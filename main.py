import asyncio
import random
from aiogram import Bot, Dispatcher, types

TOKEN = "7913481753:AAFJOpahLdc64uyO7Uqj4e7aVJmPKcH6C7w"

bot = Bot(token=TOKEN)
dp = Dispatcher()

negative_responses = [
  "Да, все пошло по пизде!"
  "Я тоже охуел братан..."
  "Сдаемся, все...конец"
  "Да ну его, у меня перегрев"
]

positive_responses = [
  "Ты че бля"
  "Жалоба молитва дьяволу"
  "Далин блядь, сильный тот не то кто не падает, а тот кто встает"
  "СИЛЬНЕЕЕ!"
  "Я Дэзмонд, тебе пизда)"
]

@dp.message()
async def handle_message(message: types.Message):
  text = message.text
   
  if any(word in text for word in ["Плохо", "Сдаюсь", "Устал", "Пиздец"]):
    response = random.choice(negative_responses)
  elif any(word in text for word in ["Мы справимся", "Заебись все", "Та ты заебешь"]):
    response - random.choice(positive_responses)
  else:
    response = "Нормально, мы тут"

  await message.answer(response)

async def main():
  print("Погнали")
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())

import asyncio

async def keep_alive():
  while True:
    await asyncio.sleep(3600)

asincio.create_task(keep_alive())
