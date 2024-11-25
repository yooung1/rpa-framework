from modules.clear_create_temp_folders import clear_create_temp_folders
from modules.create_general_variables import create_general_variables
from modules.create_queue_items import create_queue_items
from modules.read_config_file import read_config_file

class InitializeEnviroment:
    def __init__(self):
        # Trás os dados do config.json (dict)
        self.read_config_file = read_config_file()
        # Variavel que contem os dados do json extraidos acima - posso chamar este atributo em outras classes
        self.json_data = self.read_config_file
        # Criar lista de Queue items -  posso chamar este atributo em outras classes
        self.list_of_queue_items = create_queue_items(self.json_data)
        # Limpar Temp Folder
        self.clear_temp_folder = clear_create_temp_folders()
