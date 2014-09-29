#!/usr/bin/env python3

###############################################################################
# Crop image
###############################################################################

import sys
import os
from PIL import Image

CROPPED_AREA = (186, 9, 1735, 1170)


def main():
    if len(sys.argv) < 3:
        print("Syntax: {0:s} <Source Directory> <Destination Directory>".format(__file__))
        return 1
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    filelist = []
    for filename in os.listdir(src_dir):
        if filename.endswith(".png"):
            filelist.append(filename)

    if not os.path.exists(dst_dir):
        print("Make the destination directory: {0}".format(dst_dir))
        os.makedirs(dst_dir)

    for filename in sorted(filelist):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        if os.access(src_path, os.R_OK):
            print("Crop image {0} and save to {1}...".format(filename, dst_path), end='')
            image = Image.open(src_path)
            cropped_image = image.crop(CROPPED_AREA)
            if os.path.exists(dst_path):
                print("Overwriting...", end='')
            cropped_image.save(dst_path)
            print("Done")


if __name__ == "__main__":
    sys.exit(main())
