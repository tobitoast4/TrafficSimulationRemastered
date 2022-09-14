import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class IGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(None)
        self.scene = scene

    def setGrScene(self, width, height):
        self.setSceneRect(0, 0, width, height)

