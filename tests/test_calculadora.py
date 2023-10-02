import unittest
import calculadora


class TestUtils(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(10,calculadora.sum(5,5))

    def test_multiply(self):
        self.assertEqual(25,calculadora.multiply(5,5))


if __name__ == '__main__':
    unittest.main()