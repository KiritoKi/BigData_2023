from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class schemaLideres(BaseModel):
    lider_id: Optional[int]
    grupo_de_pesquisa_ID: str
    nome_completo: str
    nro_id_cnpq: str

    class Config:
        orm_mode = True