import os

from exceptions.directory_not_found_exception import DirectoryNotFoundException
from models.models import Directory, File


class FileManager:
    def __init__(self, path_dir, file_extensions):
        self.path_dir = path_dir
        self.directory = None
        self.file_extensions = file_extensions

    def scanDir(self):
        if not os.path.isdir(self.path_dir):
            raise DirectoryNotFoundException(f'Directory {self.path_dir} not found!!!')
        
        self.directory = Directory(self.path_dir)

        files = os.listdir(self.path_dir)
        for file in files:
            extension = file[-3::]
            if extension in self.file_extensions:
               fileObj = File(file)
               self.directory.addFile(fileObj)                

        return self
    
    def descList(self):
        self.list = sorted(self.list, reverse=True)

        return self
    
    def ascList(self):
        self.list = sorted(self.list)

        return self