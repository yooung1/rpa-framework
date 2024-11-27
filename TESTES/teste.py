import snowflake.connector
import json

# Cria uma conexão com o banco de dados (Snowflake);
def make_database_connection():
    try:
        conn = snowflake.connector.connect(
            # banco de dados de teste
            user='rpaorch',
            password='Rpa2024@',
            account='nra45017.east-us-2.azure',
            database='FRAMEWORK',
            schema='PUBLIC',
            quote_identifiers=True
        )
        return conn
    except snowflake.connector.errors.Error as e:
        raise snowflake.connector.errors.Error(f"Erro ao conectar ao banco de dados: {e}")
    except snowflake.connector.errors.DatabaseError as e:
        raise snowflake.connector.errors.DatabaseError(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")

# Função para query de queue items
def get_queue_items_from_db():
    query = """
    SELECT * 
    FROM QUEUE_ITEMS 
    WHERE job_id IS NULL AND FOLDERS_ID = 'Folder1';
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

        # Verificando os dados e exibindo os que não têm Job_ID
        for row in data:
            list_of_queue_items.append(row)
        
    except Exception as e:
        print("Erro ao executar a consulta:", e)
    
    finally:
        conn.close()

# Chama a função
get_queue_items_from_db()
