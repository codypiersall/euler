import euler
import unittest

class TestEuler(unittest.TestCase):
    
    def test_pandigital(self):
        """Test that pandigital function generator works."""
        f1 = euler.is_pandigital_generator(1, 9)
        self.assertTrue(f1([123, 456, 789]))
        self.assertFalse(f1([123, 456, 7891]))
        self.assertFalse(f1([112, 345, 678]))
        self.assertTrue(f1([987654321]))
        
    def test_num_digits(self):
        self.assertEqual(euler.get_num_digits(100), 3)
        self.assertEqual(euler.get_num_digits(999), 3)
        self.assertEqual(euler.get_num_digits(1), 1)
        
    def test_right_triangle_combinations(self):
        correct_answer = [(20, 48, 52), (24,45,51), (30,40,50)]
        my_answer = list(euler.right_triangle_combinations(120))
        self.assertEqual(correct_answer, my_answer)
        
    def test_is_prime(self):
        p = euler.is_prime
        self.assertTrue(p(2))
        self.assertTrue(p(3))
        self.assertTrue(p(5))
        self.assertTrue(p(7919))
        
        self.assertFalse(p(4))
        self.assertFalse(p(10))
        self.assertFalse(p(10000))
        
    def test_get_digit(self):
        f = euler.get_digit
        self.assertEqual(2, f(34352, 0))
        self.assertEqual(5, f(34352, 1))
        self.assertEqual(3, f(34352, 2))
        self.assertEqual(4, f(34352, 3))
        self.assertEqual(3, f(34352, 4))
        
    def test_generate_triangular_numbers(self):
        f = euler.generate_triangular_numbers
        
        # make sure it returns the right numbers
        self.assertEqual(1, len(list(f(1, 1))))
        self.assertEqual(10, len(list(f(1, 10))))
        self.assertEqual(25, len(list(f(1, 25))))
        
        self.assertEqual([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], list(f(1, 10)))
    
    def test_generate_pentagonal_numbers(self):
        f = euler.generate_pentagonal_numbers
        
        # make sure it returns the right numbers
        self.assertEqual(1, len(list(f(1, 1))))
        self.assertEqual(10, len(list(f(1, 10))))
        self.assertEqual(25, len(list(f(1, 25))))
        
        self.assertEqual([1, 5, 12, 22, 35, 51, 70, 92, 117, 145], list(f(1, 10)))
        
    def test_generate_hexagonal_numbers(self):
        f = euler.generate_hexagonal_numbers
        
        # make sure it returns the right numbers
        self.assertEqual(1, len(list(f(1,1))))
        self.assertEqual(10, len(list(f(1,10))))
        self.assertEqual(25, len(list(f(1,25))))
        
        self.assertEqual([1, 6, 15, 28, 45], list(f(1,5)))
        
    def test_primesfrom2to(self):
        f = euler.primesfrom2to
        primes = [2,3,5,7,11,13,17,19]
        self.assertEqual(primes, list(f(20)))
        
    def test_get_prime_factors3(self):
        f = euler.get_prime_factors3
        primes = euler.primesfrom2to(1000)
        
        n1 = 21
        factors1 = [3,7]
        self.assertEqual(factors1, f(n1, primes))
        
        n2 = 300
        factors2 = [2,2,3,5,5]
        self.assertEqual(factors2, f(n2, primes))
        
        n3 = 999
        factors3 = [3, 3, 3, 37]
        self.assertEqual(factors3, f(n3, primes))
        
    def test_numbers_are_permutations(self):
        f = euler.numbers_are_permutations
        l1 = [1234, 2341, 4321]
        l2 = [1234, 2341, 12345]
        l3 = [1111, 1111, 1111]
        
        self.assertTrue(f(l1))
        self.assertFalse(f(l2))
        self.assertTrue(f(l3))
        self.assertTrue(f([1230, 1023, 2130]))
        
if __name__ == '__main__':
    unittest.main()