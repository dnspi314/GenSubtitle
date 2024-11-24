import os
from dotenv import dotenv_values
from exceptions.exception import EnvironmentException

class EnvironmentBuilder:
    def __init__(self, args:list):
        self.args = args
        self.configuration = {}

    def load_args(self):
        if len(self.args) != 2:
            raise EnvironmentException("Por favor verifique se o argumento passado via linha de commando foi passado corretamente. Deve ter somente 1 argumento.")
        
        self.configuration["FILEPATH"] = self.args[1]

        return self
    
    def load_configuration(self):
        dotenv_path = os.path.join(os.getcwd(), '.env')

        env_vars = dotenv_values(dotenv_path=dotenv_path)

        for key, value in env_vars.items():
            if len(value) > 0: 
                self.configuration[key] = value

        return self
    
    def build(self):
        if len(self.configuration) == 0:
            raise EnvironmentException("Você precisa contruir as configurações.")
        
        return self.configuration
    