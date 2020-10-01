import cell
import random
from itertools import chain

class maze(object):
    """represents all features of a maze"""

    def __init__(self, size):
        self.cells = [[0] * size for i in range(size)]
        for x in range (0, size):
            for y in range (0, size):
                self.cells[x][y] = cell.cell(x,y)

    def isThereUnvisited(self):
        for row in self.cells:
            for cel in row:
                if(cel.isVisited() == False):
                    return True
    
    def checkNeighbors(self, x, y):
        size = self.cells.__len__()
        neighbors = []
        if x>0:
            if self.cells[(x-1)][y].isVisited()==False:
                neighbors.append(self.cells[(x-1)][y])
        if x<size-1:
            if self.cells[(x+1)][y].isVisited()==False:
                neighbors.append(self.cells[(x+1)][y])
        if y>0:
            if self.cells[x][(y-1)].isVisited()==False:
                neighbors.append(self.cells[x][(y-1)])
        if y<size-1:
            if self.cells[x][(y+1)].isVisited()==False:
                neighbors.append(self.cells[x][(y+1)])

        rnd = -1
        if (neighbors.__len__()>0):
            rnd = random.randrange(neighbors.__len__())
            return (neighbors[rnd])    #0=rows=x; 1=cols=y
        return rnd

    def create(self):
        print ("Creating the maze...\n")
        listIt = list(chain.from_iterable(zip(*self.cells)))
        cellsIt = iter(listIt)
        curr = next(cellsIt)
        curr.visit()
        cellStack = []
        nextNeighbor = 0
        wall = 0
        x=1
        while (self.isThereUnvisited()):
            print (x, "iteration")
            nextNeighbor = self.checkNeighbors(curr.getX(), curr.getY())
            if nextNeighbor != -1:
                print ("neighbor exists!")
                nextCell = nextNeighbor
                cellStack.append(curr)
                if (curr.getX()-nextCell.getX()) == 1:
                    wall = 0                    #up wall
                    print ("took down a wall!")
                elif (curr.getX()-nextCell.getX()) == -11:
                    wall = 2                    #down wall
                    print ("took down a wall!")
                elif (curr.getY()-nextCell.getY()) == 1:
                    wall = 1                    #right wall
                    print ("took down a wall!")
                elif (curr.getY()-nextCell.getY()) == -1:
                    wall = 3 #not 4             #left wall
                    print ("took down a wall!")
                curr.removeWalls(wall, nextCell)

                curr = next(cellsIt)
                curr.visit()

            elif cellStack.__len__()>0:
                curr = cellStack.pop()
            x+=1

        print ("Finished creating the maze!\n")

    def printMaze(self):
        #needs to be GUI (PyQt) and reflect cells' walls
        #but just for testing purposes: printing data
        #MOVED TO THE MAIN .PY
        print ("Printing...\n")
        for row in self.cells:
            for cel in row:
                print (cel.getX(), " ", cel.getY(), " ", cel.getWalls())
        

    def size(self):
        return self.cells.__len__()

    def getCells(self):
        return self.cells