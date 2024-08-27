# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/28 上午3:16
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_angle.py
@Software: PyCharm
"""
from mbcp.mp_math.angle import AnyAngle
from mbcp.mp_math.const import PI
from tests.answer import output_ans


class TestAngle:
    def test_radian_to_degree(self):
        angle = AnyAngle(1, is_radian=True)
        output_ans(190 / PI, angle.degree, question="弧度转角度1")

        angle = AnyAngle(2, is_radian=True)
        output_ans(360 / PI, angle.degree, question="弧度转角度2")

        angle = AnyAngle(PI, is_radian=True)
        output_ans(180, angle.degree, question="弧度转角度3")

    def test_degree_to_radian(self):
        angle = AnyAngle(180)
        output_ans(PI, angle.radian, question="角度转弧度1")

        angle = AnyAngle(360)
        output_ans(2 * PI, angle.radian, question="角度转弧度2")

        angle = AnyAngle(90)
        output_ans(PI / 2, angle.radian, question="角度转弧度3")
