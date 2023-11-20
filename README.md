# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Getting Started

Acesse [Postgresql.com](https://www.postgresql.org/download/)
Caso esteja utilizando OS Linux Dist Ubuntu, Siga esses passos:

Create the file repository configuration:
    ```sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'```
Import the repository signing key:
    ```wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -```
Update the package lists:
    ```sudo apt-get update```
Install the latest version of PostgreSQL.
    ```sudo apt-get -y install postgresql```


Apost instalacao concluida, inicializa o postgres utilizando o SuperUser postgres para criacao de um usuario
```sudo -u postgres psql```

E entao Crie o seunovo usuario

```bash
        # Substitua 'seuusuario' pelo nome desejado para o usuário e 'suasenha' pela senha desejada
    CREATE USER seuusuario WITH PASSWORD 'suasenha';

        # Substitua 'seubanco' pelo nome desejado para o banco de dados
    CREATE DATABASE seubanco;
        #Altera a configuração de codificação de caracteres para o usuário setando, define 'utf8' permitindo caracteres Unicode
    ALTER ROLE seuusuario SET client_encoding TO 'utf8';
        #Habilita o nivel de isolamento read commited, isto é, você pode ver os dados que foram confirmados (commit) por outras transações, mas não verá as mudanças não confirmadas.
    ALTER ROLE seuusuario SET default_transaction_isolation TO 'read committed';
        #Altera o fuso horario para UTC
    ALTER ROLE seuusuario SET timezone TO 'UTC';
        # Conceda todos os privilégios ao usuário sobre o banco de dados
    GRANT ALL PRIVILEGES ON DATABASE seubanco TO seuusuario;
```
Em seguida acesse como super usuario o seu banco de dados
```sudo -u postgres psql <nome_do_db>```
Garanta o acesso ao seu usuario para os schemas nesse banco

```bash
        # Conceder todas permissoes (Caso voce seja o host)
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO seuusuario;
        # Atualizar perissoes para que tambem funcione para futuras tabelas criadas no schema public
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO seuusuario;
        ## Conceder permissoes de create no schema public
    GRANT USAGE, CREATE ON SCHEMA public TO outrousuario;
        # Sair do console do PostgreSQL    
    \q
```

Apos finalizar as alteracoes de permissoes do banco, reset o servico
```sudo service postgresql restart```

Para habilitar autenticacao por senha é necessario

Abra o arquivo pg_hba.conf em um editor de texto. 
A localização do arquivo pode variar dependendo da sua instalação, mas é frequentemente encontrado em /etc/postgresql/<versão-do-postgresql>/main/pg_hba.conf.

Localize a linha correspondente ao método de autenticação para conexões locais (127.0.0.1/32 ou ::1/128) e altere peer para md5.

A partir dai voce ja tem acesso ao banco de dados e pode acessa-lo atraves do comando

```psql -U <seuusuario> -d <seubanco> -h localhost```

é necessario agora instalar a parte da biblioteca do psycopg2 do python para permitir a interacao da aplicacao com o banco de dados e algumas outras

Como boa pratica, utilizaremos um virtual env para instalar as dependencias apenas para esse projeto especifico

```python -m venv venv```
No windows:
```.\venv\Scripts\activate```
No Linux:
```source venv/bin/activate```
(Para sair do ambiente ao finaliar utiliza-se ```deactivate```)
Para agilizar o trabalho e nao aplicar varios comandos de instalacao, ja temos as dependencias no arquivo requirements.txt, para instalar insira o comando:
```pip install -r requirements.txt```

-> Atencao (Caso tenha instalado mais alguma dependencia, execute o comando ```pip freeze > requirements.txt``` para enviar essa dependencia ao requirements.txt)

A partir do ambiente virtual, deve executar o main.py

TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)