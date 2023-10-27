import unittest
from isTriangle import Triangle

class TestTriangle(unittest.TestCase):

    def test_negative_sides(self):
        # Testing for negative sides
        self.assertEqual(Triangle.classify(-1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, -1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 2, -1), Triangle.Type.INVALID)
        pass
        
    def test_zero_sides(self):
        # Testing for zero sides
        self.assertEqual(Triangle.classify(0, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 0, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 2, 0), Triangle.Type.INVALID)
        pass

    def test_equilateral(self):
        # Testing for equilateral triangle
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        pass

    def test_isosceles(self):
        # Testing for isosceles triangle
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)
        pass

    def test_scalene(self):
        # Testing for scalene triangle
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        pass

    def test_invalid_triangle(self):
        # Testing for invalid triangles due to side lengths
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 3, 1), Triangle.Type.INVALID)
        pass
    
    def test_invalid_combinations(self):
        # Test invalid combinations that previously might have been missed
        self.assertEqual(Triangle.classify(1, 1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 3, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 1, 1), Triangle.Type.INVALID)
        pass
        
    def test_large_values(self):
        # Test with large values to ensure the logic works for all ranges
        self.assertEqual(Triangle.classify(1000000, 1000000, 1000000), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(1000000, 999999, 999999), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(1000000, 999999, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1000000, 500000, 499999), Triangle.Type.INVALID)
        pass
        
    def test_boundary_values(self):
        # Test boundary values just around 0
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        pass
    
    
if __name__ == "__main__":
    unittest.main()
