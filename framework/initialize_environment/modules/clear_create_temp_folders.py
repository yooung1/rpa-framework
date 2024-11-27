"""
Módulo: clear_temp_directories
Descrição:
    Este módulo fornece uma função para gerenciar diretórios temporários. 
    Ele remove todo o conteúdo de diretórios especificados e recria os diretórios se eles não existirem.

Funções:
    - clear_create_temp_folders(list_of_directories): 
        Remove todos os arquivos e subpastas dentro dos diretórios especificados. 
        Caso um diretório não exista, ele será criado automaticamente.

Exceções:
    - TypeError: 
        Levantada se o parâmetro `list_of_directories` não for do tipo `list`.
    - PermissionError: 
        Levantada ao tentar remover um arquivo ou diretório sem permissão suficiente.
    - FileNotFoundError: 
        Levantada se um arquivo ou pasta especificado não for encontrado.
    - Exception: 
        Para quaisquer outros erros não previstos.

Usos:
    - Ideal para gerenciar pastas temporárias que precisam ser limpas antes de executar novas operações.
    - Garantir que o ambiente temporário esteja limpo e preparado para uso.

Autor: [Samuel Pierre]
Última Modificação: [27/11/2024]
"""

import os
import shutil  # Necessário para remover diretórios não vazios

def clear_create_temp_folders(list_of_directories):
    """
    Remove todos os arquivos e pastas dentro de diretórios especificados.
    Se o diretório não existir, ele será criado.

    Args:
        list_of_directories (list): Uma lista contendo os caminhos dos diretórios a serem gerenciados.

    Exceções:
        - TypeError: Levantada se `list_of_directories` não for uma lista.
        - PermissionError: Levantada ao tentar remover itens sem permissão suficiente.
        - FileNotFoundError: Levantada se o item a ser removido não for encontrado.
        - Exception: Para quaisquer erros inesperados durante a operação.

    Exemplo:
        >>> clear_create_temp_folders(["temp/dir1", "temp/dir2"])
    """
    if not isinstance(list_of_directories, list):
        raise TypeError("O parâmetro passado não é do tipo list")

    for directory in list_of_directories:
        if not os.path.exists(directory):
            # Diretório não existe, será criado
            os.makedirs(directory, exist_ok=True)
        else:
            # Limpando o conteúdo do diretório existente
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                try:
                    if os.path.isfile(item_path):
                        # Removendo arquivos
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        # Removendo subdiretórios
                        shutil.rmtree(item_path)
                except PermissionError:
                    raise PermissionError(f"Erro de permissão ao tentar remover: {item_path}. Verifique suas permissões.")
                except FileNotFoundError:
                    raise FileNotFoundError(f"Arquivo ou pasta não encontrado: {item_path}.")
                except Exception as e:
                    raise Exception(f"Erro inesperado ao remover {item_path}: {e}")
