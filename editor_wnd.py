from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from scene import Scene
from graphics_view import IGraphicsView
from car import Car

class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        # self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()
        self.grScene = self.scene.grScene
        car = Car(self.scene, 0, 0)


        # create graphics view
        self.view = IGraphicsView(self.grScene, self)
        self.view.setScene(self.grScene)


        self.layout.addWidget(self.view)
        self.setWindowTitle("WindowTitle")
        self.show()

        self.addTest()




    def addTest(self):
        brush = QBrush(Qt.red)
        outline = QPen(Qt.black)
        outline.setWidth(1)

        rect = self.grScene.addEllipse(-100, -100, 20, 20, outline, brush)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)