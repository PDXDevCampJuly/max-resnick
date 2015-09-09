from pyhtml.file import File
from pyhtml.pyhtmlparser import Pyhtmlparser

class Pyhtml:
    def __init__(self, filename):
        self.to_parse = File(filename).open_file()

    def start_proceess(self):
        parser = Pyhtmlparser()
        return parser
