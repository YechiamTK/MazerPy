import cell
import maze
import math

from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    main()


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

        size = math.sqrt(self.maze.size())
        cellIt = iter(self.maze.getCells())
        curr = next(cellIt)
        #GOING TO WRITE HERE THE PAINT AS FOLLOW:
        #LINES FOR EACH WALL=TRUE IN EACH CELL IN maze.cells


def main():
    print ("hi\n")
    myMaze = maze.maze(10)
    myMaze.create()
    myMaze.printMaze()









