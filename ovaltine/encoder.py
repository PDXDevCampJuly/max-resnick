#!/usr/bin/env python3
"""
encoder module
"""
import argparse
from random import randint

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
        parser.add_argument('-s', '--secure',
                            help='make message more secure',
                            action="store_true",
                            default=False)
        args = parser.parse_args()
        message = args.message
        self.secure = args.secure
        self.filename = args.output
        self.process(message)

    def process(self, message):
        secret_message = self.transform(message)
        secret_message_file = self.make_secret(secret_message)
        print("The secret has been stored at: {}".format(secret_message_file))

    def make_secret(self, secret_message):
        """
        Writes to file given message to file.
        secret_message: a string to write out to set filename
        returns: nothing
        """
        with open(self.filename, 'w') as f:
            f.write(secret_message)
        return(self.filename)

    def transform(self, message):
        """
        Transforms message into an encoded message
        message: the message to transform as a string.
        return: the encoded message as string.
        """
        ordinal_message = ""
        for char in message:
            ordinal_char = str(ord(char))
            if self.secure:
                len_ordinal_char = len(ordinal_char)
                str_len_ordinal_char = str(len_ordinal_char)
                ordinal_message += str_len_ordinal_char + self.get_fluff(3) + \
                    ordinal_char + \
                    self.get_fluff(len_ordinal_char) + " "

            elif not self.secure:
                ordinal_message += ordinal_char + " "
        return ordinal_message[:-1]

    def get_fluff(self, num_digits):
        """
        num_digits: number of digits for ordinal, given 2 or 3
        returns: returns random number as string opposite of num_digits
        """
        if num_digits == 2:
            return str(randint(99, 999))
        elif num_digits == 3:
            return str(randint(31, 99))
        else:
            raise ValueError

if __name__ == '__main__':
    Encoder()
