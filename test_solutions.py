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
        num_digits = 2
        answer = 9009
        
        self.assertEqual(answer, f(num_digits))
    
    def test_prob5(self):
        f = solutions.prob5
        maxnum = 10
        answer = 2520
        
        self.assertEqual(answer, f(maxnum))
        
    
    def test_prob6(self):
        f = solutions.prob6
        number= 10
        answer = 2640
        
        self.assertEqual(answer, f(number))
    
    def test_prob7(self):
        f = solutions.prob7
        nth_prime = 10
        answer = 29

        self.assertEqual(answer, f(nth_prime))
    
    def test_prob8(self):
        f = solutions.prob8
        num_as_string = '11234545'
        answer = 3 * 4 * 5 * 4 * 5
        
        self.assertEqual(answer, f(num_as_string))
        
    def test_prob9(self):
        f = solutions.prob9
        number = 3 + 4 + 5
        answer = 3 * 4 * 5
        
        self.assertEqual(answer, f(number))
    
    def test_prob10(self):
        f = solutions.prob10
        n = 10
        answer = 17
        
        self.assertEqual(answer, f(n))
    
    def test_prob12(self):
        f = solutions.prob12
        num_divisors = 5
        answer = 28
        
        self.assertEqual(answer, f(num_divisors))
    
    def test_prob14(self):
        f = solutions.prob14
        maxnum = 13
        answer = 9
        
        self.assertEqual(answer, f(maxnum))
            
    def test_prob15(self):
        f = solutions.prob15
        rows = 2
        columns = 2
        answer = 6
        
        self.assertEqual(answer, f(rows, columns))
    
    def test_prob16(self):
        f = solutions.prob16
        base = 2
        exponent = 10
        answer = 7
        
        self.assertEqual(answer, f(base, exponent))
    
    def test_prob17(self):
        f = solutions.prob17
        min = 1
        max = 5
        answer = 19
        
        self.assertEqual(answer, f(min, max))
    
    def test_prob18(self):
        f = solutions.prob18
    
        answer = ''
        return
        self.assertEqual(answer, f())
    
    def test_prob19(self):
        f = solutions.prob19
    
        answer = ''
        return
        self.assertEqual(answer, f())
    
    def test_prob20(self):
        f = solutions.prob20
    
        answer = ''
        return
        self.assertEqual(answer, f())
        

if __name__ == '__main__':
    unittest.main()
        