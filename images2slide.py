#!/usr/bin/env python3

import sys
import os
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

ALLOWED_EXTENSIONS = (".png", ".jpg", ".bmp", ".gif")


def main():
    if len(sys.argv) < 2:
        print("Syntax: {0} <Image Directory> <Output File>".format(__file__))
        return 1
    image_dir = sys.argv[1]
    output_file = sys.argv[2]
    if not output_file.endswith(".pdf"):
        output_file += ".pdf"

    file_list = []
    for filename in os.listdir(image_dir):
        if len(filename) >= 4 and filename[-4:] in ALLOWED_EXTENSIONS:
            file_list.append(os.path.join(image_dir, filename))

    print("Make a PDF slide at {0} from images in the following order:".format(output_file))
    pdf = canvas.Canvas(output_file, pageCompression=True)
    for i, filepath in enumerate(sorted(file_list)):
        print("[{2}/{1}] {0}".format(filepath,
                                     len(file_list),
                                     i+1))
        image = ImageReader(filepath)
        pdf.setPageSize(image.getSize())
        pdf.drawImage(image, 0, 0)
        pdf.showPage()
    pdf.save()


if __name__ == '__main__':
    sys.exit(main())
