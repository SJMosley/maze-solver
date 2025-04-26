import time
import random
from graphics import Point, Line
from cell import Cell
from test_drawing.unit_circle import draw_unit_circle_lines
CELLS_EXITED = 0
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if num_rows <=0 or num_cols <=0:
            raise ValueError("maze must have at least 1 cell")
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win
        self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        global CELLS_EXITED
        CELLS_EXITED = 0
        self._reset_cells_visited()
    def _create_cells(self):
        #Generate Cells
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        #Draw Cells
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            return
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = self._cells_to_visit(i, j)

            # print(f"to visit {to_visit}")
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                # sell._test_cell_visited()
                return
            else:
                direction = random.randint(0, len(to_visit) - 1)
                next_cell = to_visit[direction]

                self._break_adjacent_walls(i, j, next_cell[0], next_cell[1])

                # print(f"calling next cell {next_cell[0]}, {next_cell[1]}")
                self._break_walls_r(next_cell[0], next_cell[1])
    def _test_cell_visited(self):
        global CELLS_EXITED
        CELLS_EXITED += 1
        total_cells = self.num_cols * self.num_rows
        print(f"{CELLS_EXITED/total_cells * 100}% of Cells visited")
        print(f"{CELLS_EXITED} of {total_cells} Cells visited")
    def _cells_to_visit(self, i, j):
        to_visit = []
        if i > 0: #left
            if not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
        if i < self.num_cols - 1: #right
            if not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
        if j > 0: #top
            if not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
        if j < self.num_rows - 1: #bottom
            if not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
        return to_visit

    def _break_adjacent_walls(self, curr_x, curr_y, next_x, next_y):
        if curr_x == next_x and next_y < curr_y: #up
            self._cells[curr_x][curr_y].has_top_wall = False
            self._cells[next_x][next_y].has_bottom_wall = False
        if curr_x == next_x and curr_y < next_y: #down
            self._cells[curr_x][curr_y].has_bottom_wall = False
            self._cells[next_x][next_y].has_top_wall = False
        if curr_y == next_y and next_x < curr_x: #left
            self._cells[curr_x][curr_y].has_left_wall = False
            self._cells[next_x][next_y].has_right_wall = False
        if curr_y == next_y and curr_x < next_x: #right
            self._cells[curr_x][curr_y].has_right_wall = False
            self._cells[next_x][next_y].has_left_wall = False
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            # YOU WIN
            draw_unit_circle_lines(self.win)
            return True
        solved = False
        # If there is a cell in that direction, there is no wall blocking you, and that cell hasn't been visited:
        #move left?
        if i > 0 and not self._cells[i][j].has_left_wall:
            if not self._cells[i - 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                solved = self._solve_r(i - 1, j)
                if solved:
                    return solved
                self._cells[i - 1][j].draw_move(self._cells[i][j], undo=True)
        #move top?
        if j > 0 and not self._cells[i][j].has_top_wall:
            if not self._cells[i][j - 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                solved = self._solve_r(i, j - 1)
                if solved:
                    return solved
                self._cells[i][j - 1].draw_move(self._cells[i][j], undo=True)
        #move right?
        if i < self.num_cols - 1 and not self._cells[i][j].has_right_wall:
            if not self._cells[i + 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                solved = self._solve_r(i + 1, j)
                if solved:
                    return solved
                self._cells[i + 1][j].draw_move(self._cells[i][j], undo=True)
        #move down?
        if j < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall:
            if not self._cells[i][j + 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                solved = self._solve_r(i , j + 1)
                if solved:
                    return solved
                self._cells[i][j + 1].draw_move(self._cells[i][j], undo=True)

        return solved
    def solve(self):
        if self.win is None:
            return

        mid = self._cells[0][0].get_mid_point()
        into_maze = Line(Point(mid.x - self._cell_size_x, mid.y), mid)
        self.win.draw_line(into_maze, "red")
        solved = self._solve_r(0,0)
        if solved:
            end_mid = self._cells[self.num_cols - 1][self.num_rows-1].get_mid_point()
            out_of_maze = Line(end_mid, Point(end_mid.x + self._cell_size_x, end_mid.y))
            self.win.draw_line(out_of_maze, "red")
