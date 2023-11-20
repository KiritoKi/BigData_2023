from typing import Type

from sqlalchemy import Table
from sqlalchemy.sql import Select

from models.grupo_de_pesquisa import grupo_de_pesquisa
from repositorio.base import Base
from schemas import grupo_de_pesquisa as v1


class GrupoDePesquisaV1(Base[Table, v1.schemaGrupoDePesquisa]):
    def processar_kwargs_consulta(self, declaracao: Select, kwargs: dict):

        return declaracao



grupo_de_pesquisa_v1 = GrupoDePesquisaV1(table=grupo_de_pesquisa, order_by='nro_id_grupo')

