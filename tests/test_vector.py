# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/6 下午1:05
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_vector.py
@Software: PyCharm
"""
from mbcp.mp_math.vector import Vector3
from mbcp.mp_math.point import Point3


def test_v():
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(4, 5, 6)
    v3 = v1 + v2
    assert v3._x == 5
    assert v3._y == 7
    assert v3._z == 9
    print("test_v 1111passed")
