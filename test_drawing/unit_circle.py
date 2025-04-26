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
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 10),
            get_point_from_vector(mid_point, distance_tuple, 20),
        )
        win.draw_line(line, "red")
        ##ORANGE
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 30),
            get_point_from_vector(mid_point, distance_tuple, 50),
        )
        win.draw_line(line, "orange")

        ##YELLOW
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 60),
            get_point_from_vector(mid_point, distance_tuple, 90),
        )
        win.draw_line(line, "yellow")
        ##GREEN
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 100),
            get_point_from_vector(mid_point, distance_tuple, 140),
        )
        win.draw_line(line, "green")
        ##BLUE
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 150),
            get_point_from_vector(mid_point, distance_tuple, 200),
        )
        win.draw_line(line, "blue")
        ##VIOLET
        line = Line(
            get_point_from_vector(mid_point, distance_tuple, 210),
            get_point_from_vector(mid_point, distance_tuple, 270),
        )
        win.draw_line(line, "violet")

def get_point_from_vector(point, vector, magnitude):

    return Point(
        point.x + (vector[0] * magnitude),
        point.y + (vector[1] * magnitude),
    )
