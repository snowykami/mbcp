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
    from .point import Point3


class Line3:
    def __init__(self, a: float, b: float, c: float, d: float):
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

    def get_perpendicular(self, point: "Point3") -> "Line3":
        """
        获取直线经过指定点p的垂线。
        :param point: 指定点p，直线外的点
        :return: 垂直于self且过点p的直线
        """
        a = -self.b
        b = self.a
        c = 0
        d = -(a * point.x + b * point.y + self.c * point.z)
        return Line3(a, b, c, d)

    def get_intersection(self, line: "Line3") -> "Point3":
        """
        获取两条直线的交点。
        :param line:
        :return:
        """
        normal1 = (self.b, -self.a, 0)
        normal2 = (-line.b, line.a, 0)

        if self.is_parallel(line):
            raise ValueError("Lines are parallel and do not intersect.")

        if self.is_collinear(line):
            raise ValueError("Lines are collinear and do not have a single intersection point.")

        if not self.is_coplanar(line):
            raise ValueError("Lines are not coplanar and do not intersect.")

        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = line.a, line.b, line.c, line.d

        t = (b1 * (c2 * d1 - c1 * d2) - b2 * (c1 * d1 - c2 * d2)) / (b1 * c2 - b2 * c1)

        x = self.a * t + self.b * (-d1 / self.b)
        y = -self.b * t + self.a * (d1 / self.a)
        z = 0

        return Point3(x, y, z)

    def is_parallel(self, line: "Line3") -> bool:
        """
        判断两条直线是否平行。
        直线平行的条件是它们的法向量成比例
        :param line:
        :return:
        """
        return self.a * line.b == self.b * line.a and self.c * line.b == self.d * line.a

    def is_collinear(self, line: "Line3") -> bool:
        """
        判断两条直线是否共线。
        直线共线的条件是它们的法向量成比例且常数项也成比例
        :param line:
        :return:
        """
        return self.is_parallel(line) and (self.d * line.b - self.b * line.d) / (self.a * line.b - self.b * line.a) == 0

    def is_coplanar(self, line: "Line3") -> bool:
        """
        判断两条直线是否共面。
        两条直线共面的条件是它们的方向向量和法向量的叉乘为零向量
        :param line:
        :return:
        """
        direction1 = (-self.c, 0, self.a)
        direction2 = (line.c, -line.b, 0)
        cross_product = direction1[0] * direction2[1] - direction1[1] * direction2[0]
        return cross_product == 0
