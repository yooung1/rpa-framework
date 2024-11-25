# Imports
from data_base_connection import make_database_connection

# Função para query de queue items
def get_queue_items(process_id, conn):
    # Inicializa lista de queue items
    list_of_queue_items = []
    # Recebe variável de saída conn da função make_database_connection()
    conn = make_database_connection()
    # Inicializa cursor
    cursor = conn.cursor()
    
    # lógica de tentativa de query
    try:
        cursor.execute(process_id) # O process id vem de uma variável fora do escopo
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