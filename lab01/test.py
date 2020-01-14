#Name: Nathalie Ng
#ID: 500921963
import unittest
from mySolution import generate, calcScore

class Test(unittest.TestCase):

    def test_generate(self):
        #testing generate to make sure it generates a random string from the given letters
        self.assertEqual(generate(7, 3, "aaa"), "aaaaaaa", "Should be 'aaaaaaa'")

    def test_calculate(self):
        #testing calculate to make sure it calculates the score of how accurate the string is to the target string
        self.assertEqual(calcScore("hell ", "hello"), 80, "Should be 80")
        self.assertEqual(calcScore("moon", "mope"), 50, "Should be 50")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)