from __future__ import print_function

import argparse
import sys
import re

BLACKLIST = [
    r'AKIA',
]


def detect_blacklisted(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    problems = []

    for filename in args.filenames:
        with open(filename, 'r') as f:
            content = f.read()
            for regex in BLACKLIST:
                if re.search(regex, content):
                    problems.append('Match for ' + regex + " found in " + filename)

    if problems:
        for problem in problems:
            print(problem)
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(detect_blacklisted())
