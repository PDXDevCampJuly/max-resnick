from pyhtml.file import File
from pyhtml.pyhtmlparser import Pyhtmlparser

class Pyhtml:
    def __init__(self, filename):
        self.to_parse = File(filename)

    def wtf(self):
       string_of_html = self.to_parse.open_file()
       parser = Pyhtmlparser(string_of_html)
       return parser
