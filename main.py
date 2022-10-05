import shutil
import os

from figures import *
from texttable import Texttable

def print_header(text):
    os.system('cls')
    width = shutil.get_terminal_size().columns
    print(text.upper().center(width) + '\n')

def print_table(figures):
    table = Texttable()
    table.add_row(['№', 'Название', 'Периметр', 'Площадь'])
    for i in range(len(figures)):
        table.add_row([str(i + 1), figures[i], round(figures[i].get_perimeter(), 3), round(figures[i].get_area(), 3)])
    
    print_header('таблица фигур отсортированных по площади')
    print(table.draw())
    print('\n')

def get_int(msg):
    while True:
        try:
            num = int(input(msg + ": "))
        except:
            print("\033[31m{}\033[0m".format("ERROR: Invalid value! Try again..."))
            continue
        return num

def get_count_figs():
    print_header('программа для работы с фигурами')
    return get_int('Введите количество требуемых фигур')

def get_num_figure():
    print_header('выбор фигуры')
    return get_int('1 — Треугольник\n' +
                    '2 — Круг\n' +
                    '3 — Четырехугольник (прямоугольный)\n\n' +
                    'Выберите фигуру из доступных')
    
def get_filled_figure(num_figure):
    def pattern(coordinate, point):
        return f'Введите {coordinate} для точки {point}'

    match num_figure:
        case 1:
            print_header('заполнение треугольника')
            A = Point(get_int(pattern('x', 'A')), get_int(pattern('y', 'A')))
            B = Point(get_int(pattern('x', 'B')), get_int(pattern('y', 'B')))
            C = Point(get_int(pattern('x', 'C')), get_int(pattern('y', 'C')))
            return Triangle(A, B, C)
        case 2:
            print_header('заполнение круга')
            A = Point(get_int(pattern('x', 'A')), get_int(pattern('y', 'A')))
            B = Point(get_int(pattern('x', 'B')), get_int(pattern('y', 'B')))
            return Circle(A, B)
        case 3:
            print_header('заполнение четырехугольника')
            A = Point(get_int(pattern('x', 'A')), get_int(pattern('y', 'A')))
            B = Point(get_int(pattern('x', 'B')), get_int(pattern('y', 'B')))
            C = Point(get_int(pattern('x', 'C')), get_int(pattern('y', 'C')))
            D = Point(get_int(pattern('x', 'D')), get_int(pattern('y', 'D')))
            return Quadrilateral(A, B, C, D)
        case _:
            return -1

if __name__ == "__main__":
    # Берем количество фигур
    count = get_count_figs()

    # Заполняем все
    figures = []
    for i in range(count):
        num_figure = get_num_figure()
        figure = get_filled_figure(num_figure)
        figures.append(figure)

    # Сортируем
    figures.sort(key=lambda fig: fig.get_area())

    # Выводим
    print_table(figures)

