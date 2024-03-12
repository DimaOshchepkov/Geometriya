import unittest

import Lab1
from Lab1 import intersect, Point, is_convex_quad

class TestCollinearity(unittest.TestCase):

    def test_collinear_points(self):
        A = (1, 1)
        B = (2, 2)
        C = (3, 3)
        self.assertTrue(Lab1.are_points_collinear(A, B, C))

    def test_non_collinear_points(self):
        A = (1, 1)
        B = (2, 2)
        C = (4, 3)
        self.assertFalse(Lab1.are_points_collinear(A, B, C))

    def test_horizontal_collinear_points(self):
        A = (1, 1)
        B = (2, 1)
        C = (3, 1)
        self.assertTrue(Lab1.are_points_collinear(A, B, C))

    def test_vertical_collinear_points(self):
        A = (1, 1)
        B = (1, 2)
        C = (1, 3)
        self.assertTrue(Lab1.are_points_collinear(A, B, C))

    def test_same_point(self):
        A = (1, 1)
        self.assertTrue(Lab1.are_points_collinear(A, A, A))

    def test_common_collinear_points(self):
        A = (1, 5)
        B = (-1, 3)
        C = (2, 6)
        self.assertTrue(Lab1.are_points_collinear(A, B, C))
        
        
class TestOrientation(unittest.TestCase):

    def test_counterclockwise_orientation(self):
        A = (1, 1)
        B = (2, 2)
        C = (2, 3)
        self.assertEqual(Lab1.orientation(A, B, C), -1)

    def test_clockwise_orientation(self):
        A = (1, 1)
        B = (3, 4)
        C = (2, 2)
        self.assertEqual(Lab1.orientation(A, B, C), 1)

    def test_collinear_points(self):
        A = (1, 1)
        B = (2, 2)
        C = (4, 4)
        self.assertEqual(Lab1.orientation(A, B, C), 0)
        
        
    def test_negativenum_points(self):
        A = (-1, 5)
        B = (2, 2)
        C = (3, 4)
        self.assertEqual(Lab1.orientation(A, B, C), -1)
        

class TestSegmentIntersection(unittest.TestCase):

    def test_segments_intersect(self):
        # Тест, когда отрезки пересекаются
        self.assertTrue(intersect(Point(1, 1), Point(4, 4), Point(1, 4), Point(4, 1)))

    def test_segments_no_intersect(self):
        # Тест, когда отрезки пересекаются
        self.assertFalse(intersect(Point(1, 1), Point(1, 4), Point(4, 4), Point(4, 1)))
        
    def test_segments_coincide(self):
        # Тест, когда отрезки совпадают
        self.assertTrue(intersect(Point(0, 0), Point(2, 2), Point(0, 0), Point(2, 2)))

    def test_both_points(self):
        # Тест, когда оба отрезка являются точками
        self.assertTrue(intersect(Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)))

    def test_intersection_at_endpoints(self):
        # Тест, когда отрезки пересекаются только на концах
        self.assertTrue(intersect(Point(0, 0), Point(2, 2), Point(1, 1), Point(3, 3)))

    def test_parallel_segments(self):
        # Тест, когда отрезки параллельны, но не пересекаются
        self.assertFalse(intersect(Point(0, 0), Point(2, 0), Point(0, 1), Point(2, 1)))
        
class TestConvexQuad(unittest.TestCase):

    def test_convex_quad(self):
        # Тест на выпуклый четырехугольник
        self.assertTrue(is_convex_quad(Point(0, 0), Point(2, 0), Point(2, 1), Point(1, 2)))

    def test_non_convex_quad(self):
        # Тест на невыпуклый четырехугольник
        self.assertFalse(is_convex_quad(Point(0, 0), Point(2, 0), Point(1, 1), Point(1, -1)))

    def test_parallel_sides(self):
        # Тест на параллельные стороны
        self.assertTrue(is_convex_quad(Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)))

    def test_points_collinear(self):
        # Тест на лежащие на одной прямой точки
        self.assertFalse(is_convex_quad(Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)))
        
if __name__ == '__main__':
    unittest.main()