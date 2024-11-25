import os
import shutil


def clear_create_temp_folders():
    """
    Remove todos os arquivos e pastas dentro de um diretório.
    """
    directory_path = os.path.join(os.getcwd(), r'01 - data')
    
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"O diretório '{directory_path}' não existe.")

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)  
            elif os.path.isfile(item_path):
                os.remove(item_path)  
                return (f"Arquivo removido: {item_path}")
        except PermissionError:
            raise PermissionError (f"Erro de permissão ao tentar remover: {item_path}. Verifique suas permissões.")
        except FileNotFoundError:
            raise FileNotFoundError (f"Arquivo ou pasta não encontrado: {item_path}.")
        except Exception as e:
            raise Exception (f"Erro inesperado ao remover {item_path}: {e}")

    try:
        os.makedirs(os.path.join(directory_path, "Input"), exist_ok=True)
        os.makedirs(os.path.join(directory_path, "Output"), exist_ok=True)
        os.makedirs(os.path.join(directory_path, "Temp"), exist_ok=True)
    except Exception as e:
        raise Exception (f"Erro ao criar pastas: {e}")