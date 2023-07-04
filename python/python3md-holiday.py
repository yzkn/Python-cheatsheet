#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.

# Required:
#   pip install requests


import requests
import sys


url = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'


def get_holidays(date_label):
    response = requests.get(url)
    print('response.status_code', response.status_code)
    if response.status_code == 200:
        response.encoding = 'Shift_JIS'
        holidays = response.text.splitlines()

        # ヘッダ行削除
        holidays.pop(0)

        # 前方一致でフィルタリング
        if date_label != '':
            holidays = list(filter(lambda x: x.startswith(date_label), holidays))

        return [item.split(',') for item in holidays]


if __name__ == "__main__":
    date_label = ''
    if len(sys.argv) == 2:
        date_label = sys.argv[1]

    result = get_holidays(date_label)
    print(result)
