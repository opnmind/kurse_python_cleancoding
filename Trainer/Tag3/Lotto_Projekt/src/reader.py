#class Reader(object): 2.7 style
class Reader: # implizit von object abstammend
    def __init__(self, filename):
        self._filename = filename

    def set_filename(self, filename):
        self._filename = filename

class FileReader(Reader):
    def __init__(self, filename):
        super().__init__(filename)

    def read(self):
        with open(self._filename) as fd:
            return fd.read()



