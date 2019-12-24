import cv2

from common import generate_temp_read_image_path
from PIL import Image
import time
import numpy as np

cap = None
input = None
width = None
height = None


def start_capture(source):
    global cap, input
    input = source
    if source == '摄像头':
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(source)
    global width, height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)
    return cap.get(7)


def get_next_frame():
    ret, frame = cap.read()
    if input == '摄像头':
        frame = frame[60:420, 140:500]
    else:
        pass
    frame = frame[..., ::-1]
    image = Image.fromarray(frame)
    return image


if __name__ == '__main__':
    start_capture('摄像头')
    get_next_frame()
    start_capture('../image/content/test.mp4')
    get_next_frame()
