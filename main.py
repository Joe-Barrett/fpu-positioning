import os
from circle_finder import CircleFinder

_image_dir = 'Commissioning/Position test 1/'


def main():
    files = os.listdir(_image_dir)
    cf = CircleFinder()
    for file in files:
        cf.find_circles(_image_dir + file)


if __name__ == '__main__':
    main()
