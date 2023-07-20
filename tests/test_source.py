import unittest

from calculate.source import reverse_str
from calculate.source import is_prime


class TestReverseStr(unittest.TestCase):
    def test_should_reverse_string_with_digits(self):
        self.assertEqual(reverse_str('123'), '321')

    def test_should_not_reverse_string(self):
        self.assertEqual(reverse_str('abc'), 'abc')


class TestIsPrime(unittest.TestCase):
    def test_should_return_true_with_prime_number(self):
        self.assertEqual(is_prime(5), True)

    def test_should_return_false_with_none_prime_number(self):
        self.assertEqual(is_prime(22), False)

    def test_should_return_false_with_number_1(self):
        self.assertFalse(is_prime(1))


if __name__ == "__main__":
    unittest.main()
