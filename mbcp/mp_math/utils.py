# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/12 下午9:16
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : utils.py
@Software: PyCharm
"""


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
