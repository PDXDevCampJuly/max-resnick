#!/usr/bin/env python3
# This is a dice faking module
from random import randint


def roll(max):
    the_roll = randint(1, max)
    return the_roll


def roll_a_bunch(max, number_of_dice=4):
    rolls = []
    for i in range(number_of_dice):
        rolls.append(roll(max))

    return rolls


def roll_distro(max, number_of_dice=4):
    rolls = roll_a_bunch(max, number_of_dice)
    distribution = {}
    for each in rolls:
        distribution.get(each, 0)
        distribution[each] += 1
    return distribution

def main():
    roll_distro()
