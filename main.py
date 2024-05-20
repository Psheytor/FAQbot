import asyncio
from aiogram import Bot, Dispatcher
import menu
from handlers import answer, map
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()
async def main():
    dp.include_routers( menu.router, answer.router, map.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
