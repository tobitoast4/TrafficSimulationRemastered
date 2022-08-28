from graphics_car import IGraphicsCar

class Car():
    def __init__(self, scene, x, y):
        self.scene = scene
        self.grCar = IGraphicsCar(self)

        self.velocity = 0

        self.scene.addCar(self, x, y)
        self.scene.grScene.addItem(self.grCar)
