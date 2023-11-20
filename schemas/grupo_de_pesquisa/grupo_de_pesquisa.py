from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class schemaGrupoDePesquisa(BaseModel):
    nro_id_grupo: str
    nro_id_cnpq_instituicao: str
    nome_da_instituicao: str
    area_predominante: str
    grande_area_predominante: str
    ano_de_criacao: int
    nome_do_grupo: str


    class Config:
        orm_mode = True
