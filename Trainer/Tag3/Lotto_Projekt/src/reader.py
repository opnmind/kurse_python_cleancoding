class FileReader:
    def __init__(self, filename):
        self._filename = filename

    def read(self) -> 'str':
        with open(self._filename) as fd:
            return fd.read()



