import cv2
import image_utils


class CircleFinder:

    def test(self):
        image_utils.show_image(path='./Commissioning/Position test 1/a000b140.bmp')
        print('Hello from CircleFinder')

    def _edge_detect(self, image):
        image = cv2.Canny(image, 190, 200, apertureSize=3)
        return image

    def _hough_circles(self, image):
        return cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 2.5, 100)

    def _draw_hough_circles(self, circles, image):
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
        return image

    def _find_contours(self, image):
        return sorted(cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                      key=cv2.contourArea,
                      reverse=True)[:2]

    def _draw_contours(self, contours, image):
        return cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    def find_circles(self, path):
        image = image_utils.load_image(path)
        edged = self._edge_detect(image)
        contours = self._find_contours(edged.copy())
        drawn = self._draw_contours(contours, image)
        image_utils.show_image(drawn)
        # circles = self._hough_circles(edged)
        # circled_image = self._draw_hough_circles(circles, image)
        # image_utils.show_image(image=circled_image, delay=20)
