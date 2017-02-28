#!/usr/bin/env python3

from shutil import copy, move
import re
import argparse
import os

parser = argparse.ArgumentParser(description='Upload files to Google Drive.')
parser.add_argument('files', metavar='N', type=str, nargs='+',
                    help='files/folders to upload')
parser.add_argument('--cp', dest='cp', action='store_const',
                    const=True, default=False,
                    help='copy files to Drive rather than moving them.')

args = parser.parse_args()

#clean_path = re.compile(r'^[~/]+')

for i in range(0, len(args.files)):
    print('Uploading file %s...' % (os.getcwd() + '/' + args.files[i]))
    if args.cp:
        copy(os.getcwd() + '/' + args.files[i], os.path.expanduser('~') + '/Google Drive')
    else:
        pass  # For now

# TODO: Rewrite as map
