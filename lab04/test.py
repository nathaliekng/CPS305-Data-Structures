#Nathalie Ng 500921963
import unittest
from mySolution import power, powerH, binomial

class Test(unittest.TestCase):

    def test_infixToPostfix(self):
        self.assertEqual(power(2, 0), 1, "Should be 1")
        self.assertEqual(power(3, 3), 27, "Should be 27")
        self.assertEqual(power(10, 2), 100, "Should be 100")
        self.assertEqual(power(-12, 2), 144, "Should be 144")
        self.assertEqual(power(5, 6), 15625, "Should be 15625")

    def test_powerH(self):
        self.assertEqual(powerH(2, 4), 16, "Should be 16")
        self.assertEqual(powerH(2, 5), 32, "Should be 32")
        self.assertEqual(powerH(2, 0), 1, "Should be 1")
        self.assertEqual(powerH(-4, 3), -64, "Should be -64")

    def test_binomial(self):
        self.assertEqual(binomial(10, 6), 210, "Should be 210")
        self.assertEqual(binomial(20, 0), 1, "Should be 1")
        self.assertEqual(binomial(5, 5), 1, "Should be 1")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)