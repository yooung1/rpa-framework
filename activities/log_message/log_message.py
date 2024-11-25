# Arquivo log.py
import logging
import os

class LogMessages:
    """
        Esta função serve para gravar logs do processo\n
        Para utilizar esta função, será necessario chama-la\n
        obs: é recomendado herda-la -->\n
        super().__init__() para inicializar o modulo
    """
    def __init__(self):
        # Configurar diretório e arquivo de log
        log_dir = os.getcwd()
        os.makedirs(log_dir, exist_ok=True)
        # Configuração do logger
        logging.basicConfig(
            filename=os.path.join(log_dir, 'app.log'),
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

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
    