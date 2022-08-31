from graphics_car import IGraphicsCar

class Car():
    def __init__(self, scene, cell, lane):
        self.scene = scene
        self.grCar = IGraphicsCar(self)

        self.velocity = 0
        self.cell = cell
        self.lane = lane

        self.scene.addCar(self, cell, lane)
        self.scene.grScene.addItem(self.grCar)


    def move(self, x, y, cell):
        pass

    def printOut(self):
        return f"Car in cell: {self.cell}\n" \
               f"       Lane: {self.lane}\n" \
               f"   Velocity: {self.velocity}\n"


