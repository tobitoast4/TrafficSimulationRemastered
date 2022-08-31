from graphics_scene import *
from car import Car
import utils
import random


class Scene():
    def __init__(self, parent=None):
        self.parent = parent
        self.scene_width = 5000
        self.scene_height = 5000

        self.radius = 900
        self.radius_gap = 25
        self.amount_cells = 240
        self.amount_cars = 80
        # self.cells_random = utils.get_random_array(self.amount_cells)
        self.cells_random = utils.equal(self.amount_cells, self.amount_cars)
        self.v_max = 5
        self.amount_lanes = 1
        self.color_array = utils.get_new_color_array(self.v_max)

        self.cell_positions = []
        self.cells = self.getEmtpyCellMatrix() # contains a car or is empty
        self.cars = []  # contains all cars of the scene


        self.initUi()
        self.initCells()
        self.addCars()

    def initUi(self):
        self.grScene = IGraphicsScene(self, self.radius, self.radius_gap, self.amount_cells)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def initCells(self):
        for l in range(self.amount_lanes):
            self.cell_positions.append(list())
            radius = self.radius + round((l+0.5) * self.radius_gap)
            distance = 2 * math.pi / self.amount_cells
            for k in range(self.amount_cells):
                x = round(radius * math.cos((k + 0.5) * distance))
                y = round(radius * math.sin((k + 0.5) * distance))
                self.cell_positions[l].append([x, y])
        print(self.cell_positions)

    def addCars(self):
        total_cells = self.amount_cells * self.amount_lanes
        for c in range(0, self.amount_cars):
            value = round(c * (total_cells/self.amount_cars))
            lane = math.floor(value/self.amount_cells)
            cell = value % self.amount_cells
            Car(self, cell, lane)

    def addCar(self, car, cell, lane):
        self.cars.append(car)
        self.grScene.addItem(car.grCar)
        x, y = self.cell_positions[lane][cell]
        car.grCar.setPos(x, y)
        self.cells[lane][cell] = car
        car.cell = cell

    def removeCar(self, car):
        self.cars.remove(car)

    def addCarRandom(self):
        cell_where_car_will_be_added = self.cells_random[len(self.cars)]
        Car(self, cell_where_car_will_be_added, 0)

    def getEmtpyCellMatrix(self):
        return [[None for c in range(self.amount_cells)] for l in range(self.amount_lanes)]

    def moveCars(self, paused):
        new_cells = self.getEmtpyCellMatrix()
        amount_selected = 0
        velocity_sum = 0
        first_cell = -1

        # if not paused:
        #     self.printselfLanes()
        #     for car1 in self.cars:
        #         for car2 in self.cars:
        #             if car1 is not car2:
        #                 if car1.grCar.pos() == car2.grCar.pos():
        #                     print(f"L{car1.lane}C{car1.cell}")
        #                     # raise Exception("asdf")

        for car in self.cars:
            if car.grCar.isSelected():
                amount_selected += 1
                velocity_sum += car.velocity
                if car.cell > first_cell:
                    first_cell = car.cell

            if not paused:
                desired_velocity = car.velocity
                if desired_velocity < self.v_max:                                                                   # rule 1
                    desired_velocity += 1
                current_cell = car.cell

                amount_free_cells_at_lane = [desired_velocity for l in range(self.amount_lanes)]                    # rule 2
                for l in range(self.amount_lanes):
                    for c in range(desired_velocity):
                        next_cell = current_cell + c + 1
                        if next_cell >= self.amount_cells:
                            next_cell -= self.amount_cells
                        if self.cells[l][next_cell] is not None:
                            amount_free_cells_at_lane[l] = c
                            break

                car.velocity = desired_velocity                                                                     # part of rule 1
                if desired_velocity > amount_free_cells_at_lane[car.lane] and car.lane < self.amount_lanes-1: # lane switch to left
                    if random.randrange(0, 2) == 0 and self.checkIfLeftLaneIsFree(car.lane, car.cell):  # chance of 50%
                        car.lane += 1
                        car.velocity = car.lane
                else: # lane switch to right
                    if car.lane > 0 and self.checkIfRightLaneIsFree(car.lane, car.cell):
                        car.lane -= 1
                        car.velocity = car.lane

                for l in range(car.lane, self.amount_lanes): # rechts darf nicht überholt werden
                    if amount_free_cells_at_lane[l] < car.velocity:
                        car.velocity = amount_free_cells_at_lane[l]

                rand_int = random.randrange(1, 100)                                                                  # rule 3
                #(0 -> inclusive, 99 -> exlusive)
                if rand_int < 30 and car.velocity > 0:
                    car.velocity -= 1

                new_cell = current_cell + car.velocity                                                                   # rule 4
                if new_cell >= self.amount_cells:
                    new_cell -= self.amount_cells
                x, y = self.cell_positions[car.lane][new_cell]
                car.grCar.setPos(x, y)
                car.cell = new_cell
                car.grCar.updateBrush(self.color_array)
                new_cells[car.lane][new_cell] = car
        if not paused:
            self.cells = new_cells
        self.parent.update_selected(amount_selected, velocity_sum, first_cell)

    def checkIfLeftLaneIsFree(self, current_lane, current_cell):
        for c in range(self.v_max+1):
            previous_cell = current_cell - c
            if previous_cell < 0:
                previous_cell + self.amount_cells
            if self.cells[current_lane+1][previous_cell] is not None:
                velocity_of_other_car = self.cells[current_lane+1][previous_cell].velocity
                if velocity_of_other_car >= c:
                    return False
        return True

    def checkIfRightLaneIsFree(self, current_lane, current_cell):
        for c in range(self.v_max+1):
            previous_cell = current_cell - c
            if previous_cell < 0:
                previous_cell + self.amount_cells
            if self.cells[current_lane-1][previous_cell] is not None:
                velocity_of_other_car = self.cells[current_lane-1][previous_cell].velocity
                if velocity_of_other_car >= c:
                    return False
        return True


    def printselfLanes(self):
        new_multi_arr = []
        for l in range(len(self.cells)):
            new_lane_l = self.cells[l].copy()
            for c in range(len(new_lane_l)):
                if new_lane_l[c] is None:
                    new_lane_l[c] = " "
                if isinstance(new_lane_l[c], Car):
                    new_lane_l[c] = str(new_lane_l[c].velocity)
            new_multi_arr.append(new_lane_l)
        print("--------------------------------------------------------")
        lane_nr = self.amount_lanes
        for lane in reversed(new_multi_arr):
            lane_nr -= 1
            print(f"{lane_nr} {lane}")


