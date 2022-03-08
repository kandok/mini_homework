#!/usr/bin/env python3
import re
import sys


def convert(string):
    li = list(string.split(","))
    return li


def mini_grep():
    if sys.argv[1] == '-q':
        p = 3
        f = 4
    else:
        p = 2
        f = 3
    # this doesn't really work but theoretically
    try:
        pattern = re.compile(sys.argv[p])
    except re.error:
        print('Invalid regex')
    try:
        files = convert(sys.argv[f])
    except IndexError:
        user_input = sys.stdin.readline().split("\n")[0]
        files = convert(user_input)

    for i in range(len(files)):
        try:
            with open(files[i], "r") as file:
                line_no = 0
                for line in file:
                    line_no += 1
                    if re.search(pattern, line):
                        if sys.argv[1] == '-q':
                            print(line)
                        else:
                            print(line_no, line)
        except FileNotFoundError:
            print('Invalid file path.')


if __name__ == "__main__":
    mini_grep()
