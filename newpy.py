#!/usr/bin/env python

import os
import sys
import shutil

TEMPLATE_DIR = "/home/gertjan/.newpy_templates/"

def list_targets():
    files = os.listdir(TEMPLATE_DIR)
    templates = {}
    for f in files:
        basefile = os.path.basename(f)
        target = os.path.splitext(basefile)[0]
        if os.path.isdir(f):
            basefile += '/'
        templates[target] = basefile
    return templates


def show_targets():
    templates = list_targets()
    print("Name\t  \tFile / Dir")
    print("----\t  \t----------")
    for target in sorted(templates.keys()):
        basefile = templates[target]
        print("%s\t->\t%s" % (target, basefile))
    print("")


def create_template(target, filename):
    templates = list_targets()
    thefile = os.path.join(TEMPLATE_DIR, templates[target])
    here = os.getcwd()
    if filename is None:
        shutil.copy(thefile, here)
    else:
        dest = os.path.join(here, filename)
        shutil.copy(thefile, dest)


def fail(target=None):
    if target is None:
        print("Usage: newpy target [filename]")
    else:
        print("Chosen target '%s' doesn't exist." % target)
    print("Available targets:")
    show_targets()
    raise SystemExit


def parse_args():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        fail()
    if len(sys.argv) == 2:
        target = sys.argv[1].strip().lower()
        filename = None
    else:
        target = sys.argv[1].strip().lower()
        filename = sys.argv[2].strip()
    if not target in list_targets():
        fail(target=target)
    return target, filename


def main():
    target, filename = parse_args()
    create_template(target, filename)


if __name__ == '__main__':
    main()
