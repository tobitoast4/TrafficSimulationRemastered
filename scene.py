from graphics_scene import *
from car import Car

class Scene():
    def __init__(self):
        self.scene_width = 2000
        self.scene_height = 2000

        self.radius = 900
        self.radius_gap = 25
        self.amount_cells = 240

        self.cells = []
        self.cars = []

        self.initUi()
        self.initCells()

    def initUi(self):
        self.grScene = IGraphicsScene(self, self.radius, self.radius_gap, self.amount_cells)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def initCells(self):
        radius = self.radius + (self.radius_gap // 2)
        distance = 2 * math.pi / self.amount_cells
        for k in range(self.amount_cells):
            x = round(radius * math.cos((k + 0.5) * distance))
            y = round(radius * math.sin((k + 0.5) * distance))
            self.cells.append([x, y])
        print(self.cells)

    def addCar(self, car, x, y):
        self.cars.append(car)
        self.grScene.addItem(car.grCar)
        car.grCar.setPos(x, y)

    def removeCar(self, car):
        self.cars.remove(car)