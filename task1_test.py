import unittest
from typing import List, Tuple
from Lab1 import point_between

def read_points_from_file(filename: str) -> List[Tuple[float, float]]:
    points = []
    with open(filename, 'r') as file:
        for line in file:
            coords = tuple(map(float, line.strip().split()))
            points.append(coords)
    return points



class TestPointBetween(unittest.TestCase):

    def test_point_between_1(self):
        A = (0, 0)
        B = (1, 1)
        C = (2, 2)
        self.assertEqual(point_between(A, B, C), B)

    def test_point_between_2(self):
        A = (0.5, 0.5)
        B = (1, 1)
        C = (-1, -1)
        self.assertEqual(point_between(A, B, C), A)

    def test_point_between_3(self):
        A = (0, 0)
        B = (-2, -2)
        C = (-1, -1)
        self.assertEqual(point_between(A, B, C), C)
        
    def test_vertical_line(self):
        # Вертикальная линия
        A = (0, 0)
        B = (0, 1)
        C = (0, 2)
        self.assertEqual(point_between(A, B, C), B)

    def test_horizontal_line(self):
        # Горизонтальная линия
        A = (0, 0)
        B = (1, 0)
        C = (2, 0)
        self.assertEqual(point_between(A, B, C), B)

    def test_collinear_points(self):
        # Точки лежат на одной прямой
        A = (0, 0)
        B = (1, 1)
        C = (2, 2)
        self.assertEqual(point_between(A, B, C), B)

    def test_all_points_same(self):
        # Все точки совпадают
        A = (0, 0)
        B = (0, 0)
        C = (0, 0)
        self.assertEqual(point_between(A, B, C), B)

if __name__ == '__main__':
    unittest.main()