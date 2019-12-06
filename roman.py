import re

class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError):
    pass

class InvalidRomanNumeralError(ValueError):
    pass


roman_numeral_map = (('M',  1000),
                     ('CM',  900),
                     ('D',   500),
                     ('CD',  400),
                     ('C',   100),
                     ('XC',   90),
                     ('L',    50),
                     ('XL',   40),
                     ('X',    10),
                     ('IX',    9),
                     ('V',     5),
                     ('IV',    4),
                     ('I',     1))

roman_numeral_pattern = re.compile('''
        ^                   # beginning of string
        M{0,4}              # thousands
        (CM|CD|D?C{0,3})    # hundreds
        (XC|XL|L?X{0,3})    # tens
        (IX|IV|V?I{0,3})    # ones
        $                   # end of string
        ''', re.VERBOSE)

def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 5000):
        raise OutOfRangeError('number out of range (must be 1..4999)')

    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer

    return result

def from_roman(s):
    '''convert Roman numeral to integer'''
    if not s:
        raise InvalidRomanNumeralError('Input can not be blank')
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result

