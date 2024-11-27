from activities.database_activities.data_base_connection.data_base_connection import make_database_connection
import json


def get_queue_items_from_db(config_data):
    # Extrair o process ID dos dados de config
    process_dict = json.loads(config_data)
    process_id = process_dict["process_id"]
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
            list_of_queue_items.append(row)
        return list_of_queue_items
    
    except Exception as e:
        print("Erro ao executar a consulta:", e)
    finally:
        conn.close()