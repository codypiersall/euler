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
if __name__ == '__main__':
    unittest.main()