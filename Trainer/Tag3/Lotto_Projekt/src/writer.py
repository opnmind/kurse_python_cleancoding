
class FileWriter:
    def __init__(self, filename, mode="a"):
        self._filename = filename
        self._mode = mode

    
    def send(self, text: 'str'):
        with open(self._filename, self._mode) as fd:
            fd.write(text)
