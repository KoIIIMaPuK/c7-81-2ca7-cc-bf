from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile




# ------------------------------------------------------------------------------------------
#
#                                   variable
#
# --------------
#
#   инициализируем переменную под роутер
#
# ------------------------------------------------------------------------------------------
router_user = Router()




# отправка документа пользователю 
@router_user.message(Command('document'))
async def usr_document(message: Message):
    await message.answer_document(FSInputFile("documents/СОГЛАШЕНИЕ О РАСПРЕДЕЛЕНИИ ПРИБЫЛИ.pdf"))