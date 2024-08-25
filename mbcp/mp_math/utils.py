# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/12 下午9:16
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : utils.py
@Software: PyCharm
"""
from typing import overload

from mbcp.mp_math.mp_math_typing import RealNumber


def clamp(x: float, min_: float, max_: float) -> float:
    """
    区间截断函数。
    Args:
        x:
        min_:
        max_:

    Returns:
        限制后的值
    """
    return max(min(x, max_), min_)


class Approx(float):
    """
    用于近似比较浮点数的类。
    """
    epsilon = 0.001
    """全局近似值。"""

    def __new__(cls, x: RealNumber):
        return super().__new__(cls, x)

    def __eq__(self, other):
        return abs(self - other) < Approx.epsilon

    def __ne__(self, other):
        return not self.__eq__(other)


def approx(x: float, y: float = 0.0, epsilon: float = 0.0001) -> bool:
    """
    判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。
    Args:
        x:
        y:
        epsilon:

    Returns:
        是否近似相等
    """
    return abs(x - y) < epsilon
