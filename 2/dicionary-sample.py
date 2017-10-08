#! /usr/bin/env python

from __future__ import print_function
import argparse
import os


def get_dictionary_list(dct_filename):
    dct_filename = os.path.realpath(dct_filename)
    if not dct_filename:
        return False
    else:
        with open(dct_filename) as f:
            dct = f.readlines()
        return dct


def count_words(dct, prefix):
    num = 0
    for i in dct:
        if i.startswith(prefix):
            num += 1
    return num


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-D',
                        '--dictionary_file',
                        help='Linux dictionary file. Default: %(default)s',
                        default='/usr/share/dict/american-english')
    parser.add_argument('-p',
                        '--prefix',
                        help='The word prefix to count. Default=%(default)s',
                        default='tim')
    args = parser.parse_args()
    dct_list = get_dictionary_list(args.dictionary_file)
    prefix_count = count_words(dct_list, args.prefix)
    print('{prefix} {num}'.format(prefix=args.prefix, num=prefix_count))

if __name__ == '__main__':
    main()

