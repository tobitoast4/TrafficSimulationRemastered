import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, Qt, pyqtSignal

from editor_wnd import NodeEditorWnd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorWnd()

    sys.exit(app.exec_())




