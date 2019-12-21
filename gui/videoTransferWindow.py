from video_transfer import Ui_VideoTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from selectVideoWindow import SelectVideoWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, QMutex, QMutexLocker
from PyQt5.Qt import pyqtSignal
import time
import os
from common import *


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
        print('start to transfer')
        self.timer.start()

    def transfer_one_frame(self):
        start_time = time.time()
        ret, frame = self.device.read()

        # 读写磁盘方式
        # cv2.imwrite("2.png", frame)
        # self.image.load("2.png")

        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        # 变换彩色空间顺序
        # cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        # 转为QImage对象
        self.image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.view.setPixmap(QPixmap.fromImage(self.image))
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
