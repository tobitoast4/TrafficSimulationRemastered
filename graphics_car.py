from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class IGraphicsCar(QGraphicsItem):
    def __init__(self, car, parent=None):
        super().__init__(parent)

        self.radius = 20

        self.pen_default = QPen(QColor("#00000000"))
        self.pen_default.setWidth(2)
        self.pen_selected = QPen(QColor("#FF000000"))
        self.pen_selected.setWidth(2)

        self.initUi()

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
        painter.setBrush(QBrush(QBrush(Qt.red)))
        painter.drawPath(path_outline.simplified())