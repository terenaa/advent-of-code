import unittest

from day2 import solve_a, solve_b


class TestDay2(unittest.TestCase):
    def test_solve_a(self):
        self.assertEqual(150, solve_a(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))

    def test_solve_b(self):
        self.assertEqual(900, solve_b(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))


if __name__ == "__main__":
    unittest.main()
