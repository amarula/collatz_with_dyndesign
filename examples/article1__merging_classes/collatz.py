#!/usr/bin/env python3
import argparse

class Collatz:
    FUNCTION_NAME = 'Collatz'

    def __init__(self, n):
        self.n = int(n)

    def get_next_n(self, n):
        if n % 2 == 0:
            return n // 2
        else:
            return n*3 +1

    def get_collatz_sequence(self, n):
        while n != 1:
            n = self.get_next_n(n)
            yield n

    def output_number(self, n):
        print(f"{n}; ", end='')

    def output_sequence(self):
        print(f"{self.FUNCTION_NAME} sequence starting from {self.n} is:")
        self.output_number(self.n)
        for n in self.get_collatz_sequence(self.n):
            self.output_number(n)
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Collatz sequence.')
    parser.add_argument('n')
    args = parser.parse_args()

    collatz = Collatz(args.n)
    collatz.output_sequence()
