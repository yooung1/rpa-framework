import psutil

def kill_all_applications(list_of_process):
    """
    Esta função precisa receber uma lista de processos que devem ser finalizados
    """
    if not isinstance(list_of_process, list):
        raise TypeError("O objeto passado na função kill_all_applications não é uma lista")

    for process in list_of_process:
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] == process:
                    proc.kill()
            except psutil.AccessDenied:
                raise PermissionError (f"Acesso negado para encerrar {process}.")
            except Exception as e:
                raise RuntimeError (f"Erro generico {e}")