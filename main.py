import os
import sys
from builders.builder import EnvironmentBuilder
from managers.file_manager import FileManager
from managers.whisper_manager import WhisperManager

try:
    environment = EnvironmentBuilder(sys.argv)

    environment.add_filepath()

    fileManager = FileManager(environment.configuration["filepath"], ['mp4'])

    fileManager.scan_dir()

    download_root = os.path.join(os.getcwd(), 'whisper_cache')

    genSub = WhisperManager('medium', path_root=None)

    genSub.generate(fileManager)

except Exception as error:
    print(f'Error occurred: {error}')