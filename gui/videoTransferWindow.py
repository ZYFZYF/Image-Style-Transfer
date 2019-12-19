from video_transfer import Ui_VideoTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import os
from common import get_scaled_pixmap


class VideoTransferWindow(QMainWindow):
    def __init__(self):
        super(VideoTransferWindow, self).__init__()
        self.ui = Ui_VideoTransfer()
        self.ui.setupUi(self)
        self.ui.select_style.clicked.connect(self.select_style)

    def select_style(self):
        self.style_path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/style/',
                                                                   'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.ui.select_style.setText(os.path.split(self.style_path)[1])
            image = get_scaled_pixmap(self.style_path)
            self.ui.style_image.setPixmap(image)
