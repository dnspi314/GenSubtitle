import os
import torch
import whisper
import whisper.transcribe

from managers.file_manager import FileManager
from utils.util import write_srt 

class WhisperManager:
    def __init__(self, model_name:str, path_root:str=None):
        self.language = 'English'
        self.temperature = 0
        self.verbose = True
        self.gpu_enable = torch.cuda.is_available()
        device = "cuda" if self.gpu_enable else "cpu"
        self.model = whisper.load_model(model_name, download_root=path_root, device=device)


    def add_temperature(self, temperature:float):
        self.temperature = temperature


    def generate(self, fileManager: FileManager):
        for f in fileManager.directory.files:
            print(f'Generate subtitle for {f.name}\n')
            srt_file = os.path.join(fileManager.directory.name, str.replace(f.name, f.extension, 'srt'))

            if os.path.isfile(srt_file):
                print(f'File {srt_file} already generated.')
                continue
            
            dst = os.path.join(fileManager.directory.name, f.name)
            result = self.model.transcribe(
                dst, 
                language=self.language, 
                fp16=self.gpu_enable, 
                temperature=self.temperature, 
                verbose=self.verbose
            )

            # save SRT
            with open(srt_file, "w", encoding="utf-8") as srt:
                write_srt(result["segments"], file=srt)

            print('generated sucessfully!!!\n')

        print('All subtitle generated.')
