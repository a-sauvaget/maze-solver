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

        Parameters :
            x1 (int), y1 (int) : How many pixels from the top and left the maze should start from the side of the window
            num_rows (int) : Number of rows of the maze,
            num_cols (int) : Number of columns of the maze,
            cell_size_x (int) : Base point x for the size of the cell,
            cell_size_y (int) : Base point y of the cell,
            win (Window) : Access to the window to draw itself
        '''
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        '''
        A list of cells to draw (maze shape).
        '''
        self._cells = []

        for r in range(self.num_rows):
            rows = []
            for c in range(self.num_cols):
                cell = Cell(self.win)
                rows.append(cell)
            self._cells.append(rows)
            
    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass