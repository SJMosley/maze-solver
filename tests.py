import unittest
import random
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    def test_maze_create_cells_large(self):
            num_cols = 16
            num_rows = 12
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )
    def test_maze_create_cells_neg(self):
        num_cols = -2
        num_rows = 10
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, num_rows, num_cols, 2, 20)
    def test_entrance_and_exit(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_right_wall,
            False
        )
    # def test_break_walls(self):
    def test_reset_visited(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        i = random.randint(0, num_cols - 1)
        j = random.randint(0, num_rows - 1)
        m1._cells[i][j].visited = 1
        m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[i][j].visited,
            False
        )

if __name__ == "__main__":
     unittest.main()
