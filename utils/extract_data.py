from typing import List, Optional
import os
import xml.etree.ElementTree as ET
from utils.baseurl import baseurl


def extract_data() -> List[dict]:
    # Diretório onde estão os arquivos XML
    diretorio_raiz = baseurl('entrypoint/CensoDGPXML-2016')

    # Ler os arquivos XML e criar um DataFrame
    dados_xml = _ler_arquivos_xml(diretorio_raiz)
    return dados_xml

# Função para ler os arquivos XML em um diretório específico
def _ler_arquivos_xml(diretorio) -> List[dict]:
    dados = []
    stop = False
    for pasta_raiz, pastas, arquivos in os.walk(diretorio):
        #if stop:
        #    break
        for arquivo in arquivos:
            if arquivo.endswith('.xml') and not arquivo.endswith('_estendido.xml'):
                #stop = True
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                # Processar o arquivo XML
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()
                namespace = {'ns': 'http://www.cnpq.br/lmpl/2002/XSD/Grupo'}

                # Extrair dados do arquivo XML
                nro_id_grupo = root.attrib.get("NRO-ID-GRUPO")
                group_identification = root.find('.//ns:IDENTIFICACAO-DO-GRUPO', namespace)

                if group_identification is not None:
                    nro_id_cnpq_instituicao = root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("NRO-ID-CNPQ-INSTITUICAO")
                    nome_instituicao = root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("NOME-DA-INSTITUICAO")
                    area_predominante =  root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("AREA-PREDOMINANTE")
                    grande_area_predominante = root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("GRANDE-AREA-PREDOMINANTE")
                    ano_criacao = root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("ANO-DE-CRIACAO")
                    nome_grupo = root.find(".//ns:IDENTIFICACAO-DO-GRUPO", namespace).attrib.get("NOME-DO-GRUPO")
                else: 
                    nro_id_cnpq_instituicao = None
                    nome_instituicao = None
                    area_predominante = None
                    grande_area_predominante = None
                    ano_criacao = None
                    nome_grupo = None                
                lideres = root.findall('.//ns:LIDERES/*', namespace)
                pesquisadores = root.findall('.//ns:PESQUISADORES/*', namespace)
                estudantes = root.findall('.//ns:ESTUDANTES/*', namespace)
                #setores_aplicacao = root.find('.//ns:SETORES-DE-APLICACAO').text

                # Extrair informações dos líderes
                lista_lideres = []
                for lider in lideres:
                    lider_data = {
                        "grupo_de_pesquisa_id": nro_id_grupo,
                        "nome_completo": lider.attrib.get("NOME-COMPLETO"),
                        "nro_id_cnpq": lider.attrib.get("NRO-ID-CNPQ"),
                    }
                    lista_lideres.append(lider_data)

                # Extrair informações dos pesquisadores
                lista_pesquisadores = []
                pesquisador_data = {}
                for pesquisador in pesquisadores:
                    pesquisador_data = {
                    "grupo_de_pesquisa_id": nro_id_grupo,
                    "nome_completo": pesquisador.attrib.get("NOME-COMPLETO"),
                    "nro_id_cnpq": pesquisador.attrib.get("NRO-ID-CNPQ"),
                    "linhas_de_pesquisa": [linha.text for linha in pesquisador.findall(".//ns:LINHA-DE-PESQUISA", namespace)],
                    "areas_de_atuacao": [area.text for area in pesquisador.findall(".//ns:AREA-DE-ATUACAO", namespace)],
                }
                lista_pesquisadores.append(pesquisador_data)

                # Extrair informações dos estudantes
                lista_estudantes = []
                estudante_data= {}
                for estudante in estudantes:
                    estudante_data = {
                    "grupo_de_pesquisa_id": nro_id_grupo,
                    "nome_completo": estudante.attrib.get("NOME-COMPLETO"),
                    "linhas_de_pesquisa": [linha.text for linha in estudante.findall(".//ns:LINHA-DE-PESQUISA", namespace)],
                    "areas_de_atuacao": [area.text for area in estudante.findall(".//ns:AREA-DE-ATUACAO", namespace)],
                }
                lista_estudantes.append(estudante_data)

                # Adicionar os dados à lista
                dados.append({
                    'grupo_de_pesquisa': {
                        'nro_id_grupo': nro_id_grupo,
                        'nro_id_cnpq_instituicao': nro_id_cnpq_instituicao or None,
                        'nome_da_instituicao': nome_instituicao or None,
                        'area_predominante': area_predominante or None,
                        'grande_area_predominante': grande_area_predominante or None,
                        'ano_de_criacao': ano_criacao,
                        'nome_do_grupo': nome_grupo,
                    },
                    'lideres': lista_lideres,
                    'pesquisadores': lista_pesquisadores,
                    'estudantes': lista_estudantes,
                    #'SETORES-DE-APICACAO': setores_aplicacao
                })

    return dados





