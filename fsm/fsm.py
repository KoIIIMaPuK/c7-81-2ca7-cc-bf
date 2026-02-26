from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext




class AdminInputFile(StatesGroup):
    file = State()