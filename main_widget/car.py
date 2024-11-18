from main_widget.graphics_car import IGraphicsCar


class Car():
    def __init__(self, scene, cell):
        self.scene = scene
        self.grCar = IGraphicsCar(self)

        self.velocity = 0
        self.cell = cell


        self.scene.addCar(self, cell)
        self.scene.grScene.addItem(self.grCar)


    def move(self, x, y, cell):
        pass


    def printOut(self):
        return f"Car in cell: {self.cell}\n" \
               f"   Velocity: {self.velocity}\n" \
               f"   Cell pos: x: {self.scene.cell_positions[self.cell][0]}\n" \
               f"             y: {self.scene.cell_positions[self.cell][1]}"
