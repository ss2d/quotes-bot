from aiogram import Dispatcher

from .db import DatabaseMiddleware


def setup(dp: Dispatcher):
    dp.update.middleware.register(DatabaseMiddleware())
