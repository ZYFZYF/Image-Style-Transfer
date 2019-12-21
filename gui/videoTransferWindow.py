from video_transfer import Ui_VideoTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from selectVideoWindow import SelectVideoWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, QMutex, QMutexLocker
from PyQt5.Qt import pyqtSignal
import time
import os
from common import *
from cv import get_next_frame, start_capture
import Johnson.transfer


# from cv2 import VideoCapture


class VideoTransferWindow(QMainWindow):
    def __init__(self):
        super(VideoTransferWindow, self).__init__()
        self.ui = Ui_VideoTransfer()
        self.ui.setupUi(self)
        self.ui.select_style.clicked.connect(self.select_style)
        self.select_video_window = SelectVideoWindow(self)
        self.ui.select_video.clicked.connect(self.select_video_window.show)
        self.ui.transfer.clicked.connect(self.transfer_start)
        self.timer = Timer(self)
        self.ui.content_video.setStyleSheet(image_border_style)
        self.ui.style_image.setStyleSheet(image_border_style)
        self.ui.transfer_video.setStyleSheet(image_border_style)

        # self.device = VideoCapture(0)

    def select_style(self):
        path, return_code = QFileDialog.getOpenFileName(self, '选择图片', '../image/style/',
                                                        'Image files(*.jpg *.jpeg *.png)')
        if return_code:
            self.style_path = path
            self.ui.select_style.setText(os.path.split(self.style_path)[1])
            self.ui.style_image.setPixmap(get_scaled_pixmap(self.style_path))

    def select_video(self, content):
        self.content_path = content
        self.ui.select_video.setText(os.path.split(self.content_path)[1])
        print(content)

    def transfer_start(self):
        if not self.content_path or not self.style_path:
            box = QMessageBox(QMessageBox.Warning, '', '请先选择内容和风格')
            box.addButton(self.tr("确定"), QMessageBox.YesRole)
            box.exec()
            return
        print('start to transfer')
        start_capture(self.content_path)
        self.timer.start()

    def transfer_one_frame(self):
        start_time = time.time()
        # 从源里拿到一帧
        content_path = get_next_frame()
        output_path = generate_temp_image_path()
        # 风格迁移后输出到指定位置
        Johnson.transfer.reload_model(get_model_name_from_style_path(self.style_path))
        Johnson.transfer.transfer(content_path, self.style_path, output_path)
        # 然后显示到屏幕上
        self.ui.transfer_video.setPixmap(get_scaled_pixmap(output_path))
        print(f'迁移一帧耗费{int((time.time() - start_time) * 1000)}毫秒')


class Timer(QThread):
    time_to_render = pyqtSignal()

    def __init__(self, parent):
        super(Timer, self).__init__(parent)
        self.stop = False
        self.mutex = QMutex()
        self.time_to_render.connect(parent.transfer_one_frame)

    def run(self):
        with QMutexLocker(self.mutex):
            self.stop = False
        while True:
            if self.stop:
                return
            self.time_to_render.emit()
            # 40毫秒发送一次信号
            time.sleep(0.04)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stop = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stop
