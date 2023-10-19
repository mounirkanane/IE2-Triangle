import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def testEquilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    def testScalene(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    def testIsoceles(self):
        actual = Triangle.classify(4, 4, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def invalid_side(self):
        actual = Triangle.classify(0, 4, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def invalid_inequality(self):
        actual = Triangle.classify(1, 1, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
