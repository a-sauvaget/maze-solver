from tkinter import Tk, BOTH, Canvas

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
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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
