import psycopg2
from core.config import settings
from querys import create_tables, load_dataset, delete_dataset

import asyncio

async def main():
    create_tables.createAll()
    if settings.LOAD_DATASET.lower() == 'yes':
        delete_dataset.deleteAll()
        is_loaded = await load_dataset.loadAll()
        if is_loaded:
            print("Dados Carregados na Base com Sucesso!!")
        else:
            print("Não foi possivel carregar os dados!!")

    
asyncio.run(main())




# Substitua pelos seus próprios valores
db_params = {
    'host': 'localhost',
    'database': 'tcc',
    'user': 'kirito',
    'password': 'yanVP&159951'
}
"""
# Conectar ao banco de dados
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Exemplo: Criar uma tabela
    cursor.execute("CREATE TABLE exemplo (id serial PRIMARY KEY, nome VARCHAR);")

    # Exemplo: Inserir dados na tabela
    cursor.execute("INSERT INTO exemplo (nome) VALUES (%s);", ("Exemplo de Dado",))

    # Exemplo: Consultar dados
    cursor.execute("SELECT * FROM exemplo;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Confirmar as alterações e fechar a conexão
    connection.commit()

except Exception as e:
    print(f"Erro: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
"""