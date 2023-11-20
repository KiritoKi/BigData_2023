from sqlalchemy import Column, Integer, String, Table,ForeignKey

from database.meta_data import meta_data

lideres = Table("lideres", meta_data,
    Column("lider_id", Integer, primary_key=True),
    Column("grupo_de_pesquisa_id", String(255), ForeignKey("grupo_de_pesquisa.nro_id_grupo")),
    Column("nome_completo", String(255)),
    Column("nro_id_cnpq", String(255)),
)