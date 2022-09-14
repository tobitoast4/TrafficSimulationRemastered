import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, Qt, pyqtSignal

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())




