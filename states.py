from aiogram.fsm.state import State, StatesGroup

class get_user_name(StatesGroup):
    name = State()