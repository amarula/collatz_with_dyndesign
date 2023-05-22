#!/usr/bin/env python3
import argparse
from dyndesign import mergeclasses

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Collatz sequence.')
    parser.add_argument('n', help='an integer to calculate the Collatz sequence')
    parser.add_argument('-c', action='store_true', dest='custom_collatz',
                        help='use custom Collatz instead')
    parser.add_argument('-g', action='store_true', dest='collatz_graph')
    parser.add_argument('-s', action='store_true', dest='collatz_statistics')
    args = parser.parse_args()

    classes_to_merge = [
        "components.collatz_sequence.CollatzSequence",
        "components.collatz_output.CollatzOutput"
    ]
    if args.custom_collatz:
        classes_to_merge.append("components.collatz_custom.CollatzCustom")
    if args.collatz_graph:
        classes_to_merge.append("components.collatz_graph.CollatzGraph")
    if args.collatz_statistics:
        classes_to_merge.append("components.collatz_statistics.CollatzStatistics")
    CollatzMerged = mergeclasses(
        *classes_to_merge,
        invoke_all=['output_number', 'output_wrapper']
    )

    collatz = CollatzMerged(args)
    collatz.output_sequence()
