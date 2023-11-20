from database.meta_data import meta_data
from database.session import engine
from models.estudantes import estudantes
from models.grupo_de_pesquisa import grupo_de_pesquisa
from models.pesquisadores import pesquisadores
from models.lideres import lideres

def createAll():
    tables = [estudantes, grupo_de_pesquisa, pesquisadores, lideres]
    meta_data.create_all(bind=engine, checkfirst=True, tables=tables)
    return