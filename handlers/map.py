from aiogram.types import CallbackQuery
from aiogram import Router, F


router = Router()
@router.callback_query(F.data=='map')
async def map(callback:CallbackQuery):
    await callback.message.answer_photo("https://rasp.omgtu.ru/assets/img/map.jpg")