import cell
import random

class maze(object):
    """represents all features of a maze"""

    
    def __init__(self, size):
        """initiate the maze with a 2d array of cells (list)"""

        self.cells = [[0] * size for i in range(size)]
        for x in range (0, size):
            for y in range (0, size):
                self.cells[x][y] = cell.cell(x,y)

    
    def isThereUnvisitedCells(self):
        """check the cells array for unvisited cells"""

        for row in self.cells:
            for cel in row:
                if(cel.isVisited() == False):
                    return True
    
    
    def checkForNextNeighbor(self, x, y):
        """check if there are any unvisited cells adjacent to the current cell
return randomly one the these cells for the DFS algorithm, or -1 if there are no cells"""

        size = len(self.cells)
        neighbors = []
        #left cell
        if x>0 and self.cells[(x-1)][y].isVisited()==False:
                neighbors.append(self.cells[(x-1)][y])
        #right cell
        if x<size-1 and self.cells[(x+1)][y].isVisited()==False:
                neighbors.append(self.cells[(x+1)][y])
        #up cell
        if y>0 and self.cells[x][(y-1)].isVisited()==False:
                neighbors.append(self.cells[x][(y-1)])
        #down cell
        if y<size-1 and self.cells[x][(y+1)].isVisited()==False:
                neighbors.append(self.cells[x][(y+1)])

        #randomly choose one of the cells
        rnd = -1
        if (len(neighbors)>0):
            rnd = random.randrange(len(neighbors))
            return (neighbors[rnd])    
        return rnd


    def create(self):
        """main function for creating the maze:
use DFS to run through all the cells (randomly)
break walls between 2 unvisited cells to create the maze pattern"""

        print ("Creating the maze...\n")        #debugging usage
        #start from [0][0] and continue from there
        curr = self.cells[0][0]
        curr.visit()
        #cellStack: save the run-down cells until reaching 
        #visited cell; then pop the previous one from the cell 
        cellStack = []
        nextNeighbor = 0
        wall = 0
        while (self.isThereUnvisitedCells()):
            #check for the unvisited neighbors and take randomly one of them
            nextNeighbor = self.checkForNextNeighbor(curr.getX(), curr.getY())
            if nextNeighbor != -1:  #if there is an unvisited neighbor
                cellStack.append(curr)
                #check for the relation between the cells (which direction)
                if (curr.getX()-nextNeighbor.getX()) == 1:
                    wall = 0                    #up wall
                elif (curr.getX()-nextNeighbor.getX()) == -1:
                    wall = 3                    #down wall
                elif (curr.getY()-nextNeighbor.getY()) == 1:
                    wall = 1                    #left wall
                elif (curr.getY()-nextNeighbor.getY()) == -1:
                    wall = 2                    #right wall
                #break the walls between them
                curr.removeWalls(wall, nextNeighbor)

                #move on to the next neighbor and continue the DFS scheme
                curr = nextNeighbor
                curr.visit()

            #if return to the previous cell if there aren't any neighbors
            elif len(cellStack)>0:      
                curr = cellStack.pop()

        #debugging usage
        print ("Finished creating the maze!\n")

    
    def printMaze(self):
        """debugging usage"""

        print ("Printing...\n")
        for row in self.cells:
            for cel in row:
                print (cel.getX(), " ", cel.getY(), " ", cel.getWalls())
        
    
    def size(self):
        """return the size of the maze by the count of the cells"""

        return len(self.cells)

    
    def getCells(self):
        """return the cells array"""

        return self.cells