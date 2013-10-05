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
        number_pyramid = '''
                3    
               7 4  
              2 4 6 
             8 5 9 3
        '''
        
        answer = 23
        self.assertEqual(answer, f(number_pyramid))
    
    def test_prob20(self):
        f = solutions.prob20
        number = 5
        answer = 3
        
        self.assertEqual(answer, f(number))
        
    def test_prob21(self):
        #TODO: add test for problem 21 (it's not modular right now)
        f = solutions.prob21
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob22(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob23(self):
        #TODO: After prob23 is rewritten, write this test
        f = solutions.prob23
        maxnum = 16
        answer = 16
        return
    
        self.assertEqual(answer, f(maxnum))
        
    def test_prob24(self):
        f = solutions.prob24
        string = '1234'
        answer = '1243'
        nth_permutation = 2
        
        self.assertEqual(answer, f(string, nth_permutation))
        
    def test_prob25(self):
        f = solutions.prob25
        num_digits = 3
        answer = 12
        
        self.assertEqual(answer, f(num_digits))
        
    def test_prob26(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob27(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob28(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob29(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob30(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob31(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob32(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob33(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob34(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob35(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob36(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob37(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob38(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob39(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob40(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob41(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob42(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob43(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob44(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob45(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob46(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob47(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob48(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob49(self):
        f = solutions.prob20
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    def test_prob50(self):
        f = solutions.prob50
        number = 5
        answer = 3
        return
        
        self.assertEqual(answer, f(number))
        
    
if __name__ == '__main__':
    unittest.main()
        