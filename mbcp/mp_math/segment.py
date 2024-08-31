# -*- coding: utf-8 -*-
"""
本模块定义了三维空间中的线段类
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .point import Point3  # type: ignore
    from .vector import Vector3  # type: ignore


class Segment3:
    def __init__(self, p1: "Point3", p2: "Point3"):
        """
        三维空间中的线段。
        Args:
            p1 ([`Point3`](./point#class-point3)): 线段的一个端点
            p2 ([`Point3`](./point#class-point3)): 线段的另一个端点
        """
        self.p1 = p1
        self.p2 = p2

        """方向向量"""
        self.direction = self.p2 - self.p1
        """长度"""
        self.length = self.direction.length
        """中心点"""
        self.midpoint = Point3((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2, (self.p1.z + self.p2.z) / 2)

    def __repr__(self):
        """
        线段的字符串表示(可执行)。
        Returns:
            [`str`](https://docs.python.org/3/library/functions.html#str): 字符串
        """
        return f"Segment3({self.p1}, {self.p2})"

    def __str__(self):
        """
        线段的字符串表示。
        Returns:
            [`str`](https://docs.python.org/3/library/functions.html#str): 字符串
        """
        return f"Segment3({self.p1} -> {self.p2})"
