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
        self.assertEqual(1, len(list(f(1))))
        self.assertEqual(10, len(list(f(10))))
        self.assertEqual(25, len(list(f(25))))
        
        self.assertEqual([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], list(f(10)))
        
if __name__ == '__main__':
    unittest.main()