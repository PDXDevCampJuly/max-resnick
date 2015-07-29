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
        """
        Flow control function
        """
        secret_message = self.read_secret(self.filename)
        not_so_secret_message = self.decode(secret_message)
        print(not_so_secret_message)

    def read_secret(self, filename):
        """
        filename: name of file in the current working dirtectory.
        returns string of content from given filename.
        """
        try:
            with open(filename, 'r') as f:
                secret_file = f.read()
            return secret_file
        except IOError:
            print("input file: {} not found.".format(self.filename))
            exit()

    def decode(self, message):
        """
        decode funcation automagically attemtps to tell if the message is
            encoded with the `-s` option.
        message: encoded message
        """
        decoded_message = ""
        try:
            for ordinal in message.split(sep=" "):
                if len(ordinal) <= 3:
                    # We check for simple ordinal encoding
                    continue
                elif len(ordinal) == 8:
                    num_ordinal_digits_with_offset = int(ordinal[:1]) + 3
                    ordinal = ordinal[3:num_ordinal_digits_with_offset]
                else:
                    # Someone is throwing dirty things at us.
                    raise ValueError
                decoded_message += chr(int(ordinal))
        except ValueError:
            print("Unkown message type.")
            exit()
        return decoded_message

if __name__ == '__main__':
    Decoder()
