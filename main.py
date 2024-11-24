import sys
from builders.builder import EnvironmentBuilder
from managers.file_manager import FileManager
from managers.whisper_manager import WhisperManager

try:
    environment = EnvironmentBuilder(sys.argv)
    environment.add_filepath().load_configuration().build()

    fileManager = FileManager(environment.configuration["FILEPATH"], ['mp4'])
    fileManager.scan_dir()

    genSub = WhisperManager('medium', environment)
    genSub.generate(fileManager)

except Exception as error:
    print(f'Error occurred: {error}')