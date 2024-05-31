from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Технічні дії")],
        [KeyboardButton(text="Розклад")],
        [KeyboardButton(text="Контакти"), KeyboardButton(text="Про нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Що вас зацікавило ?",
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Боротьба у стійці", callback_data="wrestling in the rack"
            )
        ],
        [
            InlineKeyboardButton(
                text="Боротьба у партері", callback_data="wrestling on the ground floor"
            )
        ],
    ]
)

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Відправити номер", request_contact=True)]
    ],
    resize_keyboard=True,
    input_field_placeholder="Для відправки номера телефону натисніть на цю кнопку 👇",
)