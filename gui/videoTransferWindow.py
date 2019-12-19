from video_transfer import Ui_VideoTransfer
from PyQt5.QtWidgets import QMainWindow


class VideoTransferWindow(QMainWindow):
    def __init__(self):
        super(VideoTransferWindow, self).__init__()
        self.ui = Ui_VideoTransfer()
        self.ui.setupUi(self)
