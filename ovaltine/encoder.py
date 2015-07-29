#!/usr/bin/env python3
"""
encoder module
"""
import argparse


class Encoder():

    """
    Enocder class.
    """

    def __init__(self):

        parser = argparse.ArgumentParser(description="Encode a message.")
        parser.add_argument('-m', '--message',
                            help='messeage to encrypt',
                            required=True)
        parser.add_argument('-o', '--output',
                            help='output file for encrypted message',
                            default='secret.txt')

        args = parser.parse_args()
        message = args.message
        self.filename = args.output
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
    Encoder()
