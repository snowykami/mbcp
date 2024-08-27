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

from mbcp.mp_math.point import Point3
from mbcp.mp_math.vector import Vector3
from mbcp.mp_math.line import Line3


class TestLine3:

    def test_point_and_normal_factory(self):
        """
        测试通过点和法向量构造直线
        """
        correct_ans = Line3(1, -2, 3, -8)

        p = Point3(2, -3, 0)
        n = Vector3(1, -2, 3)

        actual_ans = Line3.from_point_and_direction(p, n)
        logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
        assert actual_ans == correct_ans


