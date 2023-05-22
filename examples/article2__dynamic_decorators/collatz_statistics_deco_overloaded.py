#!/usr/bin/env python3
import argparse
from dyndesign import mergeclasses, decoratewith
import matplotlib.pyplot as plt

class CollatzGraph:
    def output_number(self, n):
        self.sequence.append(n)

    def output_wrapper(self, func):
        self.sequence = []
        func(self)
        plt.plot(self.sequence)
        plt.xlabel("Step")
        plt.ylabel("Value")
        plt.title(f"{self.FUNCTION_NAME} Function")
        plt.show()


class CollatzStatistics:
    def output_number(self, n):
        self.max = max(self.max, n)
        self.count += 1

    def output_wrapper(self, func):
        self.max = 0
        self.count = 0
        func(self)
        print(f"Max value reached: {self.max}")
        print(f"Sequence length: {self.count}")


class CollatzSequence:
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


class CollatzCustom:
    FUNCTION_NAME = 'Collatz-like ternary'

    def get_next_n(self, n):
        if n % 3 == 0:
            return n // 3
        elif n % 3 == 1:
            return n*2 +1
        else:
            return n*3 -2


class CollatzOutput:
    def output_number(self, n):
        print(f"{n}; ", end='')

    @decoratewith("output_wrapper")
    def output_sequence(self):
        print(f"{self.FUNCTION_NAME} sequence starting from {self.n} is:")
        self.output_number(self.n)
        for n in self.get_collatz_sequence(self.n):
            self.output_number(n)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Collatz sequence.')
    parser.add_argument('n', help='an integer to calculate the Collatz sequence')
    parser.add_argument('-c', action='store_true', dest='custom_collatz', help='use custom Collatz instead')
    parser.add_argument('-g', action='store_true', dest='collatz_graph')
    parser.add_argument('-s', action='store_true', dest='collatz_statistics')
    args = parser.parse_args()

    CollatzMerged = mergeclasses(CollatzSequence, CollatzOutput)
    if args.custom_collatz:
        CollatzMerged = mergeclasses(CollatzMerged, CollatzCustom)
    if args.collatz_graph:
        CollatzMerged = mergeclasses(CollatzMerged, CollatzGraph, invoke_all=['output_number'])
    if args.collatz_statistics:
        CollatzMerged = mergeclasses(CollatzMerged, CollatzStatistics, invoke_all=['output_number', 'output_wrapper'])

    collatz = CollatzMerged(args.n)
    collatz.output_sequence()
