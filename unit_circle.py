import math
from graphics import Window, Point, Line

def draw_unit_circle_lines(win):
    n1_2 = 1/2
    rt_2_2 = math.sqrt(2)/2
    rt_3_2 = math.sqrt(3)/2
    unit_circle = [
        (0, (1,0),),
        (30, (rt_3_2, n1_2),),
        (45, (rt_2_2,rt_2_2),),
        (60, (n1_2,rt_3_2),),
        (90, (0,1),),
        (120, (-n1_2,rt_3_2),),
        (135, (-rt_2_2,rt_2_2),),
        (150, (-rt_3_2, n1_2),),
        (180, (-1,0),),
        (210, (-rt_3_2, -n1_2),),
        (225, (-rt_2_2,-rt_2_2),),
        (240, (-n1_2,-rt_3_2),),
        (270, (0,-1),),
        (300, (n1_2,-rt_3_2),),
        (315, (rt_2_2,-rt_2_2),),
        (330, (rt_3_2, -n1_2),),
    ]

    mid_point = win.get_mid_point()

    for angle, distance_tuple in unit_circle:
        ##RED
        start_point = Point(
            mid_point.x + distance_tuple[0] * 10,
            mid_point.y + distance_tuple[1] * 10,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 20,
            mid_point.y + distance_tuple[1] * 20,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "red")
        ##ORANGE
        start_point = Point(
            mid_point.x + distance_tuple[0] * 30,
            mid_point.y + distance_tuple[1] * 30,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 50,
            mid_point.y + distance_tuple[1] * 50,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "orange")

        ##YELLOW
        start_point = Point(
            mid_point.x + distance_tuple[0] * 60,
            mid_point.y + distance_tuple[1] * 60,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 90,
            mid_point.y + distance_tuple[1] * 90,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "yellow")
        ##GREEN
        start_point = Point(
            mid_point.x + distance_tuple[0] * 100,
            mid_point.y + distance_tuple[1] * 100,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 140,
            mid_point.y + distance_tuple[1] * 140,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "green")
        ##BLUE
        start_point = Point(
            mid_point.x + distance_tuple[0] * 150,
            mid_point.y + distance_tuple[1] * 150,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 200,
            mid_point.y + distance_tuple[1] * 200,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "blue")
        ##VIOLET
        start_point = Point(
            mid_point.x + distance_tuple[0] * 210,
            mid_point.y + distance_tuple[1] * 210,
        )
        end_point = Point(
            mid_point.x + distance_tuple[0] * 270,
            mid_point.y + distance_tuple[1] * 270,
        )
        line = Line(start_point, end_point)
        win.draw_line(line, "violet")
