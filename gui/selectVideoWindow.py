from select_video import Ui_SelectVideo
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.Qt import pyqtSignal


class SelectVideoWindow(QMainWindow):
    select_video = pyqtSignal(str)

    def __init__(self, video_transfer_window):
        super(SelectVideoWindow, self).__init__()
        self.ui = Ui_SelectVideo()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.close)
        self.ui.select_camera.clicked.connect(self.select_camera)
        self.ui.select_file.clicked.connect(self.select_file)
        self.select_video.connect(video_transfer_window.select_video)

    def select_camera(self):
        self.select_video.emit('摄像头')
        self.close()

    def select_file(self):
        path, return_code = QFileDialog.getOpenFileName(self, '选择视频', '../image/content/',
                                                        'Image files(*.mp4 *.avi)')
        if return_code:
            self.select_video.emit(path)
            self.close()
