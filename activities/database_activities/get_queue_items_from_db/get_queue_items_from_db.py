from activities.database_activities.data_base_connection.data_base_connection import make_database_connection
import json


# Função para query de queue items
def get_queue_items_from_db(config_data):
    # Extrair o process ID dos dados de config
    process_dict = json.loads(config_data)
    process_id = process_dict["process_id"]
    # Inicializa lista de queue items
    list_of_queue_items = []
    # Recebe variável de saída conn da função make_database_connection()
    conn = make_database_connection()
    # Inicializa cursor
    cursor = conn.cursor()
    try:
        # EXECUTAR A PESQUISA DE QUEUE ITEMS DO PROCESS ID

        # TODO: PEGAR OS DADOS DO BANCO DE DADOS
        cursor.execute(config_data)
        data = cursor.fetchall()
        if data:
            for i in data:
                list_of_queue_items.append(i)
        return list_of_queue_items
    except Exception as e:
        raise Exception (f"Erro inesperado {e}")
    finally:
        # Fecha as conexões do banco de dados
        cursor.close()
        conn.close()
