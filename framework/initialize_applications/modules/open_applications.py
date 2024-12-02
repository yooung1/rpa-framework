import os

def open_applications(list_of_applications):
    # CRIAR UM INSTANCIADOR DE PROCESSOS ABERTOS E RETORNAR ESSA LISTA PARA QUE POSSA SER USADA NO PROCESS (CHAMAR A INSTANCIA E USAR)
    list_of_opened_applications = []
    if not isinstance(list_of_applications, list):
        raise TypeError("O parâmetro passado não é do tipo list")

    try:
        for app in list_of_applications:
            os.popen(app)
            list_of_opened_applications.append(app)
    except PermissionError as e:
        raise (f"Erro de permissão {e}")
    except RuntimeError as e:
        raise (f"Erro de tempo {e}")
    except Exception as e:
        raise (f"Erro não mapeado {e}")

