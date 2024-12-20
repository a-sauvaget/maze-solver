from tkinter import Canvas
from point import Point

class Line():
    '''
    A class to represent a line on the window
    '''

    def __init__(self, point1: Point, point2: Point):
        '''
        The constructor of the Line class

        Parameters :
            point1 (Point) : The first point of the line
            point2 (Point) : The seconf point of the line
        '''
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str):
        '''
        Create a line between two points.

        Parameters:
            canvas (Canvas) : Widget to display a line
            fill_color (str) : The color of the line
        '''
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)