# Imports
from modules.execute_query import get_queue_items

def retrieve_queue_items():
    try:
        return get_queue_items()
    except Exception as e:
        raise Exception (f"Erro inesperado {e}")