#!/usr/bin/env python3
"""
decoder module
"""
import argparse


class Decoder():

    """
    Enocder class.
    """

    def __init__(self):
        parser = argparse.ArgumentParser(description="Decode a message.")
        parser.add_argument('-i', '--input',
                            help='input file for encrypted message',
                            default='secret.txt')
        args = parser.parse_args()
        self.filename = args.input
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
    Decoder()
