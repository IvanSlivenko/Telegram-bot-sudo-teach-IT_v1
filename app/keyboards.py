from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from app.database.requests import get_categories, get_category_item
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Технічні дії")],
        [KeyboardButton(text="Розклад")],
        [KeyboardButton(text="Контакти"), KeyboardButton(text="Про нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Що вас зацікавило ?",
)

async def categories():
    all_categories = await get_categories()
    kb_categories = InlineKeyboardBuilder()
    
    for category in all_categories:
        kb_categories.add(InlineKeyboardButton(text=category.name, 
                                               callback_data=f"category_{category.id}"))
    kb_categories.add(InlineKeyboardButton(text='На головну',
                                           callback_data='to_main'))
    return kb_categories.adjust(2).as_markup()#----------------------------------adjust(2) -  

async def items(category_id):
    all_items = await get_category_item(category_id)
    kb_items = InlineKeyboardBuilder()
    
    for item in all_items:
        kb_items.add(InlineKeyboardButton(text=f'{item.name}', 
                                               callback_data=f'{item.id}'))
    kb_items.add(InlineKeyboardButton(text='На головну',
                                           callback_data='to_main'))
    return kb_items.adjust(2).as_markup()#----------------------------------adjust(2) -  

    