import time

from window import Window
from cell import Cell

class Maze():
    '''
    A class to represent the maze.
    '''

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        '''
        The constructor of the Maze class.

        Attribute : 
            _cells (list) : The labirynthe's cell list

        Parameters :
            x1 (int), y1 (int) : How many pixels from the top and left the maze should start from the side of the window
            num_rows (int) : Number of rows of the maze,
            num_cols (int) : Number of columns of the maze,
            cell_size_x (int) : Base point x for the size of the cell,
            cell_size_y (int) : Base point y of the cell,
            win (Window) : Access to the window to draw itself
        '''
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
    
    def _create_cells(self):
        '''
        A list of cells to draw (maze shape).
        '''
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        
            
    def _draw_cell(self, i: int, j: int):
        '''
        Draw a single cell on the window.

        Parameters :
            i (int) : Number of the row
            j (int) : Number of the cell
        '''
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        '''
        Visualize the cell being drawn.
        '''
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)