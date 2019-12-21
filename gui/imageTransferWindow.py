from image_transfer import Ui_ImageTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from selectAlgorithmWindow import SelectAlgorithmWindow
from PyQt5.QtGui import QPixmap
from common import *
import os
from utils import *
import time
import Gatys.transfer
import Chen.transfer
import Johnson.transfer


class ImageTransferWindow(QMainWindow):
    content_path = None
    style_path = None

    def __init__(self):
        super(ImageTransferWindow, self).__init__()
        self.ui = Ui_ImageTransfer()
        self.ui.setupUi(self)
        self.ui.select_content.clicked.connect(self.select_content)
        self.ui.select_style.clicked.connect(self.select_style)
        self.select_algorithm = SelectAlgorithmWindow(self)
        self.ui.transfer.clicked.connect(self.select_algorithm.show)

    def select_content(self):
        path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/content/',
                                                        'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.content_path = path
            self.ui.select_content.setText(os.path.split(self.content_path)[1])
            self.ui.content_image.setPixmap(get_scaled_pixmap(self.content_path))

    def select_style(self):
        path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/style/',
                                                        'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.style_path = path
            self.ui.select_style.setText(os.path.split(self.style_path)[1])
            self.ui.style_image.setPixmap(get_scaled_pixmap(self.style_path))

    def transfer(self, algorithm):
        if not self.content_path or not self.style_path:
            box = QMessageBox(QMessageBox.Warning, '', '请先选择内容和风格')
            box.addButton(self.tr("确定"), QMessageBox.YesRole)
            box.exec()
            return
        output_path = generate_temp_image_path()
        self.ui.transfer.setText(algorithm)
        if algorithm == 'Gatys':
            Gatys.transfer.transfer(self.content_path, self.style_path, output_path)
        if algorithm == 'Chen':
            Chen.transfer.transfer(self.content_path, self.style_path, output_path)
        if algorithm == 'Johnson':
            Johnson.transfer.reload_model(get_model_name_from_style_path(self.style_path))
            Johnson.transfer.transfer(self.content_path, self.style_path, output_path)
        self.ui.transfer_image.setPixmap(get_scaled_pixmap(output_path))
