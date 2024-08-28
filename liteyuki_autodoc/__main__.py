# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/28 下午4:08
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : __main__.py
@Software: PyCharm
"""
# command line tool
# args[0] path
# -o|--output output path
# -l|--lang zh-Hans en jp default zh-Hans


import argparse
import os
import sys

from liteyuki_autodoc.output import generate_from_module


def main():
    parser = argparse.ArgumentParser(description="Generate documentation from Python modules.")
    parser.add_argument("path", type=str, help="Path to the Python module or package.")
    parser.add_argument("-o", "--output", default="doc-output", type=str, help="Output directory.")
    parser.add_argument("-c", "--contain-top", action="store_true", help="Whether to contain top-level dir in output dir.")
    parser.add_argument("-l", "--lang", nargs='+', default=["zh-Hans"], type=str, help="Languages of the document.")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: The path {args.path} does not exist.")
        sys.exit(1)

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    langs = args.lang
    for lang in langs:
        generate_from_module(args.path, args.output, with_top=args.contain_top, lang=lang)


if __name__ == '__main__':
    main()