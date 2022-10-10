#!/usr/bin/python3
# -*- coding: utf-8 -*-

import main
import pytest

def test_main():
    assert "{:.2f}".format(main.three()) == "3.00", "小数点以下2桁までを比較"
    assert not main.three() == 4, "4ではない"
