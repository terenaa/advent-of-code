import unittest

from day1 import solve_a, solve_b


class TestDay1(unittest.TestCase):
    def test_solve_a(self):
        self.assertEqual(7, solve_a([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))

    def test_solve_b(self):
        self.assertEqual(5, solve_b([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))


if __name__ == "__main__":
    unittest.main()
