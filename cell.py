from graphics import Point, Line
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self.__draw_wall("left", "black")
        else:
            self.__draw_wall("left", "white")

        if self.has_right_wall:
            self.__draw_wall("right", "black")
        else:
            self.__draw_wall("right", "white")
        if self.has_top_wall:
            self.__draw_wall("top", "black")
        else:
            self.__draw_wall("top", "white")
        if self.has_bottom_wall:
            self.__draw_wall("bottom", "black")
        else:
            self.__draw_wall("bottom", "white")
    def __draw_wall(self, wall, color):
        match wall:
            case "left":
                wall = Line(
                    Point(self._x1, self._y1),
                    Point(self._x1, self._y2),
                )
            case "right":
                wall = Line(
                    Point(self._x2, self._y1),
                    Point(self._x2, self._y2),
                )
            case "top":
                wall = Line(
                    Point(self._x1, self._y1),
                    Point(self._x2, self._y1),
                )
            case "bottom":
                wall = Line(
                    Point(self._x1, self._y2),
                    Point(self._x2, self._y2),
                )
            case _:
                raise ValueError("no matching wall")

        self._win.draw_line(wall, color)

    def draw_move(self, to_cell, undo=False):
        line = Line(
            self.get_mid_point(),
            to_cell.get_mid_point()
        )
        fill_color = "red"
        if undo:
           fill_color = "gray"
        self._win.draw_line(line, fill_color)

    def get_mid_point(self):
        x = (self._x1 + self._x2) // 2
        y = (self._y1 + self._y2) // 2
        return Point(x, y)
