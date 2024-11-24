import os
import shutil


def clear_create_temp_folders():
    """
    Remove todos os arquivos e pastas dentro de um diretório.
    """
    directory_path = os.path.join(os.getcwd(), r'01 - data')
    
    # Verificar se o diretório existe
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"O diretório '{directory_path}' não existe.")

    # Remover todos os arquivos e pastas no diretório
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove o diretório e seu conteúdo
            elif os.path.isfile(item_path):
                os.remove(item_path)  # Remove arquivos individuais
                return (f"Arquivo removido: {item_path}")
        except PermissionError:
            return (f"Erro de permissão ao tentar remover: {item_path}. Verifique suas permissões.")
        except FileNotFoundError:
            return (f"Arquivo ou pasta não encontrado: {item_path}.")
        except Exception as e:
            return (f"Erro inesperado ao remover {item_path}: {e}")

    # Criar novas pastas dentro do diretório
    try:
        os.makedirs(os.path.join(directory_path, "Input"), exist_ok=True)
        os.makedirs(os.path.join(directory_path, "Output"), exist_ok=True)
        os.makedirs(os.path.join(directory_path, "Temp"), exist_ok=True)
    except Exception as e:
        return (f"Erro ao criar pastas: {e}")