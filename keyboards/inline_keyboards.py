from aiogram import Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




# ------------------------------------------------------------------------------------------
#
#                                       keyboard
#
# --------------
#
#   клавиатура главного меню бота
#
# ------------------------------------------------------------------------------------------
main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Отправить документ", callback_data="output_document")
        ],
        [ 
            InlineKeyboardButton(text="Помощь в использовании бота", callback_data="help")
        ],
        [
            InlineKeyboardButton(text="Документация бота", callback_data="documentation")
        ]
    ]
)




# ------------------------------------------------------------------------------------------
#
#                                       keyboard
#
# --------------
#
#   клавиатура для подтверждения согласия пользователя с документом
#
# ------------------------------------------------------------------------------------------
document_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подтверждаю согласие с документом", callback_data="user_agrees")
    ],
    [
        InlineKeyboardButton(text="Отказываюсь от согласия с документом", callback_data="user_dsnt_agree")
    ]
])




# ------------------------------------------------------------------------------------------
#
#                                       keyboard
#
# --------------
#
#   клавиатура админа для загрузки документа на сервер
#
# ------------------------------------------------------------------------------------------
upload_document = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Загрузить документ на сервер", callback_data="upload_document")
    ]
])