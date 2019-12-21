import cv2

from common import generate_temp_read_image_path

cap = None
input = None


def start_capture(source):
    global cap, input
    input = source
    if source == '摄像头':
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(source)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)


def get_next_frame():
    ret, frame = cap.read()
    path = generate_temp_read_image_path()
    if input == '摄像头':
        frame = frame[60:420, 140:500]
    cv2.imwrite(path, frame)
    return path


if __name__ == '__main__':
    start_capture('摄像头')
    get_next_frame()
    start_capture('../image/content/test.mp4')
    get_next_frame()
