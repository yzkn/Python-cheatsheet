#!/usr/bin/python3
# -*- coding: utf-8 -*-

import params
import pytest

@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (0, 1, 1),
    (1, 1, 2),
    (2, 1, 3),
    (3, 1, 4),
    (4, 1, 5),
    (5, 1, 6),
    (6, 1, 7),
    (7, 1, 8),
    (8, 1, 9),
    (9, 1, 10)
])

def test_params(x, y, expected):
    assert params.add(x, y) == expected