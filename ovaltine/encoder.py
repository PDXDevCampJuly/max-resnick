#!/usr/bin/env python3
"""
encoder module
"""
import sys


class Encoder():

    """
    Enocder class.
    """

    def __init__(self, *args):
        if len(args) >= 2:
            message = args[0]
            self.filename = args[1]
        elif len(args) >= 1:
            message = args[0]
            self.filename = 'secret.txt'
        elif len(args) == 0:
            print("At least a secret message is required.")

        self.process(message)

    def process(self, message):
        secret_message = self.transform(message)
        secret_message_file = self.make_secret(secret_message, self.filename)
        print("The secret has been stored at: {}".format(secret_message_file))

    def make_secret(self, secret_message, filename):
        with open(filename, 'w') as f:
            f.write(secret_message)
            return f.name

    def transform(self, message):
        ordinal_message = ""
        for char in message:
            ordinal_message += str(ord(char)) + " "
        return ordinal_message[:-1]

if __name__ == '__main__':
    Encoder(*sys.argv[1:])
