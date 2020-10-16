#!/usr/bin/env python3
"""
Quick script to build a gif
"""

import argparse
import glob
import os

import imageio
from pygifsicle import optimize

def main():
    parser = argparse.ArgumentParser(
        description='Script to build a gif from images')
    parser.add_argument('-i', '--img_dir', help="input file directory")
    parser.add_argument('-v', '--vid', help="input video file")
    parser.add_argument( '-o', '--out', help="output gif filename")
    args = parser.parse_args()

    out = "output.gif"
    if args.out:
        out = args.out

    if args.img_dir:
        dirname = args.file_dir

        files = glob.glob(os.path.join(dirname, '*.jpg'))
        files = sorted(files)

        with imageio.get_writer(out) as writer:
            for filename in files:
                writer.append_data(imageio.imread(filename))

    if args.vid:
        with imageio.get_writer(out) as writer:
            with imageio.get_reader(args.vid) as reader:
                for idx, img in enumerate(reader):
                    writer.append_data(img)

    optimize(out)


if __name__ == '__main__':
    main()
