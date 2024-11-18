import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class IGraphicsScene(QGraphicsScene):
    def __init__(self, scene, radius, radius_gap, amount_cells, parent=None):
        super().__init__(None)
        self.scene = scene
        # settings
        self.color_background = QColor("#FFFFFF")
        self.color_light = QColor("#444444")
        self.pen_light = QPen(self.color_light)
        # self.pen_light.setWidth(0.1)
        self.setBackgroundBrush(self.color_background)
        # circle settings
        self.radius = radius
        self.radius_gap = radius_gap
        self.amount_cells = amount_cells
        self.amount_lanes = 1

    def setGrScene(self, width, height):
        self.setSceneRect(-width//2, -height//2, width, height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        radius1 = self.radius
        radius2 = self.radius + self.radius_gap*self.amount_lanes
        distance = 2*math.pi / self.amount_cells
        lines = []
        for k in range(self.amount_cells):
            x1 = round(radius1 * math.cos(k * distance))
            y1 = round(radius1 * math.sin(k * distance))
            x2 = round(radius2 * math.cos(k * distance))
            y2 = round(radius2 * math.sin(k * distance))

            lines.append(QLine(x1, y1, x2, y2))

        painter.setPen(self.pen_light)
        painter.drawLines(*lines)

        for i in range(self.amount_lanes + 1):
            path_outer = QPainterPath()
            path_outer.addEllipse(0 - self.radius - self.radius_gap*i, 0 - self.radius - self.radius_gap*i,
                                  (self.radius + self.radius_gap*i) * 2 + 1, (self.radius + self.radius_gap*i) * 2 + 1)
            painter.setPen(self.pen_light)
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(path_outer.simplified())

