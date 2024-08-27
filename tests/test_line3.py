# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/26 上午7:54
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_line3.py
@Software: PyCharm
"""
import logging

from liteyuki import logger  # type: ignore

from mbcp.mp_math.angle import AnyAngle
from mbcp.mp_math.const import PI
from mbcp.mp_math.point import Point3
from mbcp.mp_math.utils import approx
from mbcp.mp_math.vector import Vector3
from mbcp.mp_math.line import Line3
from tests.answer import output_ans


class TestLine3:

    def test_cal_angle(self) -> None:
        """
        计算两条直线的夹角
        """
        """测试样例们"""
        samples: tuple[tuple[Line3, Line3, AnyAngle], ...] = (
                (
                        Line3(Point3(0, 0, 0), Vector3(1, 1, 0)),
                        Line3(Point3(0, 0, 0), Vector3(1, 0, 0)),
                        AnyAngle(45)
                ),
                (
                        Line3(Point3(0, 0, 0), Vector3(0, 1, 0)),
                        Line3(Point3(0, 0, 0), Vector3(1, 0, 0)),
                        AnyAngle(90)
                )
        )

        for sample in samples:
            correct_ans = sample[2]
            actual_ans = sample[0].cal_angle(sample[1])
            output_ans(correct_ans, actual_ans, question="计算两条直线的夹角")
            assert correct_ans == actual_ans

    def test_cal_distance(self) -> None:
        """
        计算两条直线的距离
        """
        """测试样例们"""
        samples: tuple[tuple[Line3, Line3, float], ...] = (
                (  # 重合
                        Line3(Point3(0, 0, 0), Vector3(1, 1, 1)),
                        Line3(Point3(0, 0, 0), Vector3(2, 2, 2)),
                        0
                ),
                (  # 两条直线相交
                        Line3(Point3(0, 0, 0), Vector3(1, 1, 0)),
                        Line3(Point3(0, 0, 0), Vector3(1, 0, 0)),
                        0
                ),
                (  # 平行线
                        Line3.from_two_points(Point3(0, 0, 0), Point3(1, 1, 0)),
                        Line3.from_two_points(Point3(0, 0, 1), Point3(1, 1, 1)),
                        1
                ),
                (   # 异面
                        Line3.from_two_points(Point3(0, 0, 0), Point3(1, 1, 0)),
                        Line3.from_two_points(Point3(1, 0, 2), Point3(0, 1, 2)),
                        2
                ),
                (   # 异面2
                        Line3.from_two_points(Point3(1, 0, 1), Point3(2, 1 ,0)),
                        Line3.from_two_points(Point3(1, 2, 0), Point3(0, 1, 1)),
                        2 ** 0.5
                )
        )

        for sample in samples:
            correct_ans = sample[2]
            actual_ans = sample[0].cal_distance(sample[1])
            output_ans(correct_ans, actual_ans,approx(correct_ans, actual_ans), question="计算两条直线的距离")

    def test_equal(self):
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(1, 1, 1), Vector3(2, 2, 2))
        output_ans(True, line1 == line2, question="判断两条直线是否相等")

        # 反例
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(1, 1, 1), Vector3(2, 2, 2.1))
        output_ans(False, line1 == line2, question="判断两条直线是否不相等")

    def test_approx(self):
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(1, 1, 1), Vector3(2, 2, 2.000000001))
        output_ans(True, line1.approx(line2), question="判断两条直线是否近似相等")

        # 反例
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(1, 1, 1), Vector3(2, 2, 3.1))
        output_ans(False, line1.approx(line2), question="判断两条直线是否不近似相等")

    def test_cal_intersection(self):
        line1 = Line3.from_two_points(Point3(0, 0, 0), Point3(2, 2, 2))
        line2 = Line3.from_two_points(Point3(0, 0, 2), Point3(2, 2, 0))
        output_ans(Point3(1, 1, 1), line1 & line2, question="计算两条直线的交点测1")

        line1 = Line3.from_two_points(Point3(0, 0, 0), Point3(0, 2, 2))
        line2 = Line3.from_two_points(Point3(0, 0, 2), Point3(0, 2, 0))
        output_ans(Point3(0, 1, 1), line1 & line2, question="计算两条直线的交点测2")

        line1 = Line3.from_two_points(Point3(0, 0, 0), Point3(0, 0, 2))
        line2 = Line3.from_two_points(Point3(0, 0, 2), Point3(0, 2, 0))
        output_ans(Point3(0, 0, 2), line1 & line2, question="计算两条直线的交点测3")

        # 反例：平行线无交点
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(2, 3, 1), Vector3(1, 1, 1))
        output_ans(None, line1 & line2, question="平行线交集为空集")

        # 反例：重合线交集为自身
        line1 = Line3(Point3(1, 1, 1), Vector3(1, 1, 1))
        line2 = Line3(Point3(0, 0, 0), Vector3(2, 2, 2))
        output_ans(line1, line1 & line2, question="重合线的交集为自身")
