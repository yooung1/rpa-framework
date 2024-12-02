"""
Módulo: get_queue_items_from_db
Descrição:
    Este módulo fornece uma função para ler a tabela de queue_items
    localizado no banco de dados FRAMEWORK. É usado para carregar todos os queue items que não tem JOB_ID atribuido.

Funções:
    - get_queue_items_from_db(): Lê a tabela queue_items no banco de dados e trás os itens
    que fila que não possuem JOB_ID atribuido.
    
Exceções:
    ConnectionError: Erro generico de conexão
    ConnectionRefusedError: Erro de conexão recusada
    Exception: Erros não mapeados nas exceções
Usos (Opcional):
    - É possivel alterar os dados que virão do banco de dados

Autor: [Samuel Pierre] - EMAIL [samuel.joseph@apsen.com.br]
Última Modificação: [02/12/2024]
"""

import sys 
import os

# Indica o caminho absoluto do framework
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../../.."))

from activities.database_activities.data_base_connection.data_base_connection import make_database_connection
import json


def get_queue_items_from_db(config_data):
    """
    Lê a tabela `QUEUE_ITEMS` do banco de dados `FRAMEWORK` e retorna todos os itens de fila 
    que não possuem `JOB_ID` atribuído.

    Parâmetros:
        config_data (str): Uma string JSON contendo as configurações necessárias, incluindo o `process_id`.

    Retorna:
        list[dict]: Uma lista de dicionários, onde cada dicionário representa um item da tabela `QUEUE_ITEMS`
        que atende aos critérios definidos na consulta SQL.

    Levanta:
        ConnectionError: Se houver um erro genérico de conexão ao banco de dados.
        ConnectionRefusedError: Se a conexão ao banco de dados for recusada.
        Exception: Para quaisquer outros erros não mapeados.

    Exemplo de Uso:
        >>> config_data = '{"process_id": "12345"}'
        >>> queue_items = get_queue_items_from_db(config_data)
        >>> for item in queue_items:
        ...     print(item)
        
    Exemplo de Retorno:
        [
            [{'ID': 101, 'REFERENCE': 'Ref-001', 'CREATION_DATE': datetime.datetime(2024, 11, 27, 5, 57, 47, 812000),
            'EXECUTION_DATE': datetime.datetime(2024, 11, 27, 5, 57, 47, 812000), 'STATUS': 'Pending', 'RETRY_NUMBER': 1,
            'JOB_ID': None, 'FOLDERS_ID': 'Folder1', 'SPECIFIC_CONTENT': '{\n  "key1": "value1",\n  "key2": "value2"\n}'}]
        ]

    Observações:
        - Aqui estamos usando o SNOWFLAKE, então talvez seja necessario adaptar as querys e a logica dependo do seu processo
        - Certifique-se de que a conexão ao banco de dados esteja configurada corretamente 
          na função `make_database_connection`.
        - O banco de dados e o esquema apropriados são definidos explicitamente no código SQL.
    """

    # Extrair o process ID dos dados de config
    process_dict = json.loads(config_data) # comenta
    process_id = process_dict["process_id"] # comenta
    # process_id = 'Folder1' # descomenta
    query = f"""
    SELECT * 
    FROM QUEUE_ITEMS 
    WHERE job_id IS NULL AND FOLDERS_ID = '{process_id}';
    """
    list_of_queue_items = []

    # Recebe variável de saída conn da função make_database_connection()
    conn = make_database_connection()

    try:
        cursor = conn.cursor()
        cursor.execute("USE DATABASE FRAMEWORK;")
        cursor.execute("USE SCHEMA PUBLIC;")
        cursor.execute(query)

        # Fetching the results
        results = cursor.fetchall()
        
        # Nome das colunas
        columns = [col[0] for col in cursor.description]
        
        # Exibindo os dados no formato de lista de dicionários
        data = [dict(zip(columns, row)) for row in results]

        for row in data:
            # o valor vai vir como uma lista que contem dicionarios
            # vc vai puxar o indice da lista que sera o primeiro dicionario
            # e desse primeiro dicionario voce vai puxar o SPECIFIC_CONTENT
            # depois voce vai transformar esse specific_content num Json e esse json vc consegue tratar como dicionario - ai vc puxa a chave desse dicionario e essa chave ira trazer o valor
            # row['SPECIFIC_CONTENT'] = json.loads(row['SPECIFIC_CONTENT']) -- parsear o SPECIFIC_CONTENT a dict
            list_of_queue_items.append(row)
        return list_of_queue_items
    
    except ConnectionError as e:
        raise ConnectionError (f"Erro de conexão ao banco de dados: {e}")
    except ConnectionRefusedError as e:
        raise ConnectionRefusedError (f"Conexão recusada: {e}")
    except Exception as e:
        print("Erro ao executar a consulta:", e)
    finally:
        conn.close()