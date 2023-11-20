from typing import Type

from sqlalchemy import Table
from sqlalchemy.sql import Select

from models.pesquisadores import pesquisadores
from repositorio.base import Base
from schemas import pesquisadores as v1


class PesquisadoresV1(Base[Table, v1.schemaPesquisadores]):
    def processar_kwargs_consulta(self, declaracao: Select, kwargs: dict):

        return declaracao



pesquisadores_v1 = PesquisadoresV1(table=pesquisadores, order_by='pesquisador_id')

