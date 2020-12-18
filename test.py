import unittest
from fib import fibon


class TestProgression(unittest.TestCase):
    fib = fibon(1)
    fib2 = fibon(3)
    fib3 = fibon(20)
    def test_fibon__(self):
        self.assertEqual(self.fib, 2)
        self.assertEqual(self.fib2, 5)
        self.assertEqual(self.fib3, 17711)


if __name__ == '__main__':
    unittest.main()
