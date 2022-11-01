from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.u1 = [1, 2]
        self.u2 = [16, 27]
        self.u3 = [6, 19]
        self.u4 = [1 , 8]
        self.u5 = [9, 3]
        self.u6 = [-3, 7]
        self.u7 = [4, -5]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.u1, self.u2), [59, 54])
        self.assertEqual(add_frac(self.u3, self.u5), [63, 19])
        self.assertEqual(add_frac(self.u2, self.u4), [155, 216])
        self.assertEqual(add_frac(self.u4, self.u1), [5, 8])
        self.assertEqual(add_frac(self.u4, self.u5), [25, 8])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.u1, self.u2), [-5, 54])
        self.assertEqual(sub_frac(self.u3, self.u5), [-51, 19])
        self.assertEqual(sub_frac(self.u2, self.u4), [101, 216])
        self.assertEqual(sub_frac(self.u4, self.u1), [-3, 8])
        self.assertEqual(sub_frac(self.u4, self.u5), [-23, 8])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.u1, self.u2), [8, 27])
        self.assertEqual(mul_frac(self.u3, self.u5), [18, 19])
        self.assertEqual(mul_frac(self.u2, self.u4), [2, 27])
        self.assertEqual(mul_frac(self.u4, self.u1), [1, 16])
        self.assertEqual(mul_frac(self.u4, self.u5), [3, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.u1, self.u2), [27, 32])
        self.assertEqual(div_frac(self.u3, self.u5), [2, 19])
        self.assertEqual(div_frac(self.u2, self.u4), [128, 27])
        self.assertEqual(div_frac(self.u4, self.u1), [1, 4])
        self.assertEqual(div_frac(self.u4, self.u5), [1, 24])

    def test_is_positive(self):
        self.assertEqual(is_positive(self.u1), True)
        self.assertEqual(is_positive(self.u6), False)
        self.assertEqual(is_positive(self.u7), False)
        self.assertEqual(is_positive(self.u4), True)

    def test_is_zero(self):
        self.assertEqual(is_zero(self.u1), False)
        self.assertEqual(is_zero(self.zero), True)
        self.assertEqual(is_zero([5, 0]), -1)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.u1, self.u2), -1)
        self.assertEqual(cmp_frac(self.zero, self.u7), 1)
        self.assertEqual(cmp_frac([3, 5], [9, 15]), 0)
        self.assertEqual(cmp_frac([27, 46], [6, 11]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.u1), 0.5)
        self.assertEqual(frac2float(self.u7), -0.8)
        self.assertEqual(frac2float(self.u5), 3.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
