from html.parser import HTMLParser


class Pyhtmlparser(HTMLParser):
    """
    Custom Pyhtml parser
    """

    def __init__(self, *args):
        HTMLParser.__init__(self)
        self.start_tags = []
        self.end_tags = []

    def handle_starttag(self, name, attrs):
        self.start_tags.append(name)
        if name == "h1":
            print(name, self.getpos())

    def handle_endtag(self, name):
        self.end_tags.append(name)

    def get_tags(self):
        return self.start_tags, self.end_tags
