import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class IGraphicsScene(QGraphicsScene):
    def __init__(self, scene, radius, radius_gap, amount_cells, parent=None):
        super().__init__(None)
        self.scene = scene
        # settings
        self.grid_size = 20
        self.color_background = QColor("#FFFFFF")
        self.color_light = QColor("#444444")
        self.pen_light = QPen(self.color_light)
        self.pen_light.setWidth(0.1)
        self.setBackgroundBrush(self.color_background)
        # circle settings
        self.radius = radius
        self.radius_gap = radius_gap
        self.amount_cells = amount_cells

    def setGrScene(self, width, height):
        self.setSceneRect(-width//2, -height//2, width, height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        radius1 = self.radius
        radius2 = self.radius + self.radius_gap
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

        # inner circle
        path_inner = QPainterPath()
        path_inner.addEllipse(0 - self.radius, 0 - self.radius, self.radius*2-1, self.radius*2-1)
        painter.setPen(self.pen_light)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_inner.simplified())

        #outer circle
        path_outer = QPainterPath()
        path_outer.addEllipse(0 - self.radius - self.radius_gap, 0 - self.radius - self.radius_gap,
                              (self.radius + self.radius_gap) * 2 + 1, (self.radius + self.radius_gap) * 2 + 1)
        painter.setPen(self.pen_light)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outer.simplified())

    # def drawBackground(self, painter, rect): # OLD
    #     super().drawBackground(painter, rect)
    #
    #     left = int(math.floor(rect.left()))
    #     right = int(math.ceil(rect.right()))
    #     top = int(math.floor(rect.top()))
    #     bottom = int(math.ceil(rect.bottom()))
    #
    #     first_left = left - (left % self.grid_size)
    #     first_top = top - (top % self.grid_size)
    #
    #     lines_light = []
    #     for x in range(first_left, right, self.grid_size):
    #         lines_light.append(QLine(x, top, x, bottom))
    #
    #     for y in range(first_top, bottom, self.grid_size):
    #         lines_light.append(QLine(left, y, right, y))
    #
    #
    #     painter.setPen(self.pen_light)
    #     painter.drawLines(*lines_light)