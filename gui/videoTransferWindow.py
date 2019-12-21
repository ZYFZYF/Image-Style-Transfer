from video_transfer import Ui_VideoTransfer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from selectVideoWindow import SelectVideoWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QMutex, QMutexLocker
from PyQt5.Qt import pyqtSignal
import time
import os
from common import get_scaled_pixmap


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
        print('need to transfer one frame')
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
