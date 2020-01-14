#Nathalie Ng 500921963
import unittest
from hashing import *

class Test(unittest.TestCase):

    def test_getTest(self):
        A=HashTable()
        A[54]="a"
        A[26]="b"
        A[93]="c"
        A[17]="d"
        A[31]="e"
        A[44]="f"
        A[55]="g"
        A[20]="h"
        A[20]="updated"
        #The "h" will be replaced with "updated" since index 20 is updated. 
        self.assertEqual(A.data, (['d', None, None, 'a', 'g', 'updated', None, None, 'c', 'b', 'f', None, None, None, 'e', None, None]))
   
    def test_testLength(self):
        C=HashTable()
        C[54]="a"
        C[26]="b"
        C[93]="c"
        C[17]="d"
        #Default size will be 11
        self.assertEqual(len(C.slots), (11))
        C[31]="e"
        C[44]="f"
        C[55]="g"
        C[20]="h"
        #New length after resizing
        self.assertEqual(len(C.slots), (17))

    def test_collisions(self):
        B = HashTable()
        #Default size is 11. 14%11 and 3%11 is 3. Fourteen takes up B[3], so three will take the next B[4]
        B[14] = "fourteen"
        B[3] = "three"
        self.assertEqual(B.data, ([None, None, None, 'fourteen', 'three', None, None, None, None, None, None]))
        #size should still be 11. 10%11 = 1 and 1%11 = 1
        B[1] = "one"
        B[11] = "eleven"
        self.assertEqual(B.data, (['eleven', 'one', None, 'fourteen', 'three', None, None, None, None, None, None]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



