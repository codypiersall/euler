import unittest

import solutions
from scipy.constants.codata import unit

class TestSolutions(unittest.TestCase):
    
    def test_prob1(self):
        f = solutions.prob1
        maxnum = 10
        numbers = [2,5]
        
        answer = 23
        self.assertEqual(answer, f(maxnum, numbers))
        
    
    def test_prob2(self):
        f = solutions.prob2
        maxnum = 100
        answer = 2 + 8 + 34
        self.assertEqual(answer, f(maxnum))
    
    def test_prob3(self):
        f = solutions.prob3
        number = 13195
        answer = 29
        
        self.assertEqual(answer, f(number))
        
    def test_prob4(self):
        f = solutions.prob4
        
    
    def test_prob5(self):
        f = solutions.prob5
    
    
    def test_prob6(self):
        f = solutions.prob6
    
    
    def test_prob7(self):
        f = solutions.prob7
    
    
    def test_prob8(self):
        f = solutions.prob8
    
    
    def test_prob9(self):
        f = solutions.prob9

if __name__ == '__main__':
    unittest.main()
        