from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from scene import Scene
from graphics_view import IGraphicsView

import time

class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 700, 700)
        self.layout = QVBoxLayout()
        # self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()
        self.grScene = self.scene.grScene

        # create graphics view
        self.view = IGraphicsView(self.grScene, self)
        self.view.setScene(self.grScene)

        self.th = IThread()
        self.th.move.connect(self.moveCars)
        self.th.start()

        self.layout.addWidget(self.view)
        self.setWindowTitle("Stau Simulation")
        self.show()

    def moveCars(self):
        self.scene.moveCars()


class IThread(QThread): # see https://stackoverflow.com/a/44329475/14522363
    move = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.move.emit()
            time.sleep(0.1)