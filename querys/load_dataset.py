from database.meta_data import meta_data
from database.session import engine
from repositorio.rp_estudantes import estudantes_v1 as estudantes
from repositorio.rp_grupo_de_pesquisa import grupo_de_pesquisa_v1 as grupo_de_pesquisa
from repositorio.rp_pesquisadores import pesquisadores_v1 as pesquisadores
from repositorio.rp_lideres import lideres_v1 as lideres
from utils.extract_data import extract_data
from database.deps import get_db

async def loadAll():
    data_list = extract_data()

    try:
        with get_db() as db:
            
            for data_dict in data_list:

                grupo_de_pesquisa_instance = grupo_de_pesquisa.criar(db, obj_in=data_dict["grupo_de_pesquisa"])
                for estudante in data_dict["estudantes"]:
                    estudantes_instance = estudantes.criar(db, obj_in=estudante)
                for lider in data_dict["lideres"]:
                    lideres_instance = lideres.criar(db, obj_in=lider)
                for pesquisador in data_dict["pesquisadores"]:
                    pesquisadores_instance = pesquisadores.criar(db, obj_in=pesquisador)
        
        return True
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return False
