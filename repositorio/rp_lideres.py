from typing import Type

from sqlalchemy import Table
from sqlalchemy.sql import Select

from models.lideres import lideres
from repositorio.base import Base
from schemas import lideres as v1


class LideresV1(Base[Table, v1.schemaLideres]):
    def processar_kwargs_consulta(self, declaracao: Select, kwargs: dict):

        return declaracao



lideres_v1 = LideresV1(table=lideres, order_by='lider_id')

