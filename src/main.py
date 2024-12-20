from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    point = Point(0, 10)
    point2 = Point(10, 10)
    point3 = Point(10, 200)
    point4 = Point(20, 300)
    line = Line(point, point2)
    line2 = Line(point3, point4)
    win.draw_line(line, "red")
    win.draw_line(line2, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
