import unittest

from day3 import solve_a, solve_b


class TestDay3(unittest.TestCase):
    def test_solve_a(self):
        self.assertEqual(198, solve_a(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000",
                                       "11001", "00010", "01010"]))

    def test_solve_b(self):
        self.assertEqual(230, solve_b(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000",
                                       "11001", "00010", "01010"]))


if __name__ == "__main__":
    unittest.main()
