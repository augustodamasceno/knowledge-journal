#!/usr/bin/env python3
"""
This file is part of the Knowledge Journal
See https://github.com/augustodamasceno/knowledge-journal/
(Previously in the adlabs project)
"""
__author__ = "Augusto Damasceno"
__version__ = "1.1"
__copyright__ = "Copyright (c) 2020-2025, Augusto Damasceno."
__license__ = "All rights reserved"

# Comments are for humans!

#  Numeric Types: integers, floating point numbers, and complex numbers

# Integer (int)
age = 12

# Floating point (float)
pi = 3.14159265359

# Complex (complex)
impedance = 70.71 + 70.71j

# List
fruits = ['laranja', 'maca', 'uva', 'pera']

# Tuple
student = ('name', 'id')

# Range: start, stop, step
from_range_1 = list(range(10))
from_range_2 = list(range(1, 11))
from_range_3 = list(range(0, 30, 5))
from_range_4 = list(range(0, 10, 3))
from_range_5 = list(range(0, -10, -1))
from_range_6 = list(range(0))
from_range_7 = list(range(1, 0))

# Text (str)
string = 'Strings are immutable sequences of Unicode code points.'

# Dict
numbers = {'one': 1, 'two': 2, 'three': 3}
two = numbers['two']

# Truth value testing
#  All objects is true unless
#   Class defines either a __bool__() method that returns False or a __len__() method that returns zero;
#   Constants defined to be false: None and False.
#   Zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#   Empty sequences and collections: '', (), [], {}, set(), range(0)
true = True or 1 or list(range(10))
false = False and 0 and ''

# Built-in types we will not see in this class.
#   Binary Sequence Types — bytes, bytearray, memoryview.
#   Set Types — set, frozenset
#   Object oriented programming related.

# Put the breakpoint to debub in the next line!
the_end = True
