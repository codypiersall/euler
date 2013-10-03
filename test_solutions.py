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
        

if __name__ == '__main__':
    unittest.main()
        