from exceptions.exception import InvalidArguments

class EnvironmentBuilder:
    def __init__(self, args:list):
        self.args = args
        self.configuration = {}

    def add_filepath(self):
        if len(self.args) > 2:
            raise InvalidArguments("Please, verifiy amount of the arguments. Must be equals 2 elements.")
        
        self.configuration["filepath"] = self.args[1]

        return self
    