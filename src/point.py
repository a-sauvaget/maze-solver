class Point():
    '''
    A class to represent a point of a line.
    '''

    def __init__(self, x: int, y: int):
        '''
        The constructor of the Point class.

        x=0 is the left of the screen.
        y=0 is the top of the screen.

        Parameters:
            x (int) : the x-coordinate (horizontal) in pixels of the point
            y (int) : the y-coordinate (vertical) in pixels of the point
        '''

        self.x = x
        self.y = y