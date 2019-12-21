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
        self.select_algorithm_window = SelectAlgorithmWindow(self)
        self.ui.select_content.clicked.connect(self.select_content)
        self.ui.select_style.clicked.connect(self.select_style)
        self.ui.select_algorithm.clicked.connect(self.select_algorithm_window.show)
        self.ui.start.clicked.connect(self.transfer)
        self.ui.content_image.setStyleSheet(image_border_style)
        self.ui.style_image.setStyleSheet(image_border_style)
        self.ui.transfer_image.setStyleSheet(image_border_style)

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

    def select_algorithm(self, algorithm):
        self.algorithm = algorithm
        self.ui.select_algorithm.setText(algorithm)

    def transfer(self):
        if not self.content_path or not self.style_path or not self.algorithm:
            box = QMessageBox(QMessageBox.Warning, '', '请先选择内容、风格和算法')
            box.addButton(self.tr("确定"), QMessageBox.YesRole)
            box.exec()
            return
        start_time = time.time()
        output_path = generate_temp_write_image_path()
        if self.algorithm == 'Gatys':
            Gatys.transfer.transfer(self.content_path, self.style_path, output_path)
        if self.algorithm == 'Chen':
            Chen.transfer.transfer(self.content_path, self.style_path, output_path)
        if self.algorithm == 'Johnson':
            Johnson.transfer.reload_model(get_model_name_from_style_path(self.style_path))
            Johnson.transfer.transfer(self.content_path, self.style_path, output_path)
        self.ui.transfer_image.setPixmap(get_scaled_pixmap(output_path))
        print(f'{self.algorithm}迁移耗时{int((time.time() - start_time) * 1000)}毫秒')

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()
