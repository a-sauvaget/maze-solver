from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    '''
    A class to represent an application window.
    '''

    def __init__(self, width: int, height: int):
        '''
        The constructor for Window class.

        Parameters:
            width (int) : The width of the window
            height (int) : The height of the window
        '''
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def draw_line(self, line: Line, fill_color="black"):
        '''
        Draw a line on the window

        Parameters :
            line (Line) : An instance of a Line
            fill_color (str) : The color of the line
        '''

        line.draw(self.__canvas, fill_color)
    
    def draw_move(self, to_cell, undo=False):
        pass

    def redraw(self):
        '''
        Redraw all the graphics on the window.
        '''
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        '''
        Track the running state of the window.
        '''
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        '''
        Close the window.
        '''
        self.__running = False


