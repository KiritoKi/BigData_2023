import os
import pandas as pd
import xml.etree.ElementTree as ET
from utils.baseurl import baseurl

# Função para ler os arquivos XML em um diretório específico
def ler_arquivos_xml(diretorio):
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
                print(group_identification)
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
                        "NOME-COMPLETO": lider.attrib.get("NOME-COMPLETO"),
                        "NRO-ID-CNPQ": lider.attrib.get("NRO-ID-CNPQ"),
                    }
                    lista_lideres.append(lider_data)

                # Extrair informações dos pesquisadores
                lista_pesquisadores = []
                pesquisador_data = {}
                for pesquisador in pesquisadores:
                    pesquisador_data = {
                    "NOME-COMPLETO": pesquisador.attrib.get("NOME-COMPLETO"),
                    "NRO-ID-CNPQ": pesquisador.attrib.get("NRO-ID-CNPQ"),
                    "LINHAS-DE-PESQUISA": [linha.text for linha in pesquisador.findall(".//ns:LINHA-DE-PESQUISA", namespace)],
                    "AREAS-DE-ATUACAO": [area.text for area in pesquisador.findall(".//ns:AREA-DE-ATUACAO", namespace)],
                }
                lista_pesquisadores.append(pesquisador_data)

                # Extrair informações dos estudantes
                lista_estudantes = []
                estudante_data= {}
                for estudante in estudantes:
                    estudante_data = {
                    "NOME-COMPLETO": estudante.attrib.get("NOME-COMPLETO"),
                    "LINHAS-DE-PESQUISA": [linha.text for linha in estudante.findall(".//ns:LINHA-DE-PESQUISA", namespace)],
                    "AREAS-DE-ATUACAO": [area.text for area in estudante.findall(".//ns:AREA-DE-ATUACAO", namespace)],
                }
                lista_estudantes.append(estudante_data)

                # Adicionar os dados à lista
                dados.append({
                    'NRO-ID-GRUPO': nro_id_grupo,
                    'NRO-ID-CNPQ-INSTITUICAO': nro_id_cnpq_instituicao or None,
                    'NOME-DA-INSTITUICAO': nome_instituicao or None,
                    'AREA-PREDOMINANTE': area_predominante or None,
                    'GRANDE-AREA-PREDOMINANTE': grande_area_predominante or None,
                    'ANO-DE-CRIACAO': ano_criacao,
                    'NOME-DO-GRUPO': nome_grupo,
                    'LIDERES': lista_lideres,
                    'PESQUISADORES': lista_pesquisadores,
                    'ESTUDANTES': lista_estudantes,
                    #'SETORES-DE-APICACAO': setores_aplicacao
                })

    return pd.DataFrame(dados)



# Diretório onde estão os arquivos XML
diretorio_raiz = baseurl('entrypoint/CensoDGPXML-2016')

# Ler os arquivos XML e criar um DataFrame
dados_xml = ler_arquivos_xml(diretorio_raiz)

# Exibir o DataFrame
print(dados_xml)
#print(dados_xml[['LIDERES']])

# Filtrar as linhas onde NRO-ID-CNPQ-INSTITUICAO é igual a 123456
linhas_filtradas = dados_xml.loc[dados_xml['NRO-ID-GRUPO'] == '0000301510136952']

# Exibir o DataFrame resultante
print(linhas_filtradas)


# Se desejar, utilize Pandas para análise e Matplotlib para gráficos
# Aqui você pode usar funcionalidades do Pandas para manipular os dados e Matplotlib para criar gráficos.
