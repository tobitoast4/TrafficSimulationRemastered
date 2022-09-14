from TrafficSimulationRemastered.main_widget.graphics_scene import *
from TrafficSimulationRemastered.main_widget.car import Car
from TrafficSimulationRemastered import utils
import random


class Scene():
    def __init__(self, parent=None):
        self.parent = parent
        self.scene_width = 5000
        self.scene_height = 5000

        self.radius = 900
        self.radius_gap = 25
        self.amount_cells = 340
        self.amount_cars = 80
        # self.cells_random = utils.get_random_array(self.amount_cells)
        self.cells_random = utils.equal(self.amount_cells, self.amount_cars)
        self.v_max = 3
        self.color_array = utils.get_new_color_array(self.v_max)
        if self.amount_cars > self.amount_cells:
            raise Exception("There can't be more cars then cells")

        self.cell_positions = []
        self.cells = [None for c in range(self.amount_cells)] # contains a car or is empty
        self.cars = []  # contains all cars of the scene


        self.initUi()
        self.initCells()
        self.addCars()

    def initUi(self):
        self.grScene = IGraphicsScene(self, self.radius, self.radius_gap, self.amount_cells)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def initCells(self):
        radius = self.radius + (self.radius_gap // 2)
        distance = 2 * math.pi / self.amount_cells
        for k in range(self.amount_cells):
            x = round(radius * math.cos((k + 0.5) * distance))
            y = round(radius * math.sin((k + 0.5) * distance))
            self.cell_positions.append([x, y])

    def addCars(self):
        for c in range(self.amount_cars):
            self.addCarRandom()

    def addCar(self, car, cell):
        self.cars.append(car)
        self.grScene.addItem(car.grCar)

        x, y = self.cell_positions[cell]
        car.grCar.setPos(x, y)
        self.cells[cell] = car
        car.cell = cell

    def removeCar(self, car):
        self.cars.remove(car)

    def addCarRandom(self):
        cell_where_car_will_be_added = self.cells_random[len(self.cars)]
        Car(self, cell_where_car_will_be_added)

    def moveCars(self, paused):
        new_cells = [None for c in range(self.amount_cells)]
        amount_selected = 0
        velocity_sum = 0
        first_cell = -1
        for car in self.cars:
            if car.grCar.isSelected():
                amount_selected += 1
                velocity_sum += car.velocity
                if car.cell > first_cell:
                    first_cell = car.cell

            if not paused:
                if car.velocity < self.v_max:               # rule 1
                    car.velocity += 1
                current_cell = car.cell

                for c in range(car.velocity):               # rule 2
                    next_cell = current_cell + c + 1
                    if next_cell >= self.amount_cells:
                        next_cell -= self.amount_cells
                    if self.cells[next_cell] is not None:
                        car.velocity = c
                        break

                rand_int = random.randrange(1, 100)         # rule 3
                #(0 -> inclusive, 99 -> exlusive)
                if rand_int < 30 and car.velocity > 0:
                    car.velocity -= 1

                new_cell = car.cell + car.velocity          # rule 4
                if new_cell >= self.amount_cells:
                    new_cell -= self.amount_cells
                x, y = self.cell_positions[new_cell]
                car.grCar.setPos(x, y)
                car.cell = new_cell
                car.grCar.updateBrush(self.color_array)
                new_cells[new_cell] = car
        if not paused:
            self.cells = new_cells
            self.parent.main_diagram_widget.drawLine(self.cells)
        self.parent.update_selected(amount_selected, velocity_sum, first_cell)

    def replacedArr(self, arr):
        new_arr = arr.copy()
        for c in range(len(new_arr)):
            if new_arr[c] is None:
                new_arr[c] = "x"
            if isinstance(new_arr[c], Car):
                new_arr[c] = new_arr[c].velocity
        return new_arr


