import unittest
import mean_var_std


class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2,6,2,8,4,7,1,9,2])
        expected = {
            'mean': [[4.0, 6.333333333333333, 3.3333333333333335], [4.666666666666667, 4.333333333333333, 5.0], 4.444444444444445],
            'variance': [[5.5555555555555545, 0.2222222222222221, 8.222222222222221], [9.555555555555555, 11.555555555555557, 4.0], 6.91358024691358],
            'standard deviation': [[2.3570226039551585, 0.4714045207910317, 2.8674417556808756], [3.0912061651652345, 3.39934634239519, 2.0], 2.629314528472004],
            'max': [[8, 9, 7], [6, 8, 9], 9],
            'min': [[1, 4, 2], [2, 4, 1], 1],
            'sum': [[12, 19, 11], [14, 13, 18], 42]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=2)
        self.assertAlmostEqual(actual['mean'][0][1], expected['mean'][0][1], places=2)
        self.assertAlmostEqual(actual['mean'][0][2], expected['mean'][0][2], places=2)
        self.assertAlmostEqual(actual['mean'][1][0], expected['mean'][1][0], places=2)
        self.assertAlmostEqual(actual['mean'][1][1], expected['mean'][1][1], places=2)
        self.assertAlmostEqual(actual['mean'][1][2], expected['mean'][1][2], places=2)
        self.assertAlmostEqual(actual['mean'][2], expected['mean'][2], places=2)
        
    def test_calculate2(self):
        actual = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])
        expected = {
            'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889],
            'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875],
            'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137],
            'max': [[9, 9, 5], [9, 3, 9], 9],
            'min': [[2, 1, 0], [1, 3, 0], 0],
            'sum': [[14, 13, 8], [15, 9, 11], 35]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=2)
        self.assertAlmostEqual(actual['mean'][0][1], expected['mean'][0][1], places=2)
        self.assertAlmostEqual(actual['mean'][0][2], expected['mean'][0][2], places=2)
        self.assertAlmostEqual(actual['mean'][1][0], expected['mean'][1][0], places=2)
        self.assertAlmostEqual(actual['mean'][1][1], expected['mean'][1][1], places=2)
        self.assertAlmostEqual(actual['mean'][1][2], expected['mean'][1][2], places=2)
        self.assertAlmostEqual(actual['mean'][2], expected['mean'][2], places=2)
        
    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", mean_var_std.calculate, [2,6,2,8,4,7,1,9])
