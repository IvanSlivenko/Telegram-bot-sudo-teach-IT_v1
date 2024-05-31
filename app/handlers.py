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
    await rq.set_user(message.from_user.id)  # -------додаємо користувача в базу данних
    await message.answer(
        f"Привіт : {message.from_user.first_name}", reply_markup=kb.main_keyboard
    )


# ------------------------------------------------ catch message
@router.message(F.text == "Технічні дії Дзюдо")
async def catalog(message: Message):
    await message.answer("Оберіть вид кидків", reply_markup=await kb.categories())


# ------------------------------------------------- catch callback
@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery):
    current_category_id = callback.data.split("_")[1]
    await callback.answer("Ви обрали вид кидків")
    await callback.message.answer(
        "Оберіть технічну дію", reply_markup=await kb.items(current_category_id)
    )


@router.callback_query(F.data.startswith("item_"))
async def item(callback: CallbackQuery):
    current_item_id = callback.data.split("_")[1]
    item_data = await rq.get_item(current_item_id)
    await callback.answer("Ви обрали технічну дію")
    await callback.message.answer(
        f"Назва : {item_data.name}\nОпис : {item_data.description}\nІмовірна оцінка : {item_data.price} ",
        reply_markup=await kb.to_main(),
    )


@router.callback_query(F.data.startswith("to_main"))
async def go_main(callback: CallbackQuery):
    await callback.answer("Ви повертаєтесь на головну")
    await callback.message.answer("Ви повернулись на головну",
        reply_markup=kb.main_keyboard)
