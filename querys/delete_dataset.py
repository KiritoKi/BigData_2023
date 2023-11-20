from database.meta_data import meta_data
from database.session import engine
from repositorio.rp_estudantes import estudantes_v1 as estudantes
from repositorio.rp_grupo_de_pesquisa import grupo_de_pesquisa_v1 as grupo_de_pesquisa
from repositorio.rp_pesquisadores import pesquisadores_v1 as pesquisadores
from repositorio.rp_lideres import lideres_v1 as lideres
from utils.extract_data import extract_data
from database.deps import get_db

def deleteAll():
    try:
        with get_db() as db:
            estudantes.deleteAll(db)
            lideres.deleteAll(db)
            pesquisadores.deleteAll(db)
            grupo_de_pesquisa.deleteAll(db)
            estudantes.reset_sequence(db)
            lideres.reset_sequence(db)
            pesquisadores.reset_sequence(db)
            grupo_de_pesquisa.reset_sequence(db)
        
        return True
    except Exception as e:
        print(f"Erro ao deletar dados: {str(e)}")
        return False
