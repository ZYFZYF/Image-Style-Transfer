import cv2

# from common import generate_temp_image_path

cap = None


def start_capture(source):
    global cap
    if source == '摄像头':
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(source)


def get_next_frame():
    ret, frame = cap.read()
    path = 'test.jpg'  # generate_temp_image_path()
    cv2.imwrite(path, frame)
    return path


if __name__ == '__main__':
    start_capture('摄像头')
    get_next_frame()
    start_capture('../image/content/test.mp4')
    get_next_frame()
