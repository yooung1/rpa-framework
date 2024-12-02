"""
Módulo: kill_all_applications
Descrição:
    Este módulo fornece uma função para fechar programas.

Funções:
    - kill_all_applications(): Recebe uma lista de programas a serem fechados, verifica se o parâmetro passado é uma lista. 
      Para cada processo especificado, verifica se ele está em execução e, se estiver, o encerra.
    
Exceções:
    - psutil.AccessDenied: Informa se o usuário atual possui acesso para encerrar o processo.
    - Exception: Informa erros não capturados.

Usos (Opcional):
    ------
    Este módulo pode ser usado para encerrar programas indesejados ou gerenciar processos de forma automatizada.

Autor: [Samuel Pierre]
Última Modificação: [02/12/2024]
"""

import psutil

def kill_all_applications(list_of_process):
    """
    Encerra os processos especificados por uma lista de nomes.

    OBSERVAÇÃO: Para encontrar o nome correto do processo a ser fechado --> Entre no gerenciador de tarefas -> click direito no processo -> 
    click em "ir para detalhes" -> La voce ira encontrar o nome do processo

    Parâmetros:
    - list_of_process (list): Lista contendo os nomes dos processos a serem encerrados.

    Exceções:
    - TypeError: Lançada se o argumento fornecido não for uma lista.
    - PermissionError: Lançada se o usuário atual não tiver permissão para encerrar um processo.
    - RuntimeError: Lançada para erros genéricos durante a tentativa de encerrar o processo.

    Exemplo de Uso:
    --------
    >>> kill_all_applications(["notepad.exe", "chrome.exe"])
    """
    # Verifica se o parâmetro fornecido é uma lista
    if not isinstance(list_of_process, list):
        raise TypeError("O objeto passado na função kill_all_applications não é uma lista.")

    # Itera pela lista de processos fornecida
    for process in list_of_process:
        # Itera pelos processos ativos no sistema
        for proc in psutil.process_iter(['name']):
            try:
                # Verifica se o nome do processo corresponde ao nome fornecido
                if proc.info['name'] == process:
                    # Encerra o processo
                    proc.kill()
            except psutil.AccessDenied:
                # Lança exceção se o usuário não tiver permissão para encerrar
                raise PermissionError(f"Acesso negado para encerrar {process}.")
            except Exception as e:
                # Lança exceção genérica para outros erros
                raise RuntimeError(f"Erro genérico ao encerrar o processo {process}: {e}")

