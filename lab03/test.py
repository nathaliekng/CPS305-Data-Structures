#Nathalie Ng 500921963
import unittest
from mySolution import infixToPostfix

class Test(unittest.TestCase):

    def test1_infixToPostfix(self):
        self.assertEqual(infixToPostfix("( 2 + 2 ) ! + 8"), ('2 2 + ! 8 +', 32), "Should be ('2 2 + ! 8 +', 32)")
        self.assertEqual(infixToPostfix("( 2 + 5 ) ! + 9"), ('2 5 + ! 9 +', 5049), "Should be ('2 5 + ! 9 +', 5049)")
        self.assertEqual(infixToPostfix("( 2 + 3 + 4 + 5 ) ! * 2"), ('2 3 + 4 + 5 + ! 2 *', 174356582400), "Should be ('2 3 + 4 + 5 + ! 2 *', 174356582400)")
        self.assertEqual(infixToPostfix("5 ! - ( 9 + 7 * 4 ) + 4 / 2"), ('5 ! 9 7 4 * + - 4 2 / +', 85), "Should be ('5 ! 9 7 4 * + - 4 2 / +', 85)")
        self.assertEqual(infixToPostfix("2 ! + ( 3 * 9 )"), ('2 ! 3 9 * +', 29), "Should be ('2 ! 3 9 * +', 29)")
        self.assertEqual(infixToPostfix("2 / 2 * 2 / 4 + 9 - 5"), ('2 2 / 2 * 4 / 9 + 5 -', 4), "Should be ('2 2 / 2 * 4 / 9 + 5 -', 4)")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



