
class DirectoryNotFoundException(Exception):
    def __init__(self, message):            
        super().__init__(message)

class EnvironmentException(Exception):
    def __init__(self, message):
        super().__init__(message)
