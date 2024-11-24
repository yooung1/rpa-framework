# CRIAR ITENS DE FILA EXTRAIDOS DO CONFIG.JSON
# SE ESTIVER VAZIO O PROCESSO NÃO TERÁ QUEUE ITEMS ELE VAI RODAR COM UM VALOR DEFAULT# 
# VOU PEGAR A O DICT QUE VEIO DO config.json e pegar a chave queue_items e criar uma lista com esses valores

import json

def create_queue_items(config_file):
    """
    Cria uma lista contendo os queue items
    """
    data = json.load(config_file)
    queue_items = data["queue_items"]
    return queue_items
