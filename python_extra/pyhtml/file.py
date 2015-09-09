from os import path

class File:
    """
    A class for handling a file
    """
    def __init__(self, fullfilename):
        """
        input: path and filename of file as a single string.
        """
        self.filepath, self.filename = self.file_path_name(fullfilename)

    def file_path_name(self, fullfilename):
        """
        input: full filename and location of file
        return: absolute path, and filename if they exist
        """
        # we're double checking to make sure we are a file.
        if path.isfile(fullfilename):
            return path.split(path.realpath(fullfilename))
        else:
            return "File at {} not found".format(fullfilename)

    def open_file(self):
        """
        opens file into a string
        returns string from instance file.
        """
        string_of_html = ""
        with open(path.join(self.filepath, self.filename), "r", encoding="utf-8") as f:
            for row in f:
                string_of_html += row
        return string_of_html
