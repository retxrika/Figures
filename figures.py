import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    def __init__(self):
        self.name = ''

    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0

    def __str__(self):
        return self.name.capitalize()

    def calc_len(pointA, pointB):
        return math.sqrt(math.pow(pointB.x - pointA.x, 2) + math.pow(pointB.y - pointA.y, 2))

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.len_a_b = Figure.calc_len(a, b)
        self.len_b_c = Figure.calc_len(b, c)
        self.len_c_a = Figure.calc_len(c, a)
        self.name = 'треугольник'

    def get_perimeter(self):
        return self.len_a_b + self.len_b_c + self.len_c_a

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.len_a_b) 
                                        * (semi_perimeter - self.len_b_c)
                                        * (semi_perimeter - self.len_c_a))

class Circle(Figure):
    def __init__(self, a, b):
        self.len_a_b = Figure.calc_len(a, b)
        self.name = 'круг'

    def get_perimeter(self):
        return 2 * math.pi * self.len_a_b

    def get_area(self):
        return math.pi * math.pow(self.len_a_b, 2)

class Quadrilateral(Figure):
    def __init__(self, a, b, c, d):
        self.len_a_b = Figure.calc_len(a, b)
        self.len_b_c = Figure.calc_len(b, c)
        self.len_c_d = Figure.calc_len(c, d)
        self.len_d_a = Figure.calc_len(d, a)
        self.name = 'четырехугольник'

    def get_perimeter(self):
        return self.len_a_b + self.len_b_c + self.len_c_d + self.len_d_a

    def get_area(self):
        return self.len_a_b * self.len_b_c
