# pyroman

Pyroman is a Roman numeral conversion library written for Python 3.6. Provided are the main library, unit tests, and a command line wrapper for the library. It can convert any integer number between 1 and 4,999 to a Roman numeral, or the same in reverse. Featuring dynamically generated lookup tables for a very fast execution.

The idea and source code for this project originally came from Dive Into Python 3 by Mark Pilgrim. 

### Basic Usage

#### Library
#### Command Line Wrapper
#### Gtk3 Wrapper
I have created a simple to use Gtk3 wrapper for use of the library without entering a Python shell or writing a script. Make sure `roman_gui.py` has execute permissions and the executable directly.

The output mode setting controls the type of input accepted and the type returned. Numeral mode accepts an integer and returns a Roman numeral. Integer mode accepts a Roman numeral and returns an integer. Note that Roman numeral input must be uppercase. Integer input must be whole numbers, greater than 0 but less than 4,999.

#### TODO
##### Library
##### Command Line Wrapper
##### Gtk3 Wrapper
 * Error checking for input
 * Exception handling and error output
 * Basic program description in the main window
 * Visual tweaks and enhancements

#### Unit Tests

### Current unit test results: Pass
```
-> % python roman_test.py -v
test_blank (__main__.FromRomanBadInput)
from_roman should fail with blank string ... ok
test_malformed_antecedents (__main__.FromRomanBadInput)
from_roman should fail with malformed antecedents ... ok
test_repeated_pairs (__main__.FromRomanBadInput)
from_roman should fail with repeated pairs of numerals ... ok
test_too_many_repeated_numerals (__main__.FromRomanBadInput)
from_roman should fail with too many repeated numerals ... ok
test_roundtrip (__main__.RoundTripCheck)
from_roman(to_roman(n)) == n for all n ... ok
test_negative (__main__.ToRomanBadInput)
to_roman should fail with negative input ... ok
test_non_integer (__main__.ToRomanBadInput)
to_roman should fail with non-integer input ... ok
test_too_large (__main__.ToRomanBadInput)
to_roman should fail with large input ... ok
test_zero (__main__.ToRomanBadInput)
to_roman should fail with 0 input ... ok
test_from_roman_known_values (__main__.ToRomanGoodInput)
from_roman should give known result with known input ... ok
test_to_roman_known_values (__main__.ToRomanGoodInput)
to_roman should give known result with known input ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.011s

OK
```
