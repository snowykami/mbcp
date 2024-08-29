# -*- coding: utf-8 -*-
"""
本模块定义了方程相关的类和函数以及一些常用的数学函数
"""

from .mp_math_typing import OneVarFunc, Var, MultiVarsFunc, Number
from .point import Point3
from .const import EPSILON


class CurveEquation:
    def __init__(self, x_func: OneVarFunc, y_func: OneVarFunc, z_func: OneVarFunc):
        """
        曲线方程。
        Args:
            x_func: x函数
            y_func: y函数
            z_func: z函数
        """
        self.x_func = x_func
        self.y_func = y_func
        self.z_func = z_func

    def __call__(self, *t: Var) -> Point3 | tuple[Point3, ...]:
        """
        计算曲线上的点。
        Args:
            *t:
                参数
        Returns:
            目标点
        """
        if len(t) == 1:
            return Point3(self.x_func(t[0]), self.y_func(t[0]), self.z_func(t[0]))
        else:
            return tuple([Point3(x, y, z) for x, y, z in zip(self.x_func(t), self.y_func(t), self.z_func(t))])

    def __str__(self):
        return "CurveEquation()"


def get_partial_derivative_func(func: MultiVarsFunc, var: int | tuple[int, ...], epsilon: Number = EPSILON) -> MultiVarsFunc:
    """
    求N元函数一阶偏导函数。这玩意不太稳定，慎用。
    > [!warning]
    > 目前数学界对于一个函数的导函数并没有通解的说法，因此该函数的稳定性有待提升

    Args:
        func: 函数
        var: 变量位置，可为整数(一阶偏导)或整数元组(高阶偏导)
        epsilon: 偏移量
    Returns:
        偏导函数
    Raises:
        ValueError: 无效变量类型
    """
    # 内部函数不注释，以防止生成文档
    if isinstance(var, int):
        def partial_derivative_func(*args: Var) -> Var:
            """@litedoc-hide"""
            args_list_plus = list(args)
            args_list_plus[var] += epsilon
            args_list_minus = list(args)
            args_list_minus[var] -= epsilon
            return (func(*args_list_plus) - func(*args_list_minus)) / (2 * epsilon)

        return partial_derivative_func
    elif isinstance(var, tuple):
        def high_order_partial_derivative_func(*args: Var) -> Var:
            """
            @litedoc-hide
            求高阶偏导函数
            Args:
                *args: 参数
            Returns:
                高阶偏导数值
            """
            result_func = func
            for v in var:
                result_func = get_partial_derivative_func(result_func, v, epsilon)
            return result_func(*args)

        return high_order_partial_derivative_func
    else:
        raise ValueError("Invalid var type")


def curry(func: MultiVarsFunc, *args: Var) -> OneVarFunc:
    """
    对多参数函数进行柯里化。
    > [!tip]
    > 有关函数柯里化，可参考[函数式编程--柯理化（Currying）](https://zhuanlan.zhihu.com/p/355859667)
    Args:
        func: 函数
        *args: 参数
    Returns:
        柯里化后的函数
    """
    def curried_func(*args2: Var) -> Var:
        """@litedoc-hide"""
        return func(*args, *args2)
    return curried_func
