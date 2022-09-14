from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from TrafficSimulationRemastered import utils

from TrafficSimulationRemastered.main_diagram_widget.scene import Scene
from TrafficSimulationRemastered.main_diagram_widget.graphics_view import IGraphicsView
from TrafficSimulationRemastered.main_widget.car import Car


class MainDiagramWidget(QWidget):
    def __init__(self, v_max, parent=None):
        super().__init__(parent)
        self.color_array = utils.get_new_color_array(v_max)

        self.width = 4 # px
        self.current_line = 0

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
        # self.drawTest()


    def drawLine(self, cells):
        for c in range(len(cells)):
            if cells[c] is None:
                continue
            if isinstance(cells[c], Car):
                v = cells[c].velocity
                color = self.color_array[v]
                brush = QBrush(QColor(color))
                self.grScene.addRect(c * self.width,
                                     self.current_line * self.width,
                                     self.width,
                                     self.width,
                                     QPen(Qt.NoPen), brush)
        self.current_line += 1



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     wnd = MainDiagramWidget(5)
#     wnd.show()
#     sys.exit(app.exec_())