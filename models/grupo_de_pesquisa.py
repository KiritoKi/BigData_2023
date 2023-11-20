from sqlalchemy import Column, Integer, String, Table

from database.meta_data import meta_data

grupo_de_pesquisa = Table("grupo_de_pesquisa", meta_data,
                    Column("nro_id_grupo", String(255), primary_key=True),
                    Column("nro_id_cnpq_instituicao", String(255)),
                    Column("nome_da_instituicao", String(255)),
                    Column("area_predominante", String(255)),
                    Column("grande_area_predominante", String(255)),
                    Column("ano_de_criacao", Integer),
                    Column("nome_do_grupo", String(255))
                    )
