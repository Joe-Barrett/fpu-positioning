import os
from circle_finder import CircleFinder

_image_dir = 'Commissioning/Position test 1/'


def main():
    files = os.listdir(_image_dir)
    cf = CircleFinder()
    with open('output.csv', 'w') as csv:
        csv.write('file, circle, x, y\n')
        for file in files:
            csv.write(cf.get_data(_image_dir + file) + '\n')


if __name__ == '__main__':
    main()
