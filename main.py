import sys
from builders.builder import EnvironmentBuilder
from managers.file_manager import FileManager
from managers.whisper_manager import WhisperManager

try:
    environment = EnvironmentBuilder(sys.argv)
    configuration = environment.load_args().load_configuration().build()

    file_manager = FileManager(configuration["FILEPATH"], 'mp4')
    file_manager.scan_dir()

    whisper_manager = WhisperManager(configuration)
    whisper_manager.generate(file_manager)

except Exception as error:
    print(f'Error occurred: {error}')