import os
from pathlib import Path
from aiogram import Router, Bot
from aiogram.filters import Command, Filter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from fsm.fsm import AdminInputFile
from keyboards.inline_keyboards import upload_document

DOWNLOAD_DIR = Path("documents")
DOWNLOAD_DIR.mkdir(exist_ok=True)






class IsAdmin(Filter):
    def __init__(self, admin_id: list[int]) -> None:
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_id




# ------------------------------------------------------------------------------------------
#
#                                   variable
#
# --------------
#
#   инициализируем переменную под роутер
#
# ------------------------------------------------------------------------------------------
router_admin = Router()




# ------------------------------------------------------------------------------------------
#
#                                   default's function
#
# --------------
#
#   отправляет админ-панель в виде inline клавиатуры
#
# ------------------------------------------------------------------------------------------
@router_admin.message(Command('admin'))
async def adn_start(message: Message):

    welcome_text = (
        "Добро пожаловать в админ панель. Вы можете использовать команды:\n\n"
        "/upload - загрузить документ на сервер\n\n"
        "Выберите действие:"
    )

    await message.answer(welcome_text, reply_markup=upload_document)






# ------------------------------------------------------------------------------------------
#
#                                   default's function
#
# --------------
#
#   загрузка документов на сервер
#
# ------------------------------------------------------------------------------------------
@router_admin.message(Command('upload'))
async def adn_upload(message: Message, state: FSMContext):
    await state.set_state(AdminInputFile.file)
    await message.answer("Отправьте файл, который вы хотите загрузить")




"""
ждет файл от админа, сохраняет ее в нужную папку
"""
@router_admin.message(AdminInputFile.file)
async def adn_fsm_file(message: Message, state: FSMContext, bot: Bot):

    # если пользователь отправил не документ, отправляем исключение
    if not message.document:
        await message.asnwer("Пожалуйста, отправьте файл, как документ (не как фото/видео)")
        return

    # обновляем стейт
    await state.update_data(
        file_id=message.document.file_id,
        file_name=message.document.file_name,
        file_size=message.document.file_size,
        mime_type=message.document.mime_type
    )

    # подгружаем файл через бота
    file = await bot.get_file(message.document.file_id)
    safe_filename = message.document.file_name or f"file_{message.document.file_id}"

    save_path = DOWNLOAD_DIR / safe_filename
    await bot.download_file(file.file_path, save_path)

    if save_path.exists():
        file_size_kb = os.path.getsize(save_path) / 1024
        
        await message.answer(
            f"Файл успешно загружен:\n\n"
            f"- Имя: `{message.document.file_name}`\n"
            f"- Размер: `{file_size_kb:.2f}` KB\n"
        )
    else:
        await message.answer("Ошибка при сохранении файла")
    
    await state.clear()








# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   загрузка документов на сервер
#
# ------------------------------------------------------------------------------------------
@router_admin.callback_query(lambda c: c.data == "upload_document")
async def adm_ikb_admin_menu(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(AdminInputFile.file)
    await callback.message.answer("Отправьте файл, который вы хотите загрузить")