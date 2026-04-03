#!/usr/bin/env python3
"""
  Knowledge Journal - Project Euler - Problem 1 - Multiples of 3 or 5

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
    https://projecteuler.net/problem=1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    sum_mult_3 = utils.ap_sum(first=3, last=999, diff=3)
    sum_mult_5 = utils.ap_sum(first=5, last=995, diff=5)
    last_mult_15 = 1000//15 * 15
    sum_mult_15 = utils.ap_sum(first=15, last=last_mult_15, diff=15)

    return sum_mult_3 + sum_mult_5 - sum_mult_15


if  __name__ == "__main__":
    result = main()
    print(f"Knowledge Journal - Project Euler - Problem 1 with complexity O(1): {int(result)}")

