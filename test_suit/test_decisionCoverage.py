import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):

    def test_invalid_triangle(self):
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 1, 1), Triangle.Type.INVALID)

    def test_scalene_triangle(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(1, 1, 3), Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)

    def test_isosceles_triangle(self):
        self.assertEqual(Triangle.classify(3, 3, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 3, 3), Triangle.Type.ISOSCELES)

if __name__ == '__main__':
    unittest.main()
