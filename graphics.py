from tkinter import Tk, BOTH, Canvas

# x=0 is left of screen
# y=0 is top of screen
# 0,0 is top left of screen
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("maze-solver")
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def get_mid_point(self):

        mid_point = Point(
            self.__canvas.winfo_reqwidth()/2,
            self.__canvas.winfo_reqheight()/2
        )
        return mid_point
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x:{self.x}, y:{self.y})"

class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__start.x, self.__start.y,
            self.__end.x, self.__end.y,
            fill = fill_color,
            width = 2
        )
