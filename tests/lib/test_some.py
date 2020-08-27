import unittest

from lib.some import some


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(some(), 42)


if __name__ == '__main__':
    unittest.main()
