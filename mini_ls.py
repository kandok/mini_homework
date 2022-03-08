#!/usr/bin/env python3
import os
import sys
import time


def get_info(path):
    stat_info = os.stat(path)
    print('Path Name: {}'.format(path))
    print('Owner:', stat_info.st_uid)
    print('Permissions:', oct(stat_info.st_mode))
    print('Last modified:', time.ctime(stat_info.st_mtime))


def convert(string):
    li = list(string.split(","))
    return li


def mini_ls():
    if sys.argv[1] == '-r':
        if len(sys.argv) == 2:
            paths = [os.getcwd()]
        else:
            paths = convert(sys.argv[2])
        for i in range(len(paths)):
            if os.path.isdir(paths[i]):
                for (root, dirs, files) in os.walk(paths[i], topdown=True):
                    get_info(root)
                    for j in range(len(files)):
                        get_info(root+'/'+files[j])

    elif len(sys.argv) == 2:
        if len(sys.argv) == 1:
            paths = [os.getcwd()]
        else:
            paths = convert(sys.argv[1])
        for i in range(len(paths)):
            get_info(paths[i])

    else:
        print('invalid input')


if __name__ == "__main__":
    mini_ls()
