"""
Módulo: config_reader
Descrição:
    Este módulo fornece uma função para ler e validar um arquivo de configuração JSON 
    localizado no diretório `data`. É útil para carregar configurações gerais de um sistema.

Funções:
    - read_config_file(): Lê e valida um arquivo JSON de configuração.
    
Exceções:
    - FileNotFoundError: Se o arquivo `config.json` não for encontrado.
    - ValueError: Se o conteúdo do arquivo JSON for inválido.

Autor: [Samuel Pierre]
Última Modificação: [27/11/2024]
"""

import json
import os

def read_config_file():
    """
    Lê os dados do arquivo config.json.

    Retorna:
        dict: Um dicionário contendo os dados carregados do arquivo de configuração.

    Exceções:
        FileNotFoundError: Se o arquivo `config.json` não for encontrado no caminho esperado.
        ValueError: Se o conteúdo do arquivo JSON for inválido.

    Exemplo de Uso:
        >>> config = read_config_file()
        >>> trás o resultado do Json
    
    """
    # Caminho do arquivo de configuração
    json_path = os.path.join(os.getcwd(), r'data\config.json')

    # Verifica se o arquivo existe
    if not os.path.exists(json_path):
        raise FileNotFoundError(
            f"Arquivo de configuração (config.json) não existe '{json_path}'"
        )

    # Tenta carregar o conteúdo do arquivo
    try:
        with open(json_path) as file:
            data_config = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro no formato do arquivo JSON: {e}.")

    # Se tudo estiver certo, retorna os dados carregados
    return data_config
