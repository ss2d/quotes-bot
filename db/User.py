from . import BaseModel
from peewee import *


class User(BaseModel):
    tg_id = BigIntegerField(primary_key=True, unique=True)
