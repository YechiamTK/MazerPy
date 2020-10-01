import cell
import maze
from itertools import chain

from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class Window(QMainWindow):
    def __init__(self, maze):
        super().__init__()

        self.title = "MazerPy"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.initWindow()
        self.maze = maze  #assuming cells be a maze type

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show() 

    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.red)
        painter.setBrush(Qt.white)

        size = self.maze.size()
        listIt = chain.from_iterable(zip(*self.maze.getCells()))
        cellIt = iter(listIt)
        x=0
        y=0
        while True:
            try:        
                curr = next(cellIt)
                walls = curr.getWalls()
                
                if (walls[0]):          #up wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+50,
                                     curr.getX()*50+50,curr.getY()*50+100)
                if (walls[1]):          #right wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+100,
                                     curr.getX()*50+100,curr.getY()*50+100)
                if (walls[2]):          #down wall
                    painter.drawLine(curr.getX()*50+100,curr.getY()*50+50,
                                     curr.getX()*50+100,curr.getY()*50+100)
                if (walls[3]):          #left wall
                    painter.drawLine(curr.getX()*50+50,curr.getY()*50+50,
                                     curr.getX()*50+100,curr.getY()*50+50)
            except StopIteration:
                break


def main():
    print ("hi\n")
    myMaze = maze.maze(10)
    myMaze.create()
    myMaze.printMaze()  #testing purposes only
    App = QApplication(sys.argv)
    window = Window(myMaze)
    sys.exit(App.exec())


    
if __name__ == "__main__":
    main()






