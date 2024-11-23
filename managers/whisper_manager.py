import os
import torch
import whisper
import whisper.transcribe

from managers.file_manager import FileManager 

class WhisperManager:
    def __init__(self, model_name:str, path_root:str=None):
        self.language = 'English'
        self.temperature = 0
        self.verbose = True
        self.gpu_enable = torch.cuda.is_available()
        device = "cuda" if self.gpu_enable else "cpu"
        self.model = whisper.load_model(model_name, download_root=path_root, device=device)


    def addTemperature(self, temperature:float):
        self.temperature = temperature


    def generate(self, fileManager: FileManager):
        for f in fileManager.directory.files:
            
            srt_file = os.path.join(fileManager.directory.name, str.replace(f.name, f.extension, 'srt'))

            if os.path.isfile(srt_file):
                print(f'File {srt_file} already generated.')
                continue
            
            dst = os.path.join(fileManager.directory.name, f.name)
            self.model.transcribe(
                dst, 
                language=self.language, 
                fp16=self.gpu_enable, 
                temperature=self.temperature, 
                verbose=self.verbose
            )