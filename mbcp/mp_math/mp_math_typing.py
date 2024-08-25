# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/9 上午11:35
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : mp_math_typing.py
@Software: PyCharm
"""
from typing import Callable, Iterable, TypeAlias, TypeVar

RealNumber: TypeAlias = int | float
Number: TypeAlias = RealNumber | complex
SingleVar = TypeVar("SingleVar", bound=Number)
ArrayVar = TypeVar("ArrayVar", bound=Iterable[Number])
Var: TypeAlias = SingleVar | ArrayVar

OneSingleVarFunc: TypeAlias = Callable[[SingleVar], SingleVar]
OneArrayFunc: TypeAlias = Callable[[ArrayVar], ArrayVar]
OneVarFunc: TypeAlias = OneSingleVarFunc | OneArrayFunc

TwoSingleVarFunc: TypeAlias = Callable[[SingleVar, SingleVar], SingleVar]
TwoArrayFunc: TypeAlias = Callable[[ArrayVar, ArrayVar], ArrayVar]
TwoVarFunc: TypeAlias = TwoSingleVarFunc | TwoArrayFunc

ThreeSingleVarFunc: TypeAlias = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]
ThreeArrayFunc: TypeAlias = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]
ThreeVarFunc: TypeAlias = ThreeSingleVarFunc | ThreeArrayFunc

MultiSingleVarFunc: TypeAlias = Callable[..., SingleVar]
MultiArrayFunc: TypeAlias = Callable[..., ArrayVar]
MultiVarFunc: TypeAlias = MultiSingleVarFunc | MultiArrayFunc
