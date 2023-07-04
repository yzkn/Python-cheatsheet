#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.


import codecs
import os

def detect_encode(filepath):
    cs = [
        'utf-8',
        'utf_8_sig',
        'euc_jp',
        'cp932',
        #
        'euc_jis_2004',
        'euc_jisx0213',
        'iso2022_jp_1',
        'iso2022_jp_2',
        'iso2022_jp_3',
        'iso2022_jp_2004',
        'iso2022_jp_ext',
        'iso2022_jp',
        'shift_jis_2004',
        'shift_jis',
        'shift_jisx0213',
        'utf_7',
        'utf_16_be',
        'utf_16_le',
        'utf_16',
    ]

    for c in cs:
        try:
            with codecs.open(filepath, 'r', c, errors='strict') as f:
                print(f.read())
                return c
        except Exception as e:
            continue
    return None

c = detect_encode(os.path.join('test-fileio', 'inputsjis.txt'))
print(c)
