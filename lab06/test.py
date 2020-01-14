#Nathalie Ng 500921963
import unittest
from sorting import *

class Test(unittest.TestCase):

    def test_mo3(self):
        list1=[90,1,2,3,28,39,12,42]
        mo3_quickSort(list1)
        self.assertEqual(list1, [1, 2, 3, 12, 28, 39, 42, 90])
        list2=[-80,2,31,41,23,-32,76,1]
        mo3_quickSort(list2)
        self.assertEqual(list2, [-80, -32, 1, 2, 23, 31, 41, 76])
        list3=[10,23,4,5,631,23]
        mo3_quickSort(list3)
        self.assertEqual(list3, [4, 5, 10, 23, 23, 631])
        list4=[19,23,45,67,89,1,2,5,32,51,22,46]
        mo3_quickSort(list4)
        self.assertEqual(list4, [1, 2, 5, 19, 22, 23, 32, 45, 46, 51, 67, 89])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



