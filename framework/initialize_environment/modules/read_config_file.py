# LER O ARQUIVO DE CONFIGURAÇÃO (JSON)
# SE O ARQUIVO NÃO EXISTIR --> LANÇAR ERRO --> FINAL STATE
# SE O ARQUIVO ESTIVER FORA DE PADRÃO --> LANÇAR ERRO --> FINAL STATE
# SE TUDO ESTIVER CERTO IR PARA A FUNC CREATE_QUEUE_ITEMS# 
import json
import os

def read_config_file():
    """
    Lê os dados do arquivo config.json
    """
    # Caminho do arquivo de configuração
    json_path = os.path.join(os.getcwd(), r'data\config.json')

    # Verifica se o arquivo existe
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Arquivo de configuração (config.json) não existe '{json_path}'")

    # Tenta carregar o conteudo do arquivo
    try:
        with open(json_path) as file:
            config = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro no formato do arquivo JSON: {e}.")

    # Se tudo estiver certo, retorna os dados carregados
    return config