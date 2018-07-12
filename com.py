import cv2
import os
import math

_image_dir = './PT01_datum_repeatability_02/'


def main():
    files = [f for f in os.listdir(_image_dir) if '.txt' not in f and 'edges' not in f]
    for file in files:
        image = cv2.imread(_image_dir+file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('', cv2.resize(thresh, (0, 0), fx=0.5, fy=0.5))
        cv2.waitKey(900)
        cnts = sorted(cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                      key=cv2.contourArea,
                      reverse=True)[:15]
        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            area = cv2.contourArea(c)
            if perimeter == 0:
                break
            circularity = 4*math.pi*(area/(perimeter*perimeter))
            if 0.86 < circularity < 1.14:
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.imshow('', cv2.resize(image, (0, 0), fx=0.5, fy=0.5))
        cv2.waitKey(900)


if __name__ == '__main__':
    main()
