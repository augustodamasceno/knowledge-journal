#!/usr/bin/env python3
"""
  Knowledge Journal - Project Euler - Utilities

  Copyright (c) 2026, Augusto Damasceno.
  All rights reserved.

  SPDX-License-Identifier: BSD-2-Clause
"""

__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2026, Augusto Damasceno."
__license__ = "BSD-2-Clause"

import numbers


def ap_sum(first, last, diff, num_terms=None):
    if num_terms:
        verify = [first, last, num_terms]
    else:
        verify = [first, last, diff]

    for value in verify:
        if not isinstance(value, numbers.Number):
            raise TypeError(f"Argument must be a number, not {type(value)}")

    if num_terms is None:
        num_terms = (last - first) / diff + 1

    return (num_terms/2) * (first + last)


if __name__ == "__main__":
    print("Knowledge Journal - Project Euler - Utilities")