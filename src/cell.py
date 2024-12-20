from window import Window
from point import Point
from line import Line

class Cell():
    '''
    A class to represent a cell of the maze grid.
    '''

    def __init__(
        self,
        win: Window,
    ):
        '''
        The constructor of the Cell class.

        Parameters :
            _win (Window) : Access to the window to draw itself

        Attributes :
            has_left_wall (bool) : A potential cell wall (line)
            has_right_wall (bool) : A potential cell wall (line)
            has_top_wall (bool) : A potential cell wall (line)
            has_bottom_wall (bool) : A potential cell wall (line)
            _x1 (int) : Top-left corner value
            _x2 (int) : Bottom-right corner value
            _y1 (int) : Top-left corner value
            _y2 (int) : Bottom-right corner value

        '''

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        '''
        Draw the cell.
        '''
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_top_wall:
            p1 = Point(x1, y1)
            p2 = Point(x2, y1)
            top_wall = Line(p1, p2)
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            p1 = Point(x2, y1)
            p2 = Point(x2, y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            p1 = Point(x1, y2)
            p2 = Point(x2, y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall)
        if self.has_left_wall:
            p1 = Point(x1, y1)
            p2 = Point(x1, y2)
            left_wall = Line(p1, p2)
            self._win.draw_line(left_wall)

        # TODO draw btw cells