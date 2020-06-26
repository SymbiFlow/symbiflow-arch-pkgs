#!/usr/bin/python

import argparse
import json
import os
import os.path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--elements', '-e',
                    nargs='*', default=os.listdir(os.curdir),
                    help='generate list from the specifiec elements')

args = parser.parse_args()

print(json.dumps([
    node for node in args.elements
    if os.path.isdir(node) and 'PKGBUILD' in os.listdir(node)
]))
