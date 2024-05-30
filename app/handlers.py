
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, or_f
from aiogram.fsm.context import FSMContext

from app import keyboards
from states.states import Register


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привіт : {message.from_user.first_name}', reply_markup=keyboards.main_keyboard)
#     # await message.reply('Як справи')


@router.message(or_f(
                    (F.text == 'Технічні дії'),
                ))
async def kb_catalog(message: Message):
    await message.answer('Оберіть розділ', reply_markup=keyboards.catalog)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name} ви натиснули на кнопку -  "Допомога"')    

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)#------------------------ стаємо в state = name
    await message.answer("Вкажіть ваше ім'я")

@router.message(Register.name)#------------------------ перевіряємо чи state = name
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)#---Зберігаємо текст повідомлення в state під ключем name
    await state.set_state(Register.age)#------------------------ стаємо в state = age
    await message.answer("Вкажіть ваш вік")

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Вкажіть ваш номер телефону",reply_markup=keyboards.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше ім'я :{data["name"]}\n\
                            Ваш вік : {data["age"]}\n\
                            Ваш номер телефону : {data["number"]}")
    
    await state.clear()#--------------------------- очищаємо state
        
        









@router.callback_query(F.data == 'wrestling in the rack')
async def the_rack(callback: CallbackQuery):
    await callback.answer('Ви обрали розділ', show_alert=True)
    await  callback.message.answer(f'Ви обрали розділ : Боротьба у стійці')
  

@router.callback_query(F.data == 'wrestling on the ground floor')
async def the_rack(callback: CallbackQuery):
    await callback.answer('Ви обрали розділ', show_alert=True)
    await  callback.message.answer(f'Ви обрали розділ : Боротьба у партері')    

