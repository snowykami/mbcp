# -*- coding: utf-8 -*-
"""
应用题测试集
"""
from liteyuki.log import logger  # type: ignore
from mbcp.mp_math.line import Line3
from mbcp.mp_math.plane import Plane3
from mbcp.mp_math.point import Point3
from mbcp.mp_math.vector import Vector3
from .answer import output_answer


class TestWordProblem:

    def test_c8s4e4(self):
        """
        同济大学《高等数学》第八版 下册 第八章第四节例4
        问题：求与两平面x-4z-3=0和2x-y-5z-1=0的交线平行且过点(-3, 2, 5)的直线方程。
        """
        question = "求与两平面x-4z-3=0和2x-y-5z-1=0的交线平行且过点(-3, 2, 5)的直线方程。"
        correct_ans = Line3(Point3(-3, 2, 5), Vector3(4, 3, 1))
        pl1 = Plane3(1, 0, -4, -3)
        pl2 = Plane3(2, -1, -5, -1)
        p = Point3(-3, 2, 5)
        """解法1"""
        # 求直线方向向量s
        s = pl1.normal.cross(pl2.normal)
        actual_ans = Line3(p, s)

        output_answer(correct_ans, actual_ans, question)
        assert actual_ans == correct_ans

        """解法2"""
        # 过点p且与pl1平行的平面pl3
        pl3 = pl1.cal_parallel_plane3(p)
        # 过点p且与pl2平行的平面pl4
        pl4 = pl2.cal_parallel_plane3(p)
        # 求pl3和pl4的交线
        actual_ans = pl3.cal_intersection_line3(pl4)

        output_answer(correct_ans, actual_ans, question)
        assert actual_ans == correct_ans

    def test_c8s4e5(self):
        """
        同济大学《高等数学》第八版 下册 第八章第四节例5

        求直线(x-2)/1=(y-3)/1=(z-4)/2与平面2x+y+z-6=0的交点。
        """
        question = "求直线(x-2)/1=(y-3)/1=(z-4)/2与平面2x+y+z-6=0的交点。"
        """正确答案"""
        correct_ans = Point3(1, 2, 2)
        """题目已知量"""
        line = Line3(Point3(2, 3, 4), Vector3(1, 1, 2))
        plane = Plane3(2, 1, 1, -6)

        """解"""
        actual_ans = plane & line
        output_answer(correct_ans, actual_ans, question)

    def test_c8s4e6(self):
        question = "求过点(2, 3, 1)且与直线(x+1)/3 = (y-1)/2 = z/-1垂直相交的直线的方程。"
        """正确答案"""
        correct_ans = Line3(Point3(2, 1, 3), Vector3(2, -1, 4))
        """题目已知量"""
        point = Point3(2, 3, 1)
        line = Line3(Point3(-1, 1, 0), Vector3(3, 2, -1))

        """解"""
        # 先作平面过点且垂直与已知直线
        pl = line.cal_perpendicular(point)
        logger.debug(line.get_point(1))

        # output_answer(correct_ans, actual_ans, question)


