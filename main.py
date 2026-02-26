import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

# Импорт токена из конфига
from config import BOT_TOKEN, ADMIN_IDS
from handlers.common import router_common
from handlers.user import router_user
from handlers.admin import router_admin, IsAdmin




# ------------------------------------------------------------------------------------------
#
#                                   variables
#
# --------------
#
#   инициализация бота
#   инициализация диспетчера
#
# ------------------------------------------------------------------------------------------
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="Markdown"))
dp = Dispatcher()



# фильтруем роутер админа под админ ключи
router_admin.message.filter(IsAdmin(ADMIN_IDS))








# ------------------------------------------------------------------------------------------
#
#                                   function
#
# --------------
#
#   запуск бота
#
# ------------------------------------------------------------------------------------------
async def main():
    """Основная функция запуска бота"""
    try:
        print("Bot start")

        # Запуск пулла
        dp.include_routers(router_common, router_user, router_admin)
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        raise
    finally:
        print("Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем (Ctrl+C)")
    except Exception as e:
        print(f"Критическая ошибка: {e}")