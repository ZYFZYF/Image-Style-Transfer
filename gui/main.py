# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from startWindow import StartWindow
from imageTransferWindow import ImageTransferWindow
from videoTransferWindow import VideoTransferWindow

if __name__ == "__main__":
    app = QApplication([])
    # 开始界面
    startWindow = StartWindow()
    # 图像风格迁移界面
    imageTransferWindow = ImageTransferWindow()
    # 视频风格迁移界面
    videoTransferWindow = VideoTransferWindow()
    # 设置多个window之间的切换关系
    startWindow.ui.select_image.clicked.connect(lambda: (imageTransferWindow.show(), startWindow.close()))
    startWindow.ui.select_video.clicked.connect(lambda: (videoTransferWindow.show(), startWindow.close()))
    imageTransferWindow.ui.cancel.clicked.connect(lambda: (startWindow.show(), imageTransferWindow.close()))
    videoTransferWindow.ui.cancel.clicked.connect(lambda: (startWindow.show(), videoTransferWindow.close()))
    # 先显示第一个
    startWindow.show()
    sys.exit(app.exec_())
