import asyncio
from aiogram import Bot, Dispatcher, F

from config import TOKEN
from app.handlers import router
from app.database.models import async_main

#------------------------------------- Створення бота
# bot = Bot(TOKEN)
# dp = Dispatcher()
#-------------------------------------


    


#------------------------------------ Запуск бота
async def main():
    await async_main()
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__  == '__main__':
    print('Бот розпочав роботу')
    try:
        asyncio.run(main())  
    except KeyboardInterrupt:
        print('Бот вимкнуто')    