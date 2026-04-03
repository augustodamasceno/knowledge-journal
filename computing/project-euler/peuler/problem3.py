#!/usr/bin/env python3
"""
  Knowledge Journal - Project Euler - Problem 3 - Largest Prime Factor


  Copyright (c) 2026, Augusto Damasceno.
  All rights reserved.

  SPDX-License-Identifier: BSD-2-Clause
"""

__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2026, Augusto Damasceno."
__license__ = "BSD-2-Clause"


import utils


def main():
    '''
    https://projecteuler.net/problem=3
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    '''

    #  Fundamental Theorem of Arithmetic:
    #    All integers greater than 1 has a unique prime factorization
    #
    #  Start with the number
    #  Start divisor with 2
    #  End loop if divisor * divisor if greater than the current number
    #  Search divisors
    #      when is divided, update number to number // divisor
    #      when is not divided, increment divisor by 1
    #
    #  Base case: the number has only one divisor. Examples:
    #  16 // 2 == 8
    #  8 // 2 == 4
    #  4 // 2 == 2
    #
    #  9 % 2 != 0
    #  9 // 3 == 3
    #
    #  25 % 2 != 0
    #  25 % 3 != 0
    #  25 % 4 != 0
    #  25 // 5 = 5
    #
    #  Non-base case when the number can be divided:
    #  Largest prime is the last number remaining when that
    #  not possible to divide again.
    #  Example:
    #  15 // 3 = 5
    #
    #  42 // 2 == 21
    #  21 // 3 == 7
    return utils.largest_prime_factor(600851475143)


if  __name__ == "__main__":
    result = main()
    print(f"Knowledge Journal - Project Euler - Problem 3 with Complexity O(sqrt(n)): {result}")