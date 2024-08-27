# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/6 下午12:57
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : other.py
@Software: PyCharm
"""
import math
from typing import TYPE_CHECKING, overload
from .vector import Vector3

if TYPE_CHECKING:
    from .angle import AnyAngle
    from .plane import Plane3
    from .point import Point3


class Line3:
    def __init__(self, a: float, b: float, c: float, d: float):
        """
        三维空间中的直线。
        Args:
            a: 直线方程的系数a
            b: 直线方程的系数b
            c: 直线方程的系数c
            d: 直线方程的常数项d
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def cal_angle(self, other: "Line3") -> "AnyAngle":
        """
        计算直线和直线或面之间的夹角。
        Args:
            other: 另一条直线或面
        Returns:
            夹角弧度
        Raises:
            TypeError: 不支持的类型
        """
        if isinstance(other, Line3):
            return self.direction.cal_angle(other.direction)
        elif isinstance(other, Plane3):
            return self.direction.cal_angle(other.normal).complementary  # 方向向量和法向量的夹角的余角
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    @property
    def direction(self) -> "Vector3":
        """
        直线的方向向量。
        Returns:
            方向向量
        """
        return Vector3(self.a, self.b, self.c)

    def cal_intersection(self, line: "Line3") -> "Point3":
        """
        计算两条直线的交点。
        Args:
            line: 另一条直线
        Returns:
            交点
        """

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

    def cal_perpendicular(self, point: "Point3") -> "Line3":
        """
        计算直线经过指定点p的垂线。
        Args:
            point: 指定点
        Returns:
            垂线
        """
        a = -self.b
        b = self.a
        c = 0
        d = -(a * point.x + b * point.y + self.c * point.z)
        return Line3(a, b, c, d)

    def is_parallel(self, line: "Line3") -> bool:
        """
        判断两条直线是否平行。
        直线平行的条件是它们的法向量成比例
        Args:
            line: 另一条直线
        Returns:
            是否平行
        """
        return self.direction.is_parallel(line.direction)

    def is_collinear(self, line: "Line3") -> bool:
        """
        判断两条直线是否共线。
        直线共线的条件是它们的法向量成比例且常数项也成比例
        Args:
            line: 另一条直线
        Returns:
            是否共线
        """
        return self.is_parallel(line) and (self.d * line.b - self.b * line.d) / (self.a * line.b - self.b * line.a) == 0

    def is_coplanar(self, line: "Line3") -> bool:
        """
        判断两条直线是否共面。
        两条直线共面的条件是它们的方向向量和法向量的叉乘为零向量
        Args:
            line: 另一条直线
        Returns:
            是否共面
        """
        direction1 = (-self.c, 0, self.a)
        direction2 = (line.c, -line.b, 0)
        cross_product = direction1[0] * direction2[1] - direction1[1] * direction2[0]
        return cross_product == 0

    @classmethod
    def from_point_and_direction(cls, point: "Point3", direction: "Vector3") -> "Line3":
        """
        工厂函数 由点和方向向量构造直线(点向式构造)。
        Args:
            point: 点
            direction: 方向向量
        Returns:
            直线
        """
        a, b, c = direction.x, direction.y, direction.z
        d = -(a * point.x + b * point.y + c * point.z)
        return cls(a, b, c, d)

    @classmethod
    def from_two_points(cls, p1: "Point3", p2: "Point3") -> "Line3":
        """
        工厂函数 由两点构造直线。
        Args:
            p1: 点1
            p2: 点2
        Returns:
            直线
        """
        direction = p2 - p1
        return cls.from_point_and_direction(p1, direction)

    def __eq__(self, other) -> bool:
        """
        判断两条直线是否等价。
        Args:
            other:

        Returns:

        """
        return self.a / other.a == self.b / other.b == self.c / other.c == self.d / other.d

    def __repr__(self):
        return f"Line3({self.a}, {self.b}, {self.c}, {self.d})"

    def __str__(self):
        return f"Line3({self.a}, {self.b}, {self.c}, {self.d})"
