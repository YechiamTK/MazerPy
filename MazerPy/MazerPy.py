import cell
import maze
from itertools import chain

from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class Window(QMainWindow):
    """the PyQt class"""

    
    def __init__(self, maze):
        """initiate the window for PyQt"""

        super().__init__()

        self.title = "MazerPy"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.initWindow()
        self.maze = maze  #assuming cells be a maze type (note: will add type hints later)

    
    def initWindow(self):
        """auxiliary function for window initiation"""

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show() 

    
    def paintEvent(self, event):
        """painting function; used for painting the maze"""

        painter = QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        #maze drawing:
        painter.setPen(Qt.red)
        painter.setBrush(Qt.white)

        #creates an iterator to iterate over the cells array
        listIt = chain.from_iterable(zip(*self.maze.getCells()))
        cellIt = iter(listIt)

        while True:
            try:        
                curr = next(cellIt)
                walls = curr.getWalls()
                
                #draw the lines for each wall per cell
                if (walls[0] and not (curr.getX()==0 and curr.getY()==0)):  #don't draw for first cell
                    #up wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+50,
                                     curr.getX()*50+50,curr.getY()*50+100)
                if (walls[2]):
                    #right wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+100,
                                     curr.getX()*50+100,curr.getY()*50+100)
                if (walls[3] and not (curr.getX()==self.maze.size()-1 and
                                     curr.getY()==self.maze.size()-1)):  #don't draw for last cell
                    #down wall
                    painter.drawLine(curr.getX()*50+100,curr.getY()*50+50,
                                     curr.getX()*50+100,curr.getY()*50+100)
                if (walls[1]):
                    #left wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+50,
                                     curr.getX()*50+100,curr.getY()*50+50)
            #StopIteration means we've reached the end of the cells array
            except StopIteration:
                break
            
        #solution drawing:
        painter.setPen(Qt.transparent)
        painter.setBrush(Qt.black)
        solution = []
        #solve solution using BFS
        solution = self.maze.solve()
        #creates an iterator to iterate over the solution array
        cellIt = iter(solution)

        #draw rects for each cell in the solution list
        while True:
           try:
               curr = next(cellIt)
               painter.drawRect(curr.getX()*50+50,curr.getY()*50+50,50,50)
           #StopIteration means we've reached the end of the cells array
           except StopIteration:
               break
        


#main function for the program
def main():
    #debugging usage
    print ("hi\n")
    #creating the maze: maze(x) such as x**2 is the whole maze
    myMaze = maze.maze(15)
    myMaze.create()
    myMaze.solve()
    #myMaze.printMaze()  #debugging usage
    #creating the PyQt app
    App = QApplication(sys.argv)
    window = Window(myMaze)
    sys.exit(App.exec())


    
if __name__ == "__main__":
    main()






