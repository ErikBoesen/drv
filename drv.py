#!/usr/bin/env python3

from shutil import copy, move, copytree
import re
import argparse
import os

parser = argparse.ArgumentParser(description='Upload files to Google Drive.')
parser.add_argument('files', type=str, nargs='+',
                    help='files/folders to upload')
parser.add_argument('--cp', dest='cp', action='store_const',
                    const=True, default=False,
                    help='copy files to Drive rather than moving them.')

args = parser.parse_args()

for i in args.files:
    print('Uploading file %s... ' % (os.getcwd() + '/' + i), end='')
    src = os.getcwd() + '/' + i
    dst = os.path.expanduser('~') + '/Google Drive/' + i.split('/')[-1]
    if args.cp:
        if os.path.isdir(src):
            copytree(src, dst)
        else:
            copy(src, dst)
    else:
        move(src, dst)
    print('done!')

# TODO: Rewrite as map?
