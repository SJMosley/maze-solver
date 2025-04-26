from graphics import Point
from cell import Cell
import random

def draw_test_cells(win):
    #cell testing
    points = [
        Point(100,100),
        Point(200,100),
        Point(300,100),
        Point(400,100),
        Point(500,100),
        Point(600,100),
        Point(100,200),
        Point(200,200),
        Point(300,200),
        Point(400,200),
        Point(500,200),
        Point(600,200),
        Point(100,300),
        Point(200,300),
        Point(300,300),
        Point(400,300),
        Point(500,300),
        Point(600,300),
        Point(100,400),
        Point(200,400),
        Point(300,400),
        Point(400,400),
        Point(500,400),
        Point(600,400),
    ]
    cell_size = 50
    walls = []
    cells = []
    for point in points:
        match point.x:
            case 100:
               walls = [True, True, True, True]
            case 200:
               walls = [False, True, True, True]
            case 300:
               walls = [True, False, True, False]
            case 400:
               walls = [False, True, False, True]
            case 500:
               walls = [True, True, True, False]
            case 600:
               walls = [False, False, False, False]
        cell = Cell(win)
        cell.draw()
        cells.append(cell)

    for cell in cells:
        index = random.randint(0, len(cells)-1)
        cell.draw_move(cells[index])
