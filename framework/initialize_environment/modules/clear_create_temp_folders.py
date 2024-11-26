import os
import shutil  # Necessário para remover diretórios não vazios

def clear_create_temp_folders(list_of_directories):
    """
    Remove todos os arquivos e pastas dentro de um diretório.
    Se o diretório não existir, ele será criado.
    """
    if not isinstance(list_of_directories, list):
        raise TypeError("O parâmetro passado não é do tipo list")

    for directory in list_of_directories:
        # Verifica se o diretório existe, se não, cria
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        # Limpando arquivos temporários no diretório
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            try:
                # Se o item for um arquivo, remove
                if os.path.isfile(item_path):
                    os.remove(item_path)
                # Se o item for uma pasta, remove
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Remove diretórios e tudo o que estiver dentro deles
            except PermissionError:
                raise PermissionError(f"Erro de permissão ao tentar remover: {item_path}. Verifique suas permissões.")
            except FileNotFoundError:
                raise FileNotFoundError(f"Arquivo ou pasta não encontrado: {item_path}.")
            except Exception as e:
                raise Exception(f"Erro inesperado ao remover {item_path}: {e}")