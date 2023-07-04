#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.


import sys
import time
for num, i in enumerate(range(100)):
    sys.stdout.write("\r%d" % num)
    sys.stdout.flush()
    time.sleep(0.01)
