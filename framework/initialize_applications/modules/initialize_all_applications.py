# ESTA MODULO NÃO VAI SER USADO DEVIDO A QUE IREI TER UM PROBLEMA DE INSTANCIAMENTO DE PROGRAMAS - O MELHOR A SER FEITO É ABRIR O
# PROGRAMA DIRETAMENTE NO PROCESS

import subprocess

def abrir_aplicativo(lista_de_programas):
    """
    Ao chamar esta função, você precisa passar o caminho absoluto dos aplicativos a serem executados
    \nE uma lista precisa ser passada
    """

    if not isinstance(lista_de_programas, list):
        raise TypeError ("O parametro passado não é uma lista")

    for programa in lista_de_programas:
        try:
            # Abre o aplicativo e espera ele terminar (bloqueante)
            subprocess.run([programa], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError (f"Erro ao abrir o aplicativo: {e}")
        except FileNotFoundError:
            raise FileNotFoundError (f"Aplicativo '{programa}' não encontrado.")
        except Exception as e:
            raise Exception (f"Ocorreu um erro inesperado: {e}")

lista = ["C:\Program Files\Google\Chrome\Application\chrome.exe"]
abrir_aplicativo(lista)
