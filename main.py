# Arquivo principal
from log import LogMessages

class Main(LogMessages):
    def __init__(self):
        super().__init__()
    
    def starting(self):
        # Chama o método de log debug
        self.log_message_debug("ola ola ola")
    
    def main(self):
        # Executa o fluxo principal
        self.starting()
        self.log_message()  # Opcional

# Criar uma instância e chamar o método principal
oi = Main()
oi.main()
