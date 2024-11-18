from main_diagram_widget.graphics_scene import *


class Scene():
    def __init__(self, parent=None):
        self.parent = parent
        self.scene_width = 3000
        self.scene_height = 5000

        self.initUi()


    def initUi(self):
        self.grScene = IGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width, self.scene_height)


