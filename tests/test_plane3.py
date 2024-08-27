# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/26 上午9:07
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_plane3.py
@Software: PyCharm
"""
import logging

from mbcp.mp_math.line import Line3
from mbcp.mp_math.plane import Plane3
from mbcp.mp_math.point import Point3
from mbcp.mp_math.vector import Vector3


class TestPlane3:

    def test_intersection_line3(self):
        """
        测试平面的交线
        """
        correct_ans = Line3(Point3(-3, 2, 5), Vector3(4, 3, 1))

        pl1 = Plane3(1, 0, -4, 23)
        pl2 = Plane3(2, -1, -5, 33)
        actual_ans = pl1 & pl2  # 平面交线
        logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
        assert actual_ans == correct_ans
