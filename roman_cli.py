#!/usr/bin/env python

# PyRoman - Convert between Roman numeral and integer
# Copyright (C) 2019 ncdulo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
