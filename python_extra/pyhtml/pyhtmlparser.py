from html.parser import HTMLParser

class Pyhtmlparser(HTMLParser):
    """
    Pyhtml parser for outlining content
    """
    def handle_starttag(self, name, attrs):
        return {name: attrs}
