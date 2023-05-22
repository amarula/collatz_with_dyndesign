#!/usr/bin/env python3
import argparse
from collatz_class_builder import CollatzClassBuilder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Collatz sequence.')
    parser.add_argument('n', help='an integer to calculate the Collatz sequence')
    parser.add_argument('-c', action='store_true', dest='CollatzCustom')
    parser.add_argument('-m', type=int, dest='CollatzMultiple')
    parser.add_argument('-g', action='store_true', dest='CollatzGraph')
    parser.add_argument('-s', action='store_true', dest='CollatzStatistics')
    args = parser.parse_args()

    class_builder = CollatzClassBuilder(args)
    CollatzClass = class_builder.build_class()

    collatz = CollatzClass(args)
    collatz.output_sequence()
