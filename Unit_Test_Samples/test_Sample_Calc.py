import unittest
import Sample_Calc


class test_Sample_Calc(unittest.TestCase):

    def test_Add_num(self):
        self.assertEqual(Sample_Calc.Add_num(10, 5), 15)
        self.assertEqual(Sample_Calc.Add_num(-10, 5), -5)
        self.assertEqual(Sample_Calc.Add_num(-10, -5), -15)

    def test_Subtract_num(self):
        self.assertEqual(Sample_Calc.Subtract_num(10, 5), 5)
        self.assertEqual(Sample_Calc.Subtract_num(-10, 5), -15)
        self.assertEqual(Sample_Calc.Subtract_num(-10, -5), -5)

    def test_Multiply_num(self):
        self.assertEqual(Sample_Calc.Multiply_num(10, 5), 50)
        self.assertEqual(Sample_Calc.Multiply_num(-10, 5), -50)
        self.assertEqual(Sample_Calc.Multiply_num(-10, -5), 50)

    def test_Devide_num(self):
        self.assertEqual(Sample_Calc.Devide_num(10, 5), 2)
        self.assertEqual(Sample_Calc.Devide_num(-10, 5), -2)
        self.assertEqual(Sample_Calc.Devide_num(-10, -5), 2)
        self.assertEqual(Sample_Calc.Devide_num(9, 5), 1.8)



if __name__ == '__main__':
	unittest.main()