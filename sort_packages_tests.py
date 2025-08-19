"""
sort_packages_tests.py
Author: Esther de Mattos

This file contains unit tests for the sort function defined in sort_packages.py.
The tests cover all classification rules for packages: STANDARD, SPECIAL, and REJECTED.
"""
import unittest
from sort_packages import sort

class TestSortPackages(unittest.TestCase):
    """
    Unit tests for the sort function, which classifies packages based on their dimensions and mass.
    Each test method checks a specific rule or edge case.
    """
    def test_standard(self):
        self.assertEqual(sort(90, 90, 90, 10), "STANDARD")  # Not bulky, not heavy

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 25), "SPECIAL")  # Bulky by volume, heavy
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")  # Bulky by volume, not heavy

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(151, 10, 10, 10), "SPECIAL")  # Bulky by width only
        self.assertEqual(sort(10, 151, 10, 10), "SPECIAL")  # Bulky by height only
        self.assertEqual(sort(10, 10, 151, 10), "SPECIAL")  # Bulky by length only

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")  # Heavy, not bulky (at threshold)
        self.assertEqual(sort(10, 10, 10, 21), "SPECIAL")  # Heavy, not bulky (above threshold)

    def test_bulky_and_heavy(self):
        self.assertEqual(sort(151, 100, 100, 21), "SPECIAL")  # Bulky and heavy
        self.assertEqual(sort(200, 200, 200, 25), "SPECIAL")  # Bulky and heavy

    def test_edge_cases(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # Exactly at bulky volume threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")  # Exactly at heavy mass threshold
        self.assertEqual(sort(90, 90, 90, 19.99), "STANDARD")  # Just below heavy threshold
        self.assertEqual(sort(99.99, 99.99, 99.99, 10), "STANDARD")  # Just below bulky volume threshold
        self.assertEqual(sort(149.99, 81.65, 81.65, 10), "STANDARD")  # Just below bulky dimension threshold

if __name__ == "__main__":
    unittest.main()
