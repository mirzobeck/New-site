from unicodedata import category
from aiogram.dispatcher.filters.state import StatesGroup, State


class lst(StatesGroup):
    ism = State()
    familiya = State()
    telefon = State()
    shikoyat = State()
    wikii = State()
    news = State()


class post(StatesGroup):
    category = State()