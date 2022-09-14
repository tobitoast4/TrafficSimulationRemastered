from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from TrafficSimulationRemastered import utils

from TrafficSimulationRemastered.main_diagram_widget.scene import Scene
from TrafficSimulationRemastered.main_diagram_widget.graphics_view import IGraphicsView


class MainDiagramWidget(QWidget):
    def __init__(self, v_max, parent=None):
        super().__init__(parent)
        self.color_array = utils.get_new_color_array(v_max)

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

        self.layout.addWidget(self.view)
        # self.setWindowTitle("Stau Simulation")
        self.drawTest()

    def drawTest(self):
        velocity = 4
        color = self.color_array[velocity]
        brush = QBrush(QColor(color))
        self.grScene.addRect(0, 0, 100, 100, QPen(Qt.NoPen), brush)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     wnd = MainDiagramWidget(5)
#     wnd.show()
#     sys.exit(app.exec_())