from typing import NamedTuple, Optional, Tuple

def are_points_collinear(A: Tuple[float, float], B: Tuple[float, float], C: Tuple[float, float]) -> bool:
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    
    area = 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return area == 0

def orientation(A: Tuple[float, float], B: Tuple[float, float], C: Tuple[float, float]) -> int:
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    
    vector_BA = (x1 - x2, y1 - y2)
    vector_BC = (x3 - x2, y3 - y2)
    
    # Вычисляем косое произведение векторов BA и BC
    cross_product = vector_BA[0] * vector_BC[1] - vector_BA[1] * vector_BC[0]
    
    if cross_product > 0:
        return 1  # Обход по часовой стрелке
    elif cross_product < 0:
        return -1  # Обход против часовой стрелке
    else:
        return 0  # Точки лежат на одной прямой
    

# http://e-maxx.ru/algo/segments_intersection_checking
class Point(NamedTuple):
    x: int
    y: int

def area(a: Point, b: Point, c: Point) -> int:
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def intersect_1(a: int, b: int, c: int, d: int) -> bool:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    return max(a, c) <= min(b, d)

def intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    return (intersect_1(a.x, b.x, c.x, d.x)
            and intersect_1(a.y, b.y, c.y, d.y)
            and area(a, b, c) * area(a, b, d) <= 0
            and area(c, d, a) * area(c, d, b) <= 0)
    
    
def cross_product(v1: Tuple[float, float], v2: Tuple[float, float]) -> float:
    return v1[0] * v2[1] - v1[1] * v2[0]

def is_convex_quad(A: Tuple[float, float], B: Tuple[float, float], C: Tuple[float, float], D: Tuple[float, float]) -> bool:
    AB = (B.x - A.x, B.y - A.y)
    BC = (C.x - B.x, C.y - B.y)
    CD = (D.x - C.x, D.y - C.y)
    DA = (A.x - D.x, A.y - D.y)

    cross_products = [
        cross_product(AB, BC),
        cross_product(BC, CD),
        cross_product(CD, DA),
        cross_product(DA, AB)
    ]

    # Проверяем, все ли векторные произведения имеют одинаковое направление
    if all(cp > 0 for cp in cross_products) or all(cp < 0 for cp in cross_products):
        return True
    return False

def point_between(A: Tuple[float, float], B: Tuple[float, float], C: Tuple[float, float]) -> Tuple[float, float]:
    if A[0] <= B[0] <= C[0] or C[0] <= B[0] <= A[0]:
        return B
    elif B[0] <= A[0] <= C[0] or C[0] <= A[0] <= B[0]:
        return A
    else:
        return C
    
# https://mathter.pro/angem/2_2_4_kak_sostavit_uravnenie_pryamoy_po_dvum_tochkam.html
def intersection_point(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> Optional[Tuple[float, float]]:
    # Проверяем параллельность прямых
    det = (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1)
    if det == 0:
        return None  # Прямые параллельны, нет точки пересечения
    else:
        # Находим координаты точки пересечения
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
        return x, y
