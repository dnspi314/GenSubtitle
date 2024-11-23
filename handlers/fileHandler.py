import os

from models.models import Directory, File


class FileHandler:
    def __init__(self, path_dir, file_extensions):
        self.path_dir = path_dir
        self.list = []
        self.file_extensions = file_extensions

    def readFile(self):
        if not os.path.isdir(self.path_dir):
            raise Exception(f'Directory {self.path_dir} not found!!!')
        
        directory = Directory(self.path_dir)

        files = os.listdir(self.path_dir)

        for file in files:
            extension = file[-3::]
            if extension in self.file_extensions:
               fileObj = File(file)
               directory.addFile(fileObj)                

        return self
    
    def desc(self):
        self.list = sorted(self.list, reverse=True)

        return self
    
    def asc(self):
        self.list = sorted(self.list)

        return self