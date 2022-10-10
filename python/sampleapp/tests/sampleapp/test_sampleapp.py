#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sampleapp.sampleapp
import pytest

def test_hello_world():
    assert sampleapp.sampleapp.hello_world() == 'Hello, world!!', '返り値が一致'
