from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.inline_keyboards import main_keyboard, document_keyboard
from database.database import SessionLocal, UploadedFile



# ------------------------------------------------------------------------------------------
#
#                                   variable
#
# --------------
#
#   инициализируем переменную под роутер
#
# ------------------------------------------------------------------------------------------
router_common = Router()




# ------------------------------------------------------------------------------------------
#
#                                   default's function
#
# --------------
#
#   отпраавляет пользовательскую панель управление ботом
#
# ------------------------------------------------------------------------------------------
@router_common.message(CommandStart())
async def cmd_start(message: Message):
    username = message.from_user.username

    welcome_text = (
        f"`{username}`, выберите действие из списка ниже:"
        ""
    )

    await message.answer(welcome_text, reply_markup=main_keyboard)




# ------------------------------------------------------------------------------------------
#
#                                   default's function
#
# --------------
#
#   отпраавляет помощь в управлении ботом
#
# ------------------------------------------------------------------------------------------
@router_common.message(Command('help'))
async def cmd_help(message: Message):

    help_text = (
        "Вы можете управлять мной, отправляя следующие команды:\n\n"
        "/start - главное меню\n"
        "/help - информация о всех командах\n"
        "/documentation - документация бота\n\n"
        "/document - получить документ\n"
        "А так же вы можете использовать клавиатуру ниже:"
    )

    await message.answer(help_text, reply_markup=main_keyboard)




# ------------------------------------------------------------------------------------------
#
#                                   default's function
#
# --------------
#
#   отпраавляет документацию бота
#
# ------------------------------------------------------------------------------------------
@router_common.message(Command('documentation'))
async def cmd_getid(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_full_name = message.from_user.full_name

    info_about_user = (
        "общая информация о пользователе:\n\n"
        f"- user id: `{user_id}`\n"
        f"- user name: `{user_name}`\n"
        f"- user full name: `{user_full_name}`\n"
    )
    
    info_about_bot = (
        "общая информация о боте:\n\n"
        f"- язык разработки: `python 3.14`\n"
        f"- библиотека: `aiogram 3.X`\n"
        f"- рзработчик: `@ymfmgly`\n"
    )

    await message.answer(info_about_user)
    await message.answer(info_about_bot)








# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   отправка докуумента пользователю
#
# ------------------------------------------------------------------------------------------
@router_common.callback_query(lambda c: c.data == "output_document")
async def ikb_main_menu(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer_document(FSInputFile("documents/СОГЛАШЕНИЕ_О_РАСПРЕДЕЛЕНИИ_ПРИБЫЛИ.pdf"), 
                                           caption="Вот ваш документ", 
                                           reply_markup=document_keyboard)




# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   пользователь подтвердил свое согласие с документом
#
# ------------------------------------------------------------------------------------------
@router_common.callback_query(lambda c: c.data == "user_agrees")
async def ikb_usr_agree(callback: CallbackQuery):
    await callback.answer("Вы подтвердили свое согласие с документом")
    await callback.message.edit_reply_markup(reply_markup=None)

    database = SessionLocal()
    try:
        file_record = UploadedFile(
            user_id=callback.from_user.id,
            username=callback.from_user.username,
            user_choose="пользователь подтвердил свое согласие с документом"
        )
        database.add(file_record)
        database.commit()
    except Exception as e:
        database.rollback()
        await callback.message.answer(f"Ошибка при сохранении в БД: {e}")
    finally:
        database.close()

    await callback.message.answer("Ваше решение зафиксировано: Вы **подтвердили** свое согласия с документом")




# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   пользователь отказался от согласие с документом
#
# ------------------------------------------------------------------------------------------
@router_common.callback_query(lambda c: c.data == "user_dsnt_agree")
async def ikb_usr_dsnt_agree(callback: CallbackQuery):
    await callback.answer("Вы отказываетесь от согласия с документом")
    await callback.message.edit_reply_markup(reply_markup=None)

    database = SessionLocal()
    try:
        file_record = UploadedFile(
            user_id=callback.from_user.id,
            username=callback.from_user.username,
            user_choose="пользователь отказывается от согласия с документом"
        )
        database.add(file_record)
        database.commit()
    except Exception as e:
        database.rollback()
        await callback.message.answer(f"Ошибка при сохранении в БД: {e}")
    finally:
        database.close()

    await callback.message.answer("Ваше решение зафиксировано: Вы **отказываетесь** от согласия с документом")




# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   информация об использовании бота
#
# ------------------------------------------------------------------------------------------
@router_common.callback_query(lambda c: c.data == "help")
async def ikb_help(callback: CallbackQuery):
    await callback.answer()

    help_text = (
        "\\[o] Вы можете управлять мной, отправляя следующие команды:\n\n"
        "/start - главное меню\n"
        "/help - информация о всех командах\n"
        "/document - получить документ\n\n"
        "А так же вы можете использовать клавиатуру ниже:"
    )

    await callback.message.answer(help_text, reply_markup=main_keyboard)




# ------------------------------------------------------------------------------------------
#
#                                   callback's function
#
# --------------
#
#   документация бота
#
# ------------------------------------------------------------------------------------------
@router_common.callback_query(lambda c: c.data == "documentation")
async def ikb_documentation(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    user_name = callback.from_user.username
    user_full_name = callback.from_user.full_name

    info_about_user = (
        "общая информация о пользователе:\n\n"
        f"- user id: `{user_id}`\n"
        f"- user name: `{user_name}`\n"
        f"- user full name: `{user_full_name}`\n"
    )
    
    info_about_bot = (
        "общая информация о боте:\n\n"
        f"- язык разработки: `python 3.14`\n"
        f"- библиотека: `aiogram 3.X`\n"
        f"- рзработчик: `@ymfmgly`\n"
    )

    await callback.message.answer(info_about_user)
    await callback.message.answer(info_about_bot)