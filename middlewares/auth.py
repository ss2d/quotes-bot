from abc import ABC
from typing import Any, Dict, Callable, Optional

import peewee
from aiogram.types import Update, User

from db.Ban import Ban
from db.User import User as DBUser
from middlewares.util import UtilMiddleware


class AuthMiddleware(UtilMiddleware, ABC):
    async def __call__(
        self,
        handler: Callable,
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user = self.get_user(event)
        if self.check_ban(user):
            return

        data['user'] = self.get_auth_user(user)
        return await handler(event, data)

    def check_ban(self, user: User) -> bool:
        try:
            Ban.get_by_id(user.id)
            return True

        except peewee.DoesNotExist:
            return False

    def get_auth_user(self, user: User) -> Optional[DBUser]:
        try:
            return DBUser.get_by_id(user.id)

        except peewee.DoesNotExist:
            return None

