
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, or_f
from aiogram.fsm.context import FSMContext

from app import keyboards as kb
from states.states import Register
import app.database.requests as rq



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)#-------додаємо користувача в базу данних
    await message.answer(f'Привіт : {message.from_user.first_name}', 
                         reply_markup=kb.main_keyboard)


#------------------------------------------------ catch message        
@router.message(F.text == 'Технічні дії')
async def catalog(message: Message):
    await message.answer('Оберіть розділ', reply_markup= await kb.categories())

#------------------------------------------------- catch callback
@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    current_category_id = callback.data.split('_')[1]
    await callback.answer('Ви обрали розділ')
    await callback.message.answer('Оберіть технічну дію', 
                                  reply_markup= await kb.items(current_category_id))



