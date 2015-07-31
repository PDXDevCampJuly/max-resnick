#!/usr/bin/env python3
from sys import argv
from collections import Counter
import pdb

"""
A small program to calculate prime factors of a given number.

"""
def read_from_file():
    """
    returns: list of primes in primes.txt
    """
    primes = []
    try:
        f = open('primes.txt', 'r')
        for row in f:
            primes.append(int(row))
        f.close()
        return primes
    except IOError:
        print("primes.txt not found.")


def find_prime_factor(num_to_factor, primes):
    """
    num_to_factor: num to find prime factors of.
    primes: list of primes, must be generated upto num to factor.
    """
    prime_factors = Counter()
    for index, mod in enumerate([num_to_factor % x for x in primes]):
        if mod == 0:
            prime_factors[primes[index]] += 1
            check_num = int(num_to_factor / primes[index])
            if check_num not in primes:
                # We need to factor this number more!
                return prime_factors, check_num
            elif check_num in primes:
                 prime_factors[primes[index]] += 1

    if len(prime_factors) == 0:
        print("no prime factors found.")
        exit()
    return prime_factors, 0


def print_factorization(num_to_factor, factors):
    # Set our color for the result
    result = "= " + "\033[92m"
    for factor in factors:
        if factors[factor] > 1:
            result += str(factor) + "^" + str(factors[factor]) + " * "
        elif factors[factor] >= 2:
            result += str(factor) + " * "
    # Cut the the last three chars from string.
    final = result[:-3]
    # result += "\033[0m"
    print("The prime facorization is: \n", "\t |--->", num_to_factor, final)

def main():
    # TODO Use argparse, and it would handle this automagically, including casting.
    if len(argv) != 2:
        print(
            "Invalid number or arguments.",
            "{} requires 1 argument, ".format(argv[0]) +
            "the max number upto to find primes of.", sep="\n")
        exit()
    elif len(argv) == 2:
        try:
            num_to_factor = int(argv[1])
        except TypeError:
            print("Please enter a number.")
        primes = read_from_file()
        prime_factors = Counter()
        while num_to_factor != 0:
            prime_factors_of_left_overs, num_to_factor = \
                find_prime_factor(num_to_factor, primes)
            prime_factors.update(prime_factors_of_left_overs)
        # Note we use the initial argument because it's already a string!
        print_factorization(argv[1], prime_factors)
        exit()
    else:
        # No clue what could cause this, but we're gonna catch it.
        print("Unknown error has occured.")
        exit()

if __name__ == '__main__':
    main()
