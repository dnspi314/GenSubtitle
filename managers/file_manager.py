import os

from exceptions.exception import DirectoryNotFoundException
from models.models import Directory, File


class FileManager:
    def __init__(self, path_dir, *include_extensions):
        self.path_dir = path_dir
        self.directory = None
        self.include_extensions = include_extensions

    def scan_dir(self):
        if not os.path.isdir(self.path_dir):
            raise DirectoryNotFoundException(f'Directory {self.path_dir} not found!!!')
        
        self.directory = Directory(self.path_dir)

        files = os.listdir(self.path_dir)
        for file in files:
            extension = file[-3::]
            if extension in self.include_extensions:
               fileObj = File(file)
               self.directory.addFile(fileObj)                

        return self
    
    def files_order_desc(self):
        self.list = sorted(self.list, reverse=True)

        return self
    
    def files_order_asc(self):
        self.list = sorted(self.list)

        return self