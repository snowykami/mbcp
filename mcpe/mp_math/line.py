# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/6 下午12:57
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : line.py
@Software: PyCharm
"""
from typing import overload, TYPE_CHECKING

if TYPE_CHECKING:
    from mcpe.mp_math.point import Point3
    from mcpe.mp_math.vector import Vector3


class Line3:
    def __init__(self, a: float, b: float, c: float, d:float):
        """
        三维空间中的直线。
        :param a:
        :param b:
        :param c:
        :param d:
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"Line3({self.a}, {self.b}, {self.c}, {self.d})"

    def get_perpendicular(self, p: "Point3") -> "Line3":
        """
        获取直线经过指定点p的垂线。
        :param p: 指定点p，直线外的点
        :return: 垂直于self且过点p的直线
        """
        a = -self.b
        b = self.a
        c = 0
        d = -(a * p.x + b * p.y + self.c * p.z)
        return Line3(a, b, c, d)

    def get_intersection(self, l: "Line3") -> "Point3":
        """
        获取两空间直线的交点。
        :param l: 另一条直线，不平行于self，不共线，且共面
        :return: 交点
        """
        # 平行检测
        if ...:
            ...
        # 共线检测
        if ...:
            ...
        # 不共线检测
        if ...:
            ...





