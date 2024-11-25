# ARQUIVO PRINCIPAL
# ESTA CLASSE VAI HERDAR TODAS AS OUTRAS E VAI FZR O GERENCIAMENTO DE EXCEÇÕES --> super()._init__() para inicializar todos os modulos que serão herdados
from activities.log_message import LogMessages
from framework.initialize_environment import InitializeEnviroment

class RunApplication(LogMessages, InitializeEnviroment):
    def __init__(self):
        try:
            super().__init__()
        except Exception as e:
            # lançar no final state
            pass
