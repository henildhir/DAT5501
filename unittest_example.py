import unittest
from my_function import even_or_odd

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def test_add(self):

        # test adding negative integers
        self.assertEqual(even_or_odd(4),even_or_odd(6),even_or_odd(5))

        # test adding floats"
        self.assertEqual(even_or_odd(1),even_or_odd(3),even_or_odd(9))

# run the tests
if __name__ == "__main__":
    unittest.main()