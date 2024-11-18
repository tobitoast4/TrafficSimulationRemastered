from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import utils

from main_diagram_widget.scene import Scene
from main_diagram_widget.graphics_view import IGraphicsView
from main_widget.car import Car


class MainDiagramWidget(QWidget):
    def __init__(self, v_max, parent=None):
        super().__init__(parent)
        self.color_array = utils.get_new_color_array(v_max)

        self.width = 4 # px
        self.current_line = 0
        self.amount_lines = 250
        self.lines = []

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
        new_line = []
        for c in range(len(cells)):
            if cells[c] is None:
                continue
            if isinstance(cells[c], Car):
                v = cells[c].velocity
                color = self.color_array[v]
                brush = QBrush(QColor(color))
                dot = self.grScene.addRect(c * self.width,
                                           self.current_line * self.width,
                                           self.width,
                                           self.width,
                                           QPen(Qt.NoPen), brush)
                new_line.append(dot)
        self.lines.append(new_line)

        if self.current_line < self.amount_lines:
            self.current_line += 1
            pass
        else:
            self.current_line += 1
            top_line = self.lines[0]
            for c in top_line:
                self.grScene.removeItem(c)
            self.lines.pop(0)
            # for x in range(len(self.lines)):
            #     line_x = self.lines[x]
            #     for y in range(len(line_x)):
            #         dot = self.lines[x][y]
            #         dot.moveBy(0, -self.width)



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     wnd = MainDiagramWidget(5)
#     wnd.show()
#     sys.exit(app.exec_())