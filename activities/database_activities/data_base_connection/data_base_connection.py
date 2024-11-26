# Imports
import snowflake.connector

# Cria uma conexão com o banco de dados (Snowflake);
def make_database_connection():
    try:
        # TO-DO: INSERIR KEY VAUT AQUI
        conn = snowflake.connector.connect(
            user='orch',
            password='Rpa2024@',
            account='nra45017.east-us-2.azure',
            database='ORCHESTRATOR',
            schema='STRUCTURE',
            quote_identifiers=True
        )
        # Retorna conexão
        return conn
    # Retorna exceção durante conexão
    except snowflake.connector.errors.Error as e:
        raise snowflake.connector.errors.Error (f"Erro ao conectar ao banco de dados: {e}")
    except snowflake.connector.errors.DatabaseError as e:
        raise snowflake.connector.errors.DatabaseError(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")