import json
import os
import torch
import whisper
import whisper.transcribe

from managers.file_manager import FileManager
from utils.util import write_srt 

class WhisperManager:
    def __init__(self, configuration:list, path_root:str=None):
        self.language = configuration['LANGUAGE']
        self.temperature = float(configuration['TEMPERATURE'])
        self.verbose = json.loads(configuration['VERBOSITY'].lower())
        self.gpu_enable = torch.cuda.is_available()
        device = 'cuda' if self.gpu_enable else 'cpu'
        self.model = whisper.load_model(
            configuration['MODEL_NAME'], 
            download_root=path_root, 
            device=device
        )

    def generate(self, fileManager: FileManager):
        for f in fileManager.directory.files:
            print('*' * 20)
            print(f'Gerando legenda {f.name}')
            srt_file = os.path.join(fileManager.directory.name, str.replace(f.name, f.extension, 'srt'))

            if os.path.isfile(srt_file):
                print(f'Arquivos {srt_file} já foi gerado.')
                continue
            
            dst = os.path.join(fileManager.directory.name, f.name)
            result = self.model.transcribe(
                dst, 
                language=self.language, 
                fp16=self.gpu_enable, 
                temperature=self.temperature, 
                verbose=self.verbose,
                max_initial_timestamp=0
            )

            # save SRT
            with open(srt_file, "w", encoding="utf-8") as srt:
                write_srt(result["segments"], file=srt)

            print('Legenda gerada com sucesso!!!\n')
            print('*' * 20)

        print('Finalizado.')
