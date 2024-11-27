from framework.initialize_environment.modules.get_queue_items import get_queue_items
from modules.clear_create_temp_folders import clear_create_temp_folders
from modules.create_general_variables import create_general_variables
from modules.read_config_file import read_config_file
from activities.log_message.log_job_message import LogJobMessages

class InitializeEnviroment(LogJobMessages):
    def __init__(self):
        super().__init__()
    def read_config_file(self):
        """
        Chama o modulo de leitura do arquivo config.json e retorna os dados encontrados
        """
        self.log_message_info("LENDO ARQUIVO DE CONFIGURAÇÃO - config.json")
        return read_config_file()

    def get_queue_items(self, config_data):
        """
        Com os parematros extraidos do arquivo config.json ira pegar o Id do processo e extrair os queue_items do banco de dados
        """
        self.log_message_info("LENDO E CRIANDO QUEUE ITEMS")
        get_queue_items(config_data)
    
    def clear_temp_folders(self, list_of_directories):
        """
        Vai receber o caminho de folders, se o folder existir o script ira verificar se existe algo dentro, se existir -> deletar\n
        Se o folder não existir vai ser criado
        """
        self.log_message_info("LIMPANDO PASTAS E ELIMINANDO ARQUIVOS")
        clear_create_temp_folders(list_of_directories)
    