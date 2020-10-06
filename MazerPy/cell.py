class cell(object):
    """cell: single cell in the maze"""

    
    def __init__(self, x, y):
        """initiate the cell object with specific (x,y)
every cell has 4 walls, initated as True to represent that they exist.
visited: represents if the cell has been visited"""

        self.x = x
        self.y = y
        #walls order (to fit abs(x-3)):
        #0=up,1=left,2=right,3=down
        self.walls = [True] * 4
        self.visited = False
        #contains the parent in the BFS view; used for solutions
        self.parent = 0
   
    
    def getX(self):
        """return the X coordinate of the cell"""

        return self.x

    
    def getY(self):
        """return the Y coordinate of the cell"""

        return self.y
    
    
    def getWalls(self):
        """returns the walls array of the cell"""

        return self.walls
    
    
    def isVisited(self):
        """checking if the cell is visited"""

        return self.visited

    
    def visit(self):
        """"visits" the cell"""

        self.visited = True


    def unvisit(self):
        """"unvisit" the cell"""
    
        self.visited = False


    def getParent(self):
        """returns the parent of the cell"""

        return self.parent


    def setParent(self, parent):
        """sets the parent for the cell, used for solution.
expects parent=cell"""

        self.parent = parent


    def removeWall(self, wall): #wall=int between 0-3
        """removes a certain wall from the cell"""

        self.walls[wall] = False

    
    def removeWalls(self, wall, cell):
        """removes the walls between two adjacent cells"""

        self.removeWall(wall)
        cell.removeWall(abs(wall-3))

