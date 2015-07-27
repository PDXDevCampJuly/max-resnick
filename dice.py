#!/usr/bin/env python3
# This is a dice faking module

from random import randint

def roll(max):
    the_roll = randint(1, max)
    print("You rolled a: {}".format(the_roll))
