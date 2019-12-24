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
from tqdm import tqdm


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
        self.transfer = Transfer(self)
        self.ui.content_video.setStyleSheet(image_border_style)
        self.ui.style_image.setStyleSheet(image_border_style)
        self.ui.transfer_video.setStyleSheet(image_border_style)
        self.ui.stop.clicked.connect(self.transfer_stop)
        self.content_path = None
        self.style_path = None

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
        if not self.transfer.isStopped():
            return
        self.transfer_frames = 0
        self.transfer_start_time = time.time()

        if not self.content_path or not self.style_path:
            box = QMessageBox(QMessageBox.Warning, '', '请先选择内容和风格')
            box.addButton(self.tr("确定"), QMessageBox.YesRole)
            box.exec()
            return
        print('start to transfer')
        Johnson.transfer.reload_model(get_model_name_from_style_path(self.style_path))
        self.total_transfer_frames = int(start_capture(self.content_path))
        if self.total_transfer_frames == 0:
            self.total_transfer_frames = '∞'
        self.transfer.start()

    def transfer_stop(self):
        self.transfer_frames = 0
        self.ui.transfer.setText(f'开始迁移')
        self.transfer.stop()

    def closeEvent(self, event):
        self.transfer_stop()
        event.accept()


class Transfer(QThread):

    def __init__(self, parent):
        super(Transfer, self).__init__(parent)
        self.stopped = True
        self.mutex = QMutex()
        self.parent = parent

    def run(self):
        with QMutexLocker(self.mutex):
            self.stopped = False
        start_time = time.time()
        for i in tqdm(range(self.parent.total_transfer_frames if self.parent.total_transfer_frames != '∞' else 100000)):
            if self.stopped:
                self.parent.ui.transfer.setText(f'开始迁移')
                return
            # 从源里拿到一帧
            content_image = get_next_frame()
            self.parent.ui.content_video.setPixmap(get_scaled_pixmap(content_image))
            # 风格迁移后输出到指定位置
            target_image = Johnson.transfer.transfer(content_image, self.parent.style_path)
            # 然后显示到屏幕上
            self.parent.ui.transfer_video.setPixmap(get_scaled_pixmap(target_image))
            self.parent.ui.transfer.setText(f'{i}/{self.parent.total_transfer_frames}')
            print(f'已迁移{i + 1}帧，耗费{time.time() - start_time}秒,平均每帧耗时{(time.time() - start_time) / (i + 1)}秒')
        self.parent.ui.transfer.setText(f'已完成')

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    def isStopped(self):
        with QMutexLocker(self.mutex):
            return self.stopped
