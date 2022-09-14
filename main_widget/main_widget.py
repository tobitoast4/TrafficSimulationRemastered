from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from TrafficSimulationRemastered.main_widget.scene import Scene
from TrafficSimulationRemastered.main_widget.graphics_view import IGraphicsView

import time

class NodeEditorWnd(QWidget):
    def __init__(self, start_velocity, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.setStyleSheet("border-width: 0px; border-style: solid")
        # create graphics scene

        self.scene = Scene(parent)
        self.grScene = self.scene.grScene

        # create graphics view
        self.view = IGraphicsView(self.grScene, self)
        self.view.setScene(self.grScene)

        self.main_bg_thread = IThread(start_velocity)
        self.main_bg_thread.move.connect(self.moveCars)
        self.main_bg_thread.start()

        self.layout.addWidget(self.view)
        # self.setWindowTitle("Stau Simulation")

    def moveCars(self, paused):
        self.scene.moveCars(paused)


class IThread(QThread): # see https://stackoverflow.com/a/44329475/14522363
    move = pyqtSignal(bool)

    def __init__(self, start_velocity):
        self.time_wait = start_velocity
        self.paused = True
        super().__init__()

    def run(self):
        while True:
            self.move.emit(self.paused)
            time.sleep(self.time_wait)