from sqlalchemy import Column, Integer, String, Table,ForeignKey

from database.meta_data import meta_data

pesquisadores = Table("pesquisadores", meta_data,
    Column("pesquisador_id", Integer, primary_key=True),
    Column("grupo_de_pesquisa_id", String(255), ForeignKey("grupo_de_pesquisa.nro_id_grupo")),
    Column("nome_completo", String(255)),
    Column("nro_id_cnpq", String(255)),
    Column("linhas_de_pesquisa", String),  # Você pode ajustar isso para o tipo de array ou JSON do seu banco
    Column("areas_de_atuacao", String),   # Você pode ajustar isso para o tipo de array ou JSON do seu banco
)