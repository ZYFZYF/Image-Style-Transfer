from start import Ui_StartWindow
from PyQt5.QtWidgets import QMainWindow


class StartWindow(QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
