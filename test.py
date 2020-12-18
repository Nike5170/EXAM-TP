import unittest
from fib import fibon


class TestProgression(unittest.TestCase):
    fib = fibon(1)

    def test_fibon__(self):
        self.assertEqual(self.fib(3), 5.5600000000000005)
        self.assertEqual(self.fib.fibon(2.44), 5)
        self.assertTrue(self.fib.fibon(487), isinstance(self.fib.fibon(487), float))


if __name__ == '__main__':
    unittest.main()
