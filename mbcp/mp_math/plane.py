# -*- coding: utf-8 -*-
"""
平面模块
"""
import math
from typing import TYPE_CHECKING

import numpy as np

from .vector import Vector3
from .line import Line3
from .point import Point3

if TYPE_CHECKING:
    from .angle import AnyAngle


class Plane3:
    def __init__(self, a: float, b: float, c: float, d: float):
        """
        平面方程：ax + by + cz + d = 0
        Args:
            a:
            b:
            c:
            d:
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def cal_angle(self, other: "Line3 | Plane3") -> "AnyAngle":
        """
        计算平面与平面之间的夹角。
        Args:
            other: 另一个平面
        Returns:
            夹角弧度
        Raises:
            TypeError: 不支持的类型
        """
        if isinstance(other, Line3):
            return self.normal.cal_angle(other.direction).complementary
        elif isinstance(other, Plane3):
            return AnyAngle(math.acos(self.normal * other.normal / (self.normal.length * other.normal.length)), is_radian=True)
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def cal_distance(self, other: "Plane3 | Point3") -> float:
        """
        计算平面与平面或点之间的距离。
        Args:
            other: 另一个平面或点
        Returns:
            距离
        Raises:
            TypeError: 不支持的类型
        """
        if isinstance(other, Plane3):
            return 0
        elif isinstance(other, Point3):
            return abs(self.a * other.x + self.b * other.y + self.c * other.z + self.d) / (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def cal_intersection_line3(self, other: "Plane3") -> "Line3":
        """
        计算两平面的交线。该方法有问题，待修复。
        Args:
            other: 另一个平面
        Returns:
            交线
        """
        # 计算两法向量的叉积作为交线的方向向量
        s = self.normal.cross(other.normal)  # 交线的方向向量
        # 联立两平面方程求交线的一点
        # 两平面方程联立得到的方程组
        # | a1x + b1y + c1z = -d1
        # | a2x + b2y + c2z = -d2
        # 用numpy解方程组
        a = np.array([[self.a, self.b, self.c], [other.a, other.b, other.c]])
        b = np.array([-self.d, -other.d])
        p = np.linalg.lstsq(a, b, rcond=None)[0]
        return Line3.from_point_and_direction(Point3(*p), s)

    def cal_parallel_plane3(self, point: "Point3") -> "Plane3":
        """
        计算平行于该平面且过指定点的平面。
        Args:
            point: 指定点
        Returns:
            平面
        """
        return Plane3.from_point_and_normal(point, self.normal)

    @property
    def normal(self) -> "Vector3":
        """
        平面的法向量。
        Returns:
            法向量
        """
        return Vector3(self.a, self.b, self.c)

    @classmethod
    def from_point_and_normal(cls, point: "Point3", normal: "Vector3") -> "Plane3":
        """
        工厂函数 由点和法向量构造平面(点法式构造)。
        Args:
            point: 平面上的一点
            normal: 法向量
        Returns:
            平面
        """
        a, b, c = normal.x, normal.y, normal.z
        d = -a * point.x - b * point.y - c * point.z  # d = -ax - by - cz
        return cls(a, b, c, d)

    def __repr__(self):
        return f"Plane3({self.a}, {self.b}, {self.c}, {self.d})"

    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c}z + {self.d} = 0"
