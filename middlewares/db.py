from abc import ABC
from typing import Any, Dict, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update

from db import db


class DatabaseMiddleware(BaseMiddleware, ABC):
    async def __call__(
        self,
        handler: Callable,
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        with db:
            return await handler(event, data)
