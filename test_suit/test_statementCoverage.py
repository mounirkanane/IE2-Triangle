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
    def testIsosceles2(self):
        actual = Triangle.classify(3, 3, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def testScalene2(self):
        actual = Triangle.classify(3, 2, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def testInvalid2(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def testIsoceles(self):
        actual = Triangle.classify(4, 4, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def testIsoceles3(self):
        actual = Triangle.classify(5, 8, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def testIsoceles4(self):
        actual = Triangle.classify(4, 7, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
