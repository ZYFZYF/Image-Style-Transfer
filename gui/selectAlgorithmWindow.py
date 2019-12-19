from select_algorithm import Ui_SelectAlgorithm
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.Qt import pyqtSignal


class SelectAlgorithmWindow(QMainWindow):
    select_algorithm = pyqtSignal(str)

    def __init__(self, image_transfer_window):
        super(SelectAlgorithmWindow, self).__init__()
        self.ui = Ui_SelectAlgorithm()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.close)
        self.ui.start.clicked.connect(self.start)
        self.select_algorithm.connect(image_transfer_window.transfer)
        self.parent = image_transfer_window

    def start(self):
        self.close()
        algorithm = None
        if self.ui.Gatys.isChecked():
            algorithm = 'Gatys'
        if self.ui.Chen.isChecked():
            algorithm = 'Chen'
        if self.ui.Johnson.isChecked():
            algorithm = 'Johnson'
        self.select_algorithm.emit(algorithm)
