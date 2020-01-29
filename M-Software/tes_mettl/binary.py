import unittest
import random
import re

def solution(N):
   
    if N < 0:
        return 0  

    binNum = "{0:b}".format(N) #100100010

    
    strBinNum = str(binNum) #"100100010"

    largest = 0
    total = 0
    idx = 0
    
    binList = {}

    for match in re.finditer('1', strBinNum):
        binList[idx] = match.start()
        binList[idx + 1] = match.end()

        if(idx > 0):
            total = binList[idx] - binList[idx - 1]
            total = total - 1

        if total >= largest: 
            largest = total

        idx += 1

    return largest

class TestSkeleton(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(solution(-1), 0)

    def test_extreme_small(self):
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(5), 1)  

        
    def test_longest_binary_gap(self):
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution(42),1)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(19), 2)
                                             
    def test_no_binary_gap(self):
        self.assertEqual(solution(32), 0)
                  
    def test_extreme_large_binary_gap(self):
        self.assertEqual(solution(2147483647), 0)
        self.assertEqual(solution(3908253), 3)

if __name__ == '__main__':
    unittest.main()