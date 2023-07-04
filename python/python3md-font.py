#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.

# Required:
#   pip install fonttools


from fontTools.ttLib import TTCollection
import os


ttc_path = './YuGothM.ttc'
output_dir = './ttf/'
os.makedirs(output_dir, exist_ok=True)


ttc = TTCollection(ttc_path)
for i, ttf in enumerate(ttc):
    output_path = output_dir + f'meiryo_{i}.ttf'
    ttf.save(output_path)
