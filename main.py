import sys
from builders.builder import EnvironmentBuilder
from managers.file_manager import FileManager
from managers.whisper_manager import WhisperManager

try:
    environment = EnvironmentBuilder(sys.argv)
    configuration = environment.load_args().load_configuration().build()

    fileManager = FileManager(configuration["FILEPATH"], ['mp4'])
    fileManager.scan_dir()

    genSub = WhisperManager('medium', configuration)
    genSub.generate(fileManager)

except Exception as error:
    print(f'Error occurred: {error}')