from graphics import Window #, Point, Line
from unit_circle import draw_unit_circle_lines

def main():
    win = Window(800,600) #width, height
    draw_unit_circle_lines(win)

    win.wait_for_close()



main()
