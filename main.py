import os
from exceptions.directory_not_found_exception import DirectoryNotFoundException
from managers.file_manager import FileManager
from managers.whisper_manager import WhisperManager

try:
    fileManager = FileManager('C:\\Users\\danil\\Videos\\zero-hero-reflection-net\\zero-hero-reflection-net', ['mp4'])

    fileManager.readFile()

    download_root = os.path.join(os.getcwd(), 'whisper_cache')

    genSub = WhisperManager('medium', path_root=None)

    genSub.generate(fileManager)

except DirectoryNotFoundException as error:
    print(error)

except:  # noqa: E722
    print('Something wrong happen')