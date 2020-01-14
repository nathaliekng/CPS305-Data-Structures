#Nathalie Ng 500921963
import unittest
from eval import *

class Test(unittest.TestCase):

    def test_mo3(self):
        tree1=["*", ["a", [],[]], ["b", [],[]]]
        env1 = [["a",5], ["b", 10],["c",15]]
        #Test if function works with a simple tree
        self.assertEqual(evalTree(tree1, env1), 50)
        tree2 = ["+", ["a", [], []], ["*", ["b", [] , []], ["c", [],[]]]] 
        self.assertEqual(evalTree(tree2, env1), 155)
        tree3=["/", ["a", [], []], ["b", [], []]]
        env3 = [["a", 5], ["b", 0]]
        #Test if it works when a number is divided by 0 (undefined)
        self.assertEqual(evalTree(tree3, env3), "Can not divide by zero")
        tree4 = ["*", ["+", ["a", [], []], ["b", [],[]]], ["+", ["b", [] , []], ["c", [],[]]]] 
        tree5 = ["*", ["+", ["10", [], []], ["20", [],[]]], ["*", ["+", ["20", [] ,[]], ["30", [],[]]], ["10", [], []]]] 
        #Test for order of operation with parenthesis
        self.assertEqual(evalTree(tree4, env1), 375)
        self.assertEqual(evalTree(tree5, env1), 15000)
        tree6=["x1", [],[]]
        env6=[["a", 10], ["x1", 20]]
        #Test if variable is alphanumeric (not just alpha)
        self.assertEqual(evalTree(tree6, env6), 20)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

