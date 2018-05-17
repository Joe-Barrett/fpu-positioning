import cv2


def show_image(image=None, path='', delay=0):
    if image is None and path is not '':
        image = cv2.imread(path)
    if image is not None:
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('', image)
    cv2.waitKey(delay)


def load_image(path=''):
    return cv2.imread(path)
