#!/usr/bin/env python3
"""
  Knowledge Journal - Project Euler - Unit Tests - utils

  Copyright (c) 2026, Augusto Damasceno.
  All rights reserved.

  SPDX-License-Identifier: BSD-2-Clause
"""

__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2026, Augusto Damasceno."
__license__ = "BSD-2-Clause"


import unittest

from peuler.utils import ap_sum


class TestApSum(unittest.TestCase):

    def test_natural_numbers_1_to_10(self):
        self.assertEqual(ap_sum(first=1, last=10, diff=1), 55)

    def test_single_term(self):
        self.assertEqual(ap_sum(first=7, last=7, diff=1), 7)

    def test_two_terms(self):
        self.assertEqual(ap_sum(first=3, last=9, diff=6), 12)

    def test_even_step(self):
        self.assertEqual(ap_sum(first=0, last=10, diff=2), 30)

    def test_negative_first_term(self):
        self.assertEqual(ap_sum(first=-5, last=0, diff=1), -15)

    def test_large_sequence(self):
        self.assertEqual(ap_sum(first=1, last=100, diff=1), 5050)

    def test_num_terms_keyword(self):
        self.assertEqual(ap_sum(first=1, last=9, diff=2, num_terms=5), 25)

    def test_all_same_terms_via_num_terms(self):
        self.assertEqual(ap_sum(first=5, last=5, diff=0, num_terms=4), 20)

    def test_type_error_first_not_number(self):
        with self.assertRaises(TypeError):
            ap_sum(first="a", last=10, diff=1)

    def test_type_error_last_not_number(self):
        with self.assertRaises(TypeError):
            ap_sum(first=1, last="z", diff=1)

    def test_type_error_diff_not_number(self):
        with self.assertRaises(TypeError):
            ap_sum(first=1, last=10, diff="d")

    def test_type_error_num_terms_not_number(self):
        with self.assertRaises(TypeError):
            ap_sum(first=1, last=10, diff=1, num_terms="five")

    def test_zero_diff_raises_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            ap_sum(first=1, last=10, diff=0)


if __name__ == '__main__':
    unittest.main()
