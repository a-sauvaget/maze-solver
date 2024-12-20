from tkinter import Tk, BOTH, Canvas

class Window:
    '''
    A class to represent an application window.

    ...

    Attributes
    ----------
    width : int
        width of the window
    height : int
        height of the window

    Methods
    -------
    redraw():
        Redraw all the grpaphics in the window
    wait_for_close():
        Doc
    close():
        Doc
    '''
    
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
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
