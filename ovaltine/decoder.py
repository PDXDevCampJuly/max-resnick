"""
decoder module
"""
import sys


class Decoder():

    """
    Enocder class.
    """

    def __init__(self, args):
        if len(args) >= 1:
            self.filename = args[0]
        elif len(args) == 0:
            self.filename = 'secret.txt'

        self.process()

    def process(self):
        secret_message = self.read_secret(self.filename)
        not_so_secret_message = self.decode(secret_message)
        print(not_so_secret_message)

    def read_secret(self, filename):
        with open(filename, 'r') as f:
            return f.read()

    def decode(self, message):
        decoded_message = ""
        for ordinal in message.split(sep=" "):
            decoded_message += chr(int(ordinal))
        return decoded_message

if __name__ == '__main__':
    Decoder(sys.argv[1:])
