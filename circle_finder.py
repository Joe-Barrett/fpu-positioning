import cv2
import math


class CircleFinder:

    def __init__(self, visual_mode=False):
        self.visual_mode = visual_mode

    def get_data(self, path):
        centres = {}
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        if self.visual_mode:
            cv2.imshow('', cv2.resize(thresh, (0, 0), fx=0.5, fy=0.5))
            cv2.waitKey(900)
        cnts = sorted(cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                      key=cv2.contourArea,
                      reverse=True)[:15]
        for i, c in enumerate(cnts):
            perimeter = cv2.arcLength(c, True)
            area = cv2.contourArea(c)
            if perimeter == 0:
                break
            circularity = 4 * math.pi * (area / (perimeter * perimeter))
            if 0.86 < circularity < 1.14:
                if i is 10 or i is 11:
                    circle = 'A'
                else:
                    circle = 'B'
                M = cv2.moments(c)
                cX = M["m10"] / M["m00"]
                cY = M["m01"] / M["m00"]
                centres[circle] = (cX, cY, circularity)
                if self.visual_mode:
                    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        print(centres)
        if self.visual_mode:
            cv2.imshow('', cv2.resize(image, (0, 0), fx=0.5, fy=0.5))
            cv2.waitKey(900)
        line_a = '{}, A, {}, {}, {}'.format(path.split('/')[-1],
                                            centres['A'][0],
                                            centres['A'][1],
                                            centres['A'][2])
        line_b = '{}, B, {}, {}, {}'.format(path.split('/')[-1],
                                            centres['B'][0],
                                            centres['B'][1],
                                            centres['B'][2])
        return '\n'.join([line_a, line_b])
