#!/usr/bin/env python3

import os
import sys


if not len(sys.argv) == 2:
    err_text = '2 arguments are expected.\nExample: ext hello.jpg'
    sys.exit(err_text)


def main():
    file_path = sys.argv[1]
    ext = os.path.splitext(file_path)[1]
    if len(ext) > 0:
        text = 'File extension: {!s}'.format(ext)
    else:
        text = 'No file extension'
    print(text)
    sys.exit()


if __name__ == '__main__':
    main()
