from . import BaseModel
from peewee import *


class Ban(BaseModel):
    tg_id = BigIntegerField(primary_key=True, unique=True)
    reason = CharField(max_length=128, null=True)
