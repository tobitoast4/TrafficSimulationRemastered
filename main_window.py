from datetime import datetime

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from main_widget.main_widget import *
from main_diagram_widget.main_diagram_widget import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self)  # Load the .ui file

        self.diagram_widget = self.findChild(QWidget, "main_diagram_widget")
        self.main_diagram_widget = MainDiagramWidget(4, parent=self)
        self.frame_main_widget_layout = QVBoxLayout()
        self.frame_main_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_widget_layout.addWidget(self.main_diagram_widget)
        self.diagram_widget.setLayout(self.frame_main_widget_layout)
        self.right_frame = self.findChild(QWidget, "frame_5")
        self.right_frame.setMaximumWidth(592)
        self.splitter_right = self.findChild(QWidget, "splitter_right")
        self.splitter_right.setSizes([1, 2])


        self.widget = self.findChild(QWidget, "widget")
        self.main_widget = NodeEditorWnd(0.000008*(100000-85000), self.main_diagram_widget, parent=self)
        self.frame_main_widget_layout = QVBoxLayout()
        self.frame_main_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_widget_layout.addWidget(self.main_widget)
        self.widget.setLayout(self.frame_main_widget_layout)

        self.pushButton = self.findChild(QAction, "actionShow_Diagramm_1")
        self.pushButton.triggered.connect(self.show_main_diagram)



        self.slider_velocity_changed = self.findChild(QSlider, "velocitySlider")
        self.slider_velocity_changed.valueChanged.connect(self.velocity_changed)

        self.button_pause = self.findChild(QPushButton, "pauseButton")
        pixmapi = getattr(QStyle, "SP_MediaPause")
        icon = self.style().standardIcon(pixmapi)
        self.button_pause.setIcon(icon)
        self.button_pause.clicked.connect(self.pause)

        self.runningTime = self.findChild(QLCDNumber, "runtimeLcd")
        self.milliseconds_since_start = 0
        self.main_bg_thread = TimerThread()
        self.main_bg_thread.update.connect(self.update_timer)
        self.main_bg_thread.start()

        self.label_amount = self.findChild(QLabel, "label_amount")
        self.label_velocity = self.findChild(QLabel, "label_velocity")
        self.label_cell = self.findChild(QLabel, "label_cell")


    def show_main_diagram(self):
        self.splitter_right.setSizes([1, 2])


    def pause(self):
        if self.main_widget.main_bg_thread.paused:
            pixmapi = getattr(QStyle, "SP_MediaPause")
            icon = self.style().standardIcon(pixmapi)
            self.button_pause.setIcon(icon)
            self.main_widget.main_bg_thread.paused = False
        else:
            pixmapi = getattr(QStyle, "SP_MediaPlay")
            icon = self.style().standardIcon(pixmapi)
            self.button_pause.setIcon(icon)
            self.main_widget.main_bg_thread.paused = True

    def velocity_changed(self):  # Inside the class
        value = self.slider_velocity_changed.value()
        self.main_widget.main_bg_thread.time_wait = 0.000008*(100000-value)

    def update_timer(self):
        self.milliseconds_since_start += 1
        time = datetime.fromtimestamp(self.milliseconds_since_start / 10)
        self.runningTime.display(f"{str(time.hour-1).zfill(2)}:{str(time.minute).zfill(2)}:"
                                 f"{str(time.second).zfill(2)}.{int(time.microsecond/100000)}")

    def update_selected(self, amount, v_sum, first_cell):
        self.label_amount.setText(f"{amount}")
        if amount > 0:
            self.label_velocity.setText(f"{round(v_sum/amount, 3)}")
            self.label_cell.setText(f"{first_cell}")
        else:
            self.label_velocity.setText("-")
            self.label_cell.setText("-")


class TimerThread(QThread): # see https://stackoverflow.com/a/44329475/14522363
    update = pyqtSignal()

    def __init__(self):

        super().__init__()

    def run(self):
        while True:
            self.update.emit()
            time.sleep(0.1)