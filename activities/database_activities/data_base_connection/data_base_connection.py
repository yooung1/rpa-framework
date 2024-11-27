"""
Módulo: database_connection
Descrição:
    Este módulo fornece uma função para estabelecer conexão com o banco de dados Snowflake.
    É utilizado para facilitar a comunicação entre os scripts do sistema e o banco de dados, 
    retornando uma conexão ativa que pode ser usada para executar consultas e outras operações.

Funções:
    - make_database_connection(): 
        Estabelece uma conexão com o banco de dados Snowflake, utilizando credenciais predefinidas.

Exceções:
    - snowflake.connector.errors.Error: 
        Erro genérico relacionado à conexão com o banco de dados Snowflake.
    - snowflake.connector.errors.DatabaseError: 
        Erro específico de banco de dados, como autenticação inválida ou banco inexistente.
    - Exception: 
        Para quaisquer outros erros não previstos.

Usos (Opcional):
    - Essa conexão pode ser reutilizada em outros módulos para interagir com o banco de dados.
    - É recomendável que as credenciais e configurações sejam armazenadas em um gerenciador seguro.

Autor: [Samuel Pierre]
Última Modificação: [27/11/2024]
"""

import snowflake.connector


def make_database_connection():
    """
    Cria e retorna uma conexão com o banco de dados Snowflake.

    Retorna:
        snowflake.connector.connection.SnowflakeConnection: Um objeto de conexão ao banco de dados Snowflake.

    Levanta:
        snowflake.connector.errors.Error: Se ocorrer algum erro genérico relacionado à conexão com o banco de dados.
        snowflake.connector.errors.DatabaseError: Se ocorrer um erro específico relacionado ao banco de dados.
        Exception: Para quaisquer outros erros inesperados.

    Observações:
        - O usuário, senha, conta, banco de dados e esquema estão atualmente configurados de forma fixa 
          (deveriam ser obtidos de forma mais segura, como de um gerenciador de credenciais ou arquivo de configuração).
        - O parâmetro `quote_identifiers` está ativado para assegurar que identificadores sejam citados corretamente.

    Exemplo de Uso:
        >>> try:
        ...     conn = make_database_connection()
        ...     print("Conexão bem-sucedida!")
        ... except Exception as e:
        ...     print(f"Erro ao conectar: {e}")
    """
    try:
        # TODO: INSERIR KEY VAULT AQUI
        conn = snowflake.connector.connect(
            # Banco de dados de teste
            user='rpaorch',
            password='Rpa2024@',
            account='nra45017.east-us-2.azure',
            database='FRAMEWORK',
            schema='PUBLIC',
            quote_identifiers=True
        )
        # Retorna conexão
        return conn
    # Retorna exceção durante conexão
    except snowflake.connector.errors.Error as e:
        raise snowflake.connector.errors.Error(f"Erro ao conectar ao banco de dados: {e}")
    except snowflake.connector.errors.DatabaseError as e:
        raise snowflake.connector.errors.DatabaseError(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")
