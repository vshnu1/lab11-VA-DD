#https://github.com/vshnu1/lab11-VA-DD.git
# Partner 1: Vishnu Araveeti
# Partner 2: Damien Decker
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(4, 0),4)
        self.assertEqual(add(-5, -7), -12)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract(8, 0), 8)
        self.assertEqual(subtract(-8, -9), 1)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
            self.assertEqual(mul(1,2),2)
            self.assertEqual(mul(0,1),0)
            self.assertEqual(mul(100,1),100)

    def test_divide(self): # 3 assertions
            self.assertEqual(div(2,100),50)
            self.assertEqual(div(1,0),0)
            self.assertEqual(div(3,6),2)

        ##########################
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3,27),3)
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(3,1),0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5,0)
        
        
        ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
            with self.assertRaises(ValueError):
                logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
            self.assertEqual(hypotenuse(5,12),13)
            self.assertEqual(hypotenuse(3,4),5)
            self.assertEqual(hypotenuse(6,8),10)

    def test_sqrt(self): # 3 assertions
            with self.assertRaises(ValueError):
                square_root(-1)
            self.assertEqual(square_root(9),3)
            self.assertEqual(square_root(0),0)
        #########################

    # # Do not touch this
if __name__ == "__main__":
    unittest.main()