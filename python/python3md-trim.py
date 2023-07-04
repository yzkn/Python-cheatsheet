#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.

# $ py .\python\python3md-trim.py python/img


import cv2
import os
import sys


out_path = 'result'

def main():
    args = sys.argv
    data_dir = args[1]
    out_dir = os.path.join(data_dir, out_path).replace('\\', '/')
    os.mkdir(out_dir)
    files = [f for f in os.listdir(data_dir) if '.jpeg' in f or '.jpg' in f or '.png' in f]
    for file in files:
        img = cv2.imread(os.path.join(data_dir, file).replace('\\', '/'))
        selected = cv2.selectROI(img)
        if sum(selected):
            img2 = img[
                int(selected[1]):int(selected[1]+selected[3]),
                int(selected[0]):int(selected[0]+selected[2])
            ]
            cv2.imwrite(os.path.join(out_dir, file).replace('\\', '/'), img2)
            print('.', end='')

if __name__ == '__main__':
    main()
