from typing import Generic, List, Type, TypeVar, Optional
from pydantic import BaseModel
from sqlalchemy import Table, func, asc
from sqlalchemy.orm import Session, attributes
from sqlalchemy.sql import select, insert, Select, delete

TableType = TypeVar("TableType", bound=Table)
SelectSchemaType = TypeVar("SelectSchemaType", bound=BaseModel)


class Base(Generic[TableType, SelectSchemaType]):
    def __init__(self, table: Type[TableType],
                 order_by: Optional[str] = None):
        self.table = table
        self.order_by = order_by

    def proccess_kwargs_consult(self, query: Select, kwargs: dict):
        return query
    
    def declaration_total_result(self, **kwargs) -> Select:
        query = self.table.select(). \
            with_only_columns([func.count(self.table.c.nro_id_grupo)])
        query = self.proccess_kwargs_consult(query, kwargs)

        return query
    
    def declaration_get_result(self,
                                   deslocamento: int,
                                   limite: int,
                                   **kwargs) -> Select:
        query = self.table.select()
        query = self.proccess_kwargs_consult(query, kwargs)

        if self.order_by:
            query = query.order_by(asc(self.order_by))
        query = query.offset(deslocamento).limit(limite)

        return query
    
    def criar(self, db: Session, *, obj_in: SelectSchemaType) -> SelectSchemaType:
        #obj_in_data = attributes.instance_dict(obj_in)
        
        #obj_in_data = jsonable_encoder(obj_in)
        query = insert(self.table).values(obj_in)
        db.execute(query)
        db.commit()
        return obj_in
    
    def deleteAll(self, db: Session):
        query = delete(self.table)
        db.execute(query)
        db.commit()
    
    def reset_sequence(self, db: Session):
        table_name = self.table.name
        query = f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), coalesce(max(id), 1), false) FROM {table_name};"
        db.execute(query)
        db.commit()