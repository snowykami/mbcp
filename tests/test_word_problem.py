# -*- coding: utf-8 -*-
"""
应用题测试集
"""
import logging

from mbcp.mp_math.line import Line3
from mbcp.mp_math.plane import Plane3
from mbcp.mp_math.point import Point3


class TestWordProblem:

    def test_c8s4e4(self):
        """
        同济大学《高等数学》第八版 下册 第八章第四节例4
        问题：求与两平面x-4z-3=0和2x-y-5z-1=0的交线平行且过点(-3, 2, 5)的直线方程。
        """
        correct_ans = Line3(4, 3, 1, 1)

        pl1 = Plane3(1, 0, -4, -3)
        pl2 = Plane3(2, -1, -5, -1)
        p = Point3(-3, 2, 5)
        """解法1"""
        # 求直线方向向量s
        s = pl1.normal @ pl2.normal
        actual_ans = Line3.from_point_and_direction(p, s)

        logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
        assert actual_ans == correct_ans

        """解法2"""
        # 过点p且与pl1平行的平面pl3
        pl3 = pl1.cal_parallel_plane3(p)
        # 过点p且与pl2平行的平面pl4
        pl4 = pl2.cal_parallel_plane3(p)
        # 求pl3和pl4的交线
        actual_ans = pl3.cal_intersection_line3(pl4)
        print(pl3, pl4, actual_ans)

        logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
        assert actual_ans == correct_ans

