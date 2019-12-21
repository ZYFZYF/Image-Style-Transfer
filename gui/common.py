from PyQt5.QtGui import QPixmap, QImage
from PyQt5.Qt import QRect
from PIL import Image, ImageQt
from utils import *
import time
import numpy as np

image_border_style = 'border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);'


def get_scaled_pixmap(path):
    image = QImage(path)
    if not image.width():
        # 如果QImage打不开用PIL打开强转
        image = Image.open(path)
        image = image.convert("RGB")
        data = image.tobytes("raw", "RGB")
        image = QImage(data, image.size[0], image.size[1], QImage.Format_RGB888)
    width = image.width()
    height = image.height()
    # 窄的图片取上方，宽的图片取中间，保持和神经网络一样的剪切方式
    if width < height:
        rect = QRect(0, 0, width, width)
    else:
        rect = QRect(int(width / 2 - height / 2), 0, height, height)
    image = image.copy(rect)
    return QPixmap(image.scaled(256, 256))


def generate_temp_image_path():
    return 'frame.jpg'
    # return (TEMP_DIR + str(int(time.time() * 1000)) + '.jpg').replace('\\', '/')
