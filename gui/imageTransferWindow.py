from image_transfer import Ui_ImageTransfer
from PyQt5.QtWidgets import QMainWindow


class ImageTransferWindow(QMainWindow):
    def __init__(self):
        super(ImageTransferWindow, self).__init__()
        self.ui = Ui_ImageTransfer()
        self.ui.setupUi(self)
