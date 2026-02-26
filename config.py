import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Теперь можно получать значения
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID_STR = os.getenv("ADMIN_ID_STR")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR")

ADMIN_IDS = [int(id_str) for id_str in ADMIN_ID_STR.split(",")] if ADMIN_ID_STR else []

# Проверка, что токен загрузился
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле")

if not ADMIN_ID_STR:
    raise ValueError("ADMIN_ID_STR не найден в .env файле")

if not DOWNLOAD_DIR:
    raise ValueError("DOWNLOAD_DIR не найден в .env файле")