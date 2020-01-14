#Nathalie Ng 500921963
import unittest
from parserTools import *

class Test(unittest.TestCase):

    def test(self):
        #Test if function works with a simple tree
        x=['4','+','5','-','10']
        self.assertEqual(parse(x), ['-', ['+', ['4', [], []], ['5', [], []]], ['10', [], []]])
        x2=['4','+','3','/','10','+','2','*','5']
        self.assertEqual(parse(x2), ['+', ['+', ['4', [], []], ['/', ['3', [], []], ['10', [], []]]], ['*', ['2', [], []], ['5', [], []]]])
        x3=['4','+','2','!']
        self.assertEqual(parse(x3), ['+',['4',[],[]], ['!',['2',[],[]],[]]])
        x4=['4','+',['2','!']]
        self.assertEqual(parse(x4), ['+',['4',[],[]], ['!',['2',[],[]],[]]])
        x5=[['4','/','2'],'!']
        self.assertEqual(parse(x5), ['!',['/',['4',[],[]],['2',[],[]]],[]])
        x6=['5']
        self.assertEqual(parse(x6), ['5',[],[]]]
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
