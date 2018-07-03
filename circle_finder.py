import cv2
import image_utils
import math


class CircleFinder:

    def __init__(self, visual_mode=False):
        self.visual_mode = visual_mode

    @staticmethod
    def _edge_detect(image):
        image = cv2.GaussianBlur(image, (5, 5), 0)
        image = cv2.Canny(image, 0, 150, apertureSize=3)
        return image

    @staticmethod
    def _find_contours(image):
        return sorted(cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                      key=cv2.contourArea,
                      reverse=True)[:2]

    # def _get_centres(self, contours):
    #     centres = {}
    #     for i, contour in enumerate(contours):
    #         M = cv2.moments(contour)
    #         circle = ''
    #         if i is 0:
    #             circle = 'A'
    #         else:
    #             circle = 'B'
    #         centre = (M['m10'] / M['m00'], M['m01'] / M['m00'])
    #         centres[circle] = centre
    #     return centres

    @staticmethod
    def _draw_contours(contours, image):
        for i, contour in enumerate(contours):
            M = cv2.moments(contour)
            contourX = int(M['m10'] / M['m00'])
            contourY = int(M['m01'] / M['m00'])
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
            cv2.circle(image, (contourX, contourY), 7, (255, 255, 255), -1)
        return image

    def _get_centres(self, contours, image):
        centres = {}
        for i, contour in enumerate(contours):
            if i is 0:
                circle = 'A'
            else:
                circle = 'B'
            (x, y), radius = cv2.minEnclosingCircle(contour)
            area = (4 * 3.141592 * cv2.contourArea(contour)) / math.pow(cv2.arcLength(contour, 1), 2)  # SW addition
            centres[circle] = (x, y, area)
            center = (int(x), int(y))
            radius = int(radius)

            if self.visual_mode:
                cv2.circle(image, center, radius, (0, 255, 0), 2)
                cv2.circle(image, center, 7, (255, 255, 255), -1)
        if self.visual_mode:
            image_utils.show_image(image, delay=500)
        return centres

    def get_data(self, path):
        image = image_utils.load_image(path)
        edged = self._edge_detect(image)
        contours = self._find_contours(edged)
        centres = self._get_centres(contours, image)
        line_a = '{}, A, {}, {}, {}'.format(path.split('/')[-1],
                                            centres['A'][0],
                                            centres['A'][1],
                                            centres['A'][2])  # SW modification
        line_b = '{}, B, {}, {}, {}'.format(path.split('/')[-1],
                                            centres['B'][0],
                                            centres['B'][1],
                                            centres['B'][2])  # SW modification
        return '\n'.join([line_a, line_b])

    def find_circles(self, path):
        image = image_utils.load_image(path)
        edged = self._edge_detect(image)
        contours = self._find_contours(edged)
        # self._draw_bounding_circle(contours, image)
        # drawn = self._draw_contours(contours, image)
        # image_utils.show_image(drawn)
