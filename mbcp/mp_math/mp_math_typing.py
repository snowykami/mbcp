# -*- coding: utf-8 -*-
"""
本模块用于内部类型提示
"""
from typing import Callable, Iterable, TypeAlias, TypeVar

RealNumber: TypeAlias = int | float  # 实数
Number: TypeAlias = RealNumber | complex  # 数
SingleVar = TypeVar("SingleVar", bound=Number)  # 单变量
ArrayVar = TypeVar("ArrayVar", bound=Iterable[Number])  # 数组变量
Var: TypeAlias = SingleVar | ArrayVar  # 变量

OneSingleVarFunc: TypeAlias = Callable[[SingleVar], SingleVar]  # 一元单变量函数
OneArrayFunc: TypeAlias = Callable[[ArrayVar], ArrayVar]  # 一元数组函数
OneVarFunc: TypeAlias = OneSingleVarFunc | OneArrayFunc  # 一元函数

TwoSingleVarsFunc: TypeAlias = Callable[[SingleVar, SingleVar], SingleVar]  # 二元单变量函数
TwoArraysFunc: TypeAlias = Callable[[ArrayVar, ArrayVar], ArrayVar]  # 二元数组函数
TwoVarsFunc: TypeAlias = TwoSingleVarsFunc | TwoArraysFunc  # 二元函数

ThreeSingleVarsFunc: TypeAlias = Callable[[SingleVar, SingleVar, SingleVar], SingleVar]  # 三元单变量函数
ThreeArraysFunc: TypeAlias = Callable[[ArrayVar, ArrayVar, ArrayVar], ArrayVar]  # 三元数组函数
ThreeVarsFunc: TypeAlias = ThreeSingleVarsFunc | ThreeArraysFunc  # 三元函数

MultiSingleVarsFunc: TypeAlias = Callable[..., SingleVar]  # 多元单变量函数
MultiArraysFunc: TypeAlias = Callable[..., ArrayVar]  # 多元数组函数
MultiVarsFunc: TypeAlias = MultiSingleVarsFunc | MultiArraysFunc  # 多元函数
