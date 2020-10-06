import cell
import random
from collections import deque

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
    
                
    def clearVisits(self):
        """clears all visited flags from the maze"""

        for x in range (0, len(self.cells)):
            for y in range (0, len(self.cells)):
                self.cells[x][y].unvisit()

    
    def getNextNeighbor(self, x, y, randomize=True):    #perhaps I should to separate it to 2 funcs
        """check if there are any unvisited cells adjacent to the current cell
return randomly one the these cells for the DFS algorithm, or -1 if there are no cells;
if chosen, returns all neighbors (insert value False for parameter randomize)"""

        size = len(self.cells)
        neighbors = []
        #left cell
        if x>0 and self.cells[(x-1)][y].isVisited()==False:
            if (randomize or (not randomize and self.cells[x][y].walls[1])):
                neighbors.append(self.cells[(x-1)][y])
        #right cell
        if x<size-1 and self.cells[(x+1)][y].isVisited()==False:
            if (randomize or (not randomize  and self.cells[x][y].walls[2])):
                neighbors.append(self.cells[(x+1)][y])
        #up cell
        if y>0 and self.cells[x][(y-1)].isVisited()==False:
            if (randomize or (not randomize  and self.cells[x][y].walls[0])):
                neighbors.append(self.cells[x][(y-1)])
        #down cell
        if y<size-1 and self.cells[x][(y+1)].isVisited()==False:
            if (randomize or (not randomize  and self.cells[x][y].walls[3])):
                neighbors.append(self.cells[x][(y+1)])

        if (randomize):
            #randomly choose one of the cells
            rnd = -1
            if (len(neighbors)>0):
                rnd = random.randrange(len(neighbors))
                return (neighbors[rnd])    
            return rnd
        else:
            return neighbors

    def create(self):
        """main function for creating the maze:
use DFS to run through all the cells (randomly)
break walls between 2 unvisited cells to create the maze pattern"""

        print ("Creating the maze...\n")        #debugging usage
        #first make sure cells are unvisited
        self.clearVisits()
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
            nextNeighbor = self.getNextNeighbor(curr.getX(), curr.getY())
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


    def solve(self):
        """main function for automatically solving the maze, using BFS"""

        print ("solving the maze...")   #debugging usage
        #first make sure cells are unvisited
        self.clearVisits()
        #using queue as per BFS algorithm to run through the maze
        cellQueue = deque([])
        #start from [0][0] and continue from there
        cellQueue.append(self.cells[0][0])
        self.cells[0][0].visit()
        #solution list will contain the shortest path
        solution = []

        #BFS:
        while (len(cellQueue) != 0):
            curr = cellQueue.popleft()
            #if current cell is the finish line, stop running
            if (curr == self.cells[-1][-1]):
                break

            #if not, check all adjacent cells and move to one of them
            #also provide them with a parent (will be used for solution)
            neighbors = self.getNextNeighbor(curr.getX(),curr.getY(),False)
            for adjacentCell in neighbors:
                if (not adjacentCell.isVisited()):
                    adjacentCell.visit()
                    adjacentCell.setParent(curr)
                    cellQueue.append(adjacentCell)

        #run through the parents from the finish line to the top
        curr = self.cells[-1][-1]
        solution.append(curr)
        while curr.getParent() != 0:
            solution.append(curr.getParent())
            curr = curr.getParent()

        print ("Finished solving!")     #debugging usage
        return solution

    
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