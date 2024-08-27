# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/6 下午12:57
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : other.py
@Software: PyCharm
"""
from typing import TYPE_CHECKING

from .mp_math_typing import OneSingleVarFunc, RealNumber
from .utils import sign_format
from .vector import Vector3

if TYPE_CHECKING:
    from .angle import AnyAngle
    from .point import Point3


class Line3:
    def __init__(self, point: 'Point3', direction: 'Vector3'):
        """
        三维空间中的直线。由一个点和一个方向向量确定。
        Args:
            point: 直线上的一点
            direction: 直线的方向向量
        """
        self.point = point
        self.direction = direction

    def cal_angle(self, other: 'Line3') -> 'AnyAngle':
        """
        计算直线和直线之间的夹角。
        Args:
            other: 另一条直线
        Returns:
            夹角弧度
        Raises:
            TypeError: 不支持的类型
        """
        return self.direction.cal_angle(other.direction)

    def cal_intersection(self, other: 'Line3') -> 'Point3':
        """
        计算两条直线的交点。
        Args:
            other: 另一条直线
        Returns:
            交点
        """
        if self.is_parallel(other):
            raise ValueError("Lines are parallel and do not intersect.")
        if not self.is_coplanar(other):
            raise ValueError("Lines are not coplanar and do not intersect.")
        return self.point + self.direction.cross(other.direction)

    def cal_perpendicular(self, point: 'Point3') -> 'Line3':
        """
        计算直线经过指定点p的垂线。
        Args:
            point: 指定点
        Returns:
            垂线
        """
        return Line3(point, self.direction.cross(point - self.point))

    def get_point(self, t: RealNumber) -> 'Point3':
        """
        获取直线上的点。同一条直线，但起始点和方向向量不同，则同一个t对应的点不同。
        Args:
            t: 参数t
        Returns:
            点
        """
        return self.point + t * self.direction

    def get_parametric_equations(self) -> tuple[OneSingleVarFunc, OneSingleVarFunc, OneSingleVarFunc]:
        """
        获取直线的参数方程。
        Returns:
            x(t), y(t), z(t)
        """
        return (lambda t: self.point.x + self.direction.x * t,
                lambda t: self.point.y + self.direction.y * t,
                lambda t: self.point.z + self.direction.z * t)

    def is_parallel(self, other: 'Line3') -> bool:
        """
        判断两条直线是否平行。
        Args:
            other: 另一条直线
        Returns:
            是否平行
        """
        return self.direction.is_parallel(other.direction)

    def is_collinear(self, other: 'Line3') -> bool:
        """
        判断两条直线是否共线。
        Args:
            other: 另一条直线
        Returns:
            是否共线
        """
        return self.is_parallel(other) and (self.point - other.point).is_parallel(self.direction)

    def is_coplanar(self, other: 'Line3') -> bool:
        """
        判断两条直线是否共面。
        Args:
            other: 另一条直线
        Returns:
            是否共面
        """
        return self.direction.cross(other.direction).is_parallel(self.direction)

    def simplify(self):
        """
        简化直线方程，等价相等。
        自体简化，不返回值。

        按照可行性一次对x y z 化 0 处理，并对向量单位化
        """
        self.direction.normalize()
        # 平行与zy平面，x始终为0
        if self.direction.x == 0:
            self.point.x = 0
        # 平行与xz平面，y始终为0
        if self.direction.y == 0:
            self.point.y = 0
        # 平行与xy平面，z始终为0
        if self.direction.z == 0:
            self.point.z = 0

    @classmethod
    def from_two_points(cls, p1: 'Point3', p2: 'Point3') -> 'Line3':
        """
        工厂函数 由两点构造直线。
        Args:
            p1: 点1
            p2: 点2
        Returns:
            直线
        """
        direction = p2 - p1
        return cls(p1, direction)

    def __and__(self, other: 'Line3') -> 'Point3':
        """
        计算两条直线点集合的交集。交点
        Args:
            other: 另一条直线
        Returns:
            交点
        """
        return self.cal_intersection(other)

    def __eq__(self, other) -> bool:
        """
        判断两条直线是否等价。

        v1 // v2 ∧ (p1 - p2) // v1
        Args:
            other:

        Returns:

        """
        return self.direction.is_parallel(other.direction) and (self.point - other.point).is_parallel(self.direction)

    def __str__(self):
        """
        返回点向式（x-x0）
        Returns:

        """
        s = "Line3: "
        if self.direction.x != 0:
            s += f"(x{sign_format(-self.point.x)})/{self.direction.x}"
        if self.direction.y != 0:
            s += f" = (y{sign_format(-self.point.y)})/{self.direction.y}"
        if self.direction.z != 0:
            s += f" = (z{sign_format(-self.point.z)})/{self.direction.z}"
        return s

    def __repr__(self):
        return f"Line3({self.point}, {self.direction})"
