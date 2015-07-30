#!/usr/bin/env python3

from sys import argv
# take input

primes = [2, 3, 5]


def find_prime(maxvalue):
    global primes
    for num in range(7, int(maxvalue), 6):
        if is_prime(num):
            primes.append(num)
        if is_prime(num + 4) and (num + 4) < maxvalue:
            primes.append(num + 4)
    write(primes)


# is prime
def is_prime(num):
    if 0 not in [num % x for x in primes]:
        return True
    else:
        return False


def write(rows):
    """
    Takes a list, and writes to disk, as a row.
    """
    f = open('primes.txt', 'w')
    for row in rows:
        f.write(str(row) + '\n')
    f.close

def main():
    if len(argv) != 2:
        print(
            "Invalid number or arguments.",
            "{} requires 1 argument, ".format(argv[0]) +
            "the max number upto to find primes of.", sep="\n")
        exit()
    elif len(argv) == 2:
        find_prime(int(argv[1]))
    else:
        print("Unknown error has occured.")

if __name__ == '__main__':
    main()
