# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/7 上午12:42
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : segment.py
@Software: PyCharm
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .point import Point3  # type: ignore
    from .vector import Vector3  # type: ignore


class Segment3:
    def __init__(self, p1: "Point3", p2: "Point3"):
        """
        三维空间中的线段。
        :param p1:
        :param p2:
        """
        self._start = p1
        self._end = p2

        """方向向量"""
        self._direction = self._end - self._start
        """长度"""
        self._length = self._direction.length
        """中心点"""
        self._midpoint = (self._start + self._end) / 2

    def __str__(self):
        return f"Segment3({self._start}, {self._end})"

    def _unset_properties(self):
        self._length = None
        self._direction = None
        self._midpoint = None

    @property
    def start(self) -> "Point3":
        return self._start

    @start.setter
    def start(self, value: "Point3"):
        self._start = value
        self._unset_properties()

    @property
    def end(self) -> "Point3":
        return self._end

    @end.setter
    def end(self, value: "Point3"):
        self._end = value
        self._unset_properties()

    @property
    def length(self) -> float:
        """
        线段的长度。
        :return:
        """
        if self._length is None:
            self._length = (self._end - self._start).length
        return self._length

    @property
    def direction(self) -> "Vector3":
        """
        线段的方向向量。
        :return:
        """
        if self._direction is None:
            self._direction = self._end - self._start
        return self._direction

    @property
    def midpoint(self) -> "Point3":
        """
        线段的中点。
        :return:
        """
        if self._midpoint is None:
            self._midpoint = (self._start + self._end) / 2
        return self._midpoint
