class File:
    def __init__(self, name: str):
        self.name = name
        self.extension = name[-3::]

class Directory:
    def __init__(self, name:str):
        self.name = name
        self.files = []

    def addFile(self, file: File):
        self.files.append(file)
