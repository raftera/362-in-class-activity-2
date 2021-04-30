import unittest
import calc


class TestCase(unittest.TestCase):

    def test_addition(self):
     result = calc.addition(4,3)
     self.assertEqual(result, 7)

    def test_subtraction(self):
       result = calc.subtraction(4,3)
       self.assertEqual(result, 1)

    def test_multiplication(self):
     result = calc.multiplication(4,3)
     self.assertEqual(result, 12)

    def test_division(self):
     result = calc.division(12,3)
     self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()



