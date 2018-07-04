import argparse
import os
import sys
from circle_finder import CircleFinder

_image_dir = 'Commissioning/Position test 1/'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--directory',
                        action='store',
                        metavar='',
                        required=True,
                        help='The directory to read images from')
    parser.add_argument('-o',
                        '--output',
                        action='store',
                        metavar='',
                        required=False,
                        default='output.txt',
                        help='The filename for the output file, will save in provided image directory')
    parser.add_argument('-v',
                        '--visual',
                        action='store_true',
                        required=False,
                        help='Run in visual mode')
    args = parser.parse_args()
    if len(sys.argv) is 1:
        parser.print_help()
        sys.exit(0)
    if args.directory[-1] is not '/':
        args.directory = args.directory + '/'
    print(args.directory)
    cf = CircleFinder(visual_mode=args.visual)
    output_filepath = '/'.join([args.directory, args.output])
    print('Getting file list')
    files = [f for f in os.listdir(args.directory) if '.txt' not in f and 'edges' not in f]
    print('Running')
    with open(output_filepath, 'w') as csv:
        csv.write('file, circle, x, y, metric\n')
        for file in files:
            csv.write(cf.get_data(args.directory + file) + '\n')


if __name__ == '__main__':
    main()
