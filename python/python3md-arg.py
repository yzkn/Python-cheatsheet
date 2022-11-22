#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


import sys

args = sys.argv
print(args)

for i, arg in enumerate(args):
    print('第{}引数: {}'.format(i, args[i]))