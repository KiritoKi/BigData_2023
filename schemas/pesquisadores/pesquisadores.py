from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class schemaPesquisadores(BaseModel):
    pesquisador_id: Optional[int]
    grupo_de_pesquisa_ID: str
    nome_completo: str
    nro_id_cnpq: str
    linhas_de_pesquisa: str
    areas_de_atuacao: str

    class Config:
        orm_mode = True