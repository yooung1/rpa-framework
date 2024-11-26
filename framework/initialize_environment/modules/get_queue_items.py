from activities.database_activities.get_queue_items_from_db.get_queue_items_from_db import get_queue_items_from_db

# PEGAR O ID DO PROCESSO E CHAMAR A ACTIVITIE DE CONEXAO COM O BANCO DE DADOS E EXTRAIR O QUEUE ITEMS DE LA E RETORNAR

def get_queue_items(config_data):
    """
    Esta função ira extrair os queue items do banco de dados e trata-los e ira retornar a lista tratada dos queue items
    """
    get_queue_items_from_db(config_data)
    # TRATAR OS DADOS DE QUEUE ITEMS RECEBIDOS
    # AQUI EMBAIXO

