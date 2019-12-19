from image_transfer import Ui_ImageTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from common import *
import os


class ImageTransferWindow(QMainWindow):
    content_path = None
    style_path = None

    def __init__(self):
        super(ImageTransferWindow, self).__init__()
        self.ui = Ui_ImageTransfer()
        self.ui.setupUi(self)
        self.ui.select_content.clicked.connect(self.select_content)
        self.ui.select_style.clicked.connect(self.select_style)

    def select_content(self):
        self.content_path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/content/',
                                                                     'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.ui.select_content.setText(os.path.split(self.content_path)[1])
            image = get_scaled_pixmap(self.content_path)
            self.ui.content_image.setPixmap(image)

    def select_style(self):
        self.style_path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/style/',
                                                                   'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.ui.select_style.setText(os.path.split(self.style_path)[1])
            image = get_scaled_pixmap(self.style_path)
            self.ui.style_image.setPixmap(image)
