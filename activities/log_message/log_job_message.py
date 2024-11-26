# Arquivo log.py
import logging
import os

# TODO: ESTE MODULO VAI SE ENCARREGAR DE CRIAR LOGS APENAS PARA O JOB, ISSO INCLUI O Initialize Environment, Initialize Applications, Get Next Queue Item
# E DO final state

# TODO: A LOGICA DE PREENCHIMENTO DE LOG PARA O JOB TERA QUE SER FEITA AQUI DENTRO
# A IDEIA É CRIAR UMA LOGICA QUE IRA CONTINUAR PREENCHENDO O ARQUIVO DE LOGS, MESMO APOS A INSTANCIA TER SIDO FINALIZADA

class LogJobMessages:

    """
        Esta função serve para gravar logs do processo\n
        Para utilizar esta função, será necessario chama-la\n
        obs: é recomendado herda-la -->\n
        super().__init__() para inicializar o modulo
    """
    def __init__(self):
        # Configurar diretório e arquivo de log
        self.log_dir = os.getcwd()

        # Configuração do logger
        logging.basicConfig(
            filename=os.path.join(self.log_dir, r'logs\job.log'),
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def delete_log_file(self):
        try:
            if os.path.exists:
                os.remove(os.path.join(self.log_dir, r'logs\job.log'))
        except PermissionError:
            raise PermissionError (f"Erro de permissão")
        except Exception as e:
            raise Exception (f"Erro inesperado {e}")


    def log_message_debug(self, msg):
        logging.debug(msg)
    
    def log_message_info(self, msg):
        logging.info(msg)

    def log_message_warning(self, msg):
        logging.warning(msg)
    
    def log_message_error(self, msg):
        logging.error(msg)

    def log_message_critical(self, msg):
        logging.critical(msg)


teste = LogJobMessages()

teste.log_message_error("ERRO DE SISTEMA")


