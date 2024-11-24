import os
from dotenv import dotenv_values
from exceptions.exception import InvalidArguments

class EnvironmentBuilder:
    def __init__(self, args:list):
        self.args = args
        self.configuration = {}

    def add_filepath(self):
        if len(self.args) > 2:
            raise InvalidArguments("Please, verifiy amount of the arguments. It must be equals 2 elements.")
        
        self.configuration["FILEPATH"] = self.args[1]

        return self
    
    def load_configuration(self):
        dotenv_path = os.path.join(os.getcwd(), '.env')

        env_vars = dotenv_values(dotenv_path=dotenv_path)

        for key, value in env_vars.items():
            if len(value) > 0: 
                self.configuration[key] = value

        return self
    