from aiogram.filters import Command
from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


router = Router()
builder = InlineKeyboardBuilder()
builder.add(types.InlineKeyboardButton(text="Карта корпусов",callback_data='map'))
@router.message(Command("start"))
async def cmd_start(message:types.Message):
   await message.answer(
        "Здравствуй, абитуриет, тебя приветствует FAQ бот от ОмГТУ, который ответит на твои вопросы! Для начала выбери тему из списка:"
        "\n1. Обучение\n2. Стипендия и другие виды поддержки\n3. Для иностранных студентов\n4. Общежитие\n5. Оплата услуг\n"
        "6. Внеучебная деятельность\n7. Здоровье\n8. Информационная поддержка\n9. Технические вопросы\n10. Личные вопросы\n11. Студенческое самоуправление\n12. Права\n (отправь цифру)",
        reply_markup=builder.as_markup()
    )
@router.message(Command("menu"))
async def cmd_menu(message:types.Message):
   await message.answer(
        "Здравствуй, абитуриет, тебя приветствует FAQ бот от ОмГТУ, который ответит на твои вопросы! Для начала выбери тему из списка:"
        "\n1. Обучение\n2. Стипендия и другие виды поддержки\n3. Для иностранных студентов\n4. Общежитие\n5. Оплата услуг\n"
        "6. Внеучебная деятельность\n7. Здоровье\n8. Информационная поддержка\n9. Технические вопросы\n10. Личные вопросы\n11. Студенческое самоуправление\n12. Права\n (отправь цифру)",
        reply_markup=builder.as_markup()
    )
