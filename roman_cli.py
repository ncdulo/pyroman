#!/usr/bin/python

import roman

import argparse

def parse_command_line_args():
    '''Load a dictionary with pairs of command line arguments and return them'''
    # Create a new argument parser object
    parser = argparse.ArgumentParser(description='convert between Roman numeral and integer')

    # A mutually exclusive group means only one of the items within may be selected
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-i', '--integer', action='store_true', help='convert to Roman Numeral to integer')
    mode.add_argument('-n', '--numeral', action='store_true', help='convert integer to Roman numeral')

    # Add the rest of our arguments
    parser.add_argument('number', help='integer or numeral expressing the number to convert')
    parser.add_argument('-v', '--verbose', action='store_true',
            help='increase output verbosity')

    # Parse and return the arguments
    args = parser.parse_args()

    return args



def main():
    '''Main program entry point'''

    # Run our command line argument parser and collect the results into an object
    args = parse_command_line_args()

    # Print some extra information if you like
    if args.verbose:
        print('Number: {0}'.format(args.number))
        print('Numeral: {0}'.format(args.numeral))
        print('Integer: {0}'.format(args.integer))

    # If we are converting to Roman  numeral..
    if args.numeral:
        print(roman.to_roman(int(args.number)))
    # If we are converting to integer..
    elif args.integer:
        print(roman.from_roman(args.number))


if __name__ == '__main__':
    main()
