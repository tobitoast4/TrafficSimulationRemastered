from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import utils

class IGraphicsCar(QGraphicsItem):
    def __init__(self, car, parent=None):
        super().__init__(parent)
        self.car = car
        self.radius = 25

        self.pen_default = QPen(QColor("#00000000"))
        self.pen_default.setWidth(2)
        self.pen_selected = QPen(QColor("#FF000000"))
        self.pen_selected.setWidth(10)
        self.brush = QBrush(Qt.black)

        self.initUi()

    def updateBrush(self, v_max):
        velocity = self.car.velocity
        color = utils.get_new_color(velocity, v_max)
        self.brush = QBrush(QColor(color))
        self.update()

    def boundingRect(self):
        return QRectF(
            0 - (self.radius//2),
            0 - (self.radius//2),
            self.radius,
            self.radius
        ).normalized()

    def initUi(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)


    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        path_outline = QPainterPath()
        # path_outline.addRoundedRect(0, 0, self.radius, self.radius, self.radius, self.radius)
        path_outline.addEllipse(0 - (self.radius//2), 0 - (self.radius//2), self.radius, self.radius)
        painter.setPen(self.pen_default if not self.isSelected() else self.pen_selected)
        painter.setBrush(self.brush)
        painter.drawPath(path_outline.simplified())

