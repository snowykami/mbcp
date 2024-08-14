# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/9 上午11:32
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : equation.py
@Software: PyCharm
"""
import numpy as np

from .point import Point3
from .mp_math_typing import ONE_VARIABLE_FUNC, TWO_VARIABLES_FUNC, THREE_VARIABLES_FUNC

class CurveEquation:
    def __init__(self, x_func: ONE_VARIABLE_FUNC, y_func: ONE_VARIABLE_FUNC, z_func: ONE_VARIABLE_FUNC):
        """
        曲线方程。
        :param x_func:
        :param y_func:
        :param z_func:
        """
        self.x_func = x_func
        self.y_func = y_func
        self.z_func = z_func

    def __call__(self, *t: float) -> "Point3" | tuple["Point3"]:
        if len(t) == 1:
            return Point3(self.x_func(t[0]), self.y_func(t[0]), self.z_func(t[0]))
        else:
            # np加速
            ...



    def __str__(self):
        return "CurveEquation()"
