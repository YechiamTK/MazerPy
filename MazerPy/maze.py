import cell
import random
import math

class maze(object):
    """represents all features of a maze"""

    def __init__(self, size):
        self.cells = [[0] * size for i in range(size)]
        for x in range (0, size):
            for y in range (0, size):
                self.cells[x][y] = cell.cell(x,y)

    def isThereUnvisited(self):
        for cel in self.cells:
            if(cel.isVisited() == False):
                return True
    
    def checkNeighbors(self, x, y):
        size = math.sqrt(self.cells.__len__())
        neighbors = []
        #NEED REPAIR!
        if x>0:
            if self.cells[(x-1)*int(size)+y].isVisited()==False:
                neighbors.append(self.cells[(x-1)*int(size)+y])
        if x<size-1:
            if self.cells[(x+1)*int(size)+y].isVisited()==False:
                neighbors.append(self.cells[(x+1)*int(size)+y])
        if y>0:
            if self.cells[x*int(size)+y-1].isVisited()==False:
                neighbors.append(self.cells[x*int(size)+y-1])
        if y<size-1:
            if self.cells[x*int(size)+y+1].isVisited()==False:
                neighbors.append(self.cells[x*int(size)+y+1])
        rnd = -1
        if (neighbors.__len__()>0):
            rnd = random.randrange(neighbors.__len__())
            return (self.cells[rnd].getX()*int(size)+self.cells[rnd].getY())    #NEED REPAIR!
        return rnd

    def create(self):
        cellsIt = iter(self.cells)
        curr = next(cellsIt)
        curr.visit()
        cellStack = []
        nextNeighbor = 0
        wall = 0
        while (self.isThereUnvisited()):
            nextNeighbor = self.checkNeighbors(curr.getX(), curr.getY())
            if nextNeighbor != -1:
                nextCell = self.cells[nextNeighbor]
                cellStack.append(curr)
                if (curr.getX()-nextCell.getX()) == 1:
                    wall = 0
                elif (curr.getX()-nextCell.getX()) == -11:
                    wall = 2
                elif (curr.getY()-nextCell.getY()) == 1:
                    wall = 1
                elif (curr.getY()-nextCell.getY()) == -1:
                    wall = 3 #not 4
                curr.removeWalls(wall, nextCell)

                curr = next(cellsIt)
                curr.visit()

            elif cellStack.__len__()>0:
                curr = cellStack.pop()


    def printMaze(self):
        #needs to be GUI (PyQt) and reflect cells' walls
        #but just for testing purposes: printing data
        #MOVED TO THE MAIN .PY
        for cel in self.cells:
            print (cel.getX(), " ", cel.getY(), " ", cel.getWalls())
        

    def size(self):
        return self.cells.__len__()

    def getCells(self):
        return self.cells