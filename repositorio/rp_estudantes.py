from typing import Type

from sqlalchemy import Table
from sqlalchemy.sql import Select

from models.estudantes import estudantes
from repositorio.base import Base
from schemas import estudantes as v1


class EstudantesV1(Base[Table, v1.schemaEstudantes]):
    def processar_kwargs_consulta(self, declaracao: Select, kwargs: dict):

        return declaracao



estudantes_v1 = EstudantesV1(table=estudantes, order_by='estudante_ID')

