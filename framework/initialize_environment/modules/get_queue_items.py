"""
Módulo: get_queue_items
Descrição:
    Este módulo fornece uma função para ler a tabela de queue_items
    localizado no banco de dados FRAMEWORK. É usado para carregar todos os queue items que não tem JOB_ID atribuido.

Funções:
    - get_queue_items(): Chama a função get_queue_items_from_db() --> Lê a tabela queue_items no banco de dados e trás os itens
    que fila que não possuem JOB_ID atribuido.
    
Exceções:
    None

Usos (Opcional):
    - É possivel tratar os dados que vieram do banco de dados

Autor: [Samuel Pierre]
Última Modificação: [27/11/2024]
"""


from activities.database_activities.get_queue_items_from_db.get_queue_items_from_db import get_queue_items_from_db

def get_queue_items(config_data):
    """
    Chama a função get_queue_items_from_db() --> Lê a tabela queue_items no banco de dados e trás os itens
    que fila que não possuem JOB_ID atribuido

    Retorna:
        list: Uma lista contendo os dados carregados do banco de dados.

    Exceções:
        None --> Se o dev adicionar uma tratativa de dados nesta função ele ira colocar as suas exceções dependendo do tratamento

    Usos (Opcional):
        - É possivel tratar os dados que vieram do banco de dados
    
    """
    # Retornar a lista com todos os dados dos queue items
    return get_queue_items_from_db(config_data)
