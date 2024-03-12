import unittest
from Lab1 import intersection_point

class TestIntersectionPoint(unittest.TestCase):

    def test_intersection_point(self):
        # Точки для первой прямой:
        # Точки для второй прямой: 
        x1, y1 = 1, 1
        x2, y2 = 2, 2
        x3, y3 = 1, 2
        x4, y4 = 2, 1
        expected_point = (1.5, 1.5)
        intersection = intersection_point(x1, y1, x2, y2, x3, y3, x4, y4)
        self.assertEqual(intersection, expected_point)

    def test_parallel_lines(self):
        # Параллельные прямые: 
        x1, y1 = 1, 1
        x2, y2 = 2, 2
        x3, y3 = 1, 2
        x4, y4 = 2, 3
        intersection = intersection_point(x1, y1, x2, y2, x3, y3, x4, y4)
        self.assertIsNone(intersection)

    def test_coincident_lines(self):
        # Совпадающие прямые: 
        x1, y1 = 1, 1
        x2, y2 = 2, 2
        intersection = intersection_point(x1, y1, x2, y2, x1, y1, x2, y2)
        self.assertIsNone(intersection)

if __name__ == '__main__':
    unittest.main()