from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class schemaBase(BaseModel):
    total: int
    deslocamento: int
    limite: int
    usuario: str

    class Config:
        orm_mode = True


class ExtraV1(BaseModel):
    pass

class V1Base(BaseModel):
    pass
