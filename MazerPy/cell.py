class cell(object):
    """cell: single cell in the maze"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True] * 4
        self.visited = False
   
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getWalls(self):
        return self.walls
    
    def isVisited(self):
        return self.visited

    def visit(self):
        self.visited = True

    #do I need that?
    def removeWall(self, wall): #wall=int between 0-3
        self.walls[wall] = False

    def removeWalls(self, wall, cell):
        self.removeWall(wall)
        cell.removeWall(abs(wall-3))

    #add drawing capabilities

