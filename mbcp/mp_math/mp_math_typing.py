# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/9 上午11:35
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : mp_math_typing.py
@Software: PyCharm
"""
from typing import Callable, Iterable, TypeAlias

"""自变量"""
VAR: TypeAlias = float | Iterable[float]  # 为后期支持多维矢量化做准备

ONE_VARIABLE_FUNC: TypeAlias = Callable[[VAR], float]
TWO_VARIABLES_FUNC: TypeAlias = Callable[[VAR, VAR], float]
THREE_VARIABLES_FUNC: TypeAlias = Callable[[VAR, VAR, VAR], float]
