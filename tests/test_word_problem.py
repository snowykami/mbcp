# -*- coding: utf-8 -*-
"""
应用题测试集
"""
from liteyuki.log import logger  # type: ignore
from mbcp.mp_math.line import Line3
from mbcp.mp_math.plane import Plane3
from mbcp.mp_math.point import Point3
from mbcp.mp_math.vector import Vector3
from .answer import output_ans, output_step_ans


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

        output_ans(correct_ans, actual_ans, question=question)
        assert actual_ans == correct_ans

        """解法2"""
        # 过点p且与pl1平行的平面pl3
        pl3 = pl1.cal_parallel_plane3(p)
        # 过点p且与pl2平行的平面pl4
        pl4 = pl2.cal_parallel_plane3(p)
        # 求pl3和pl4的交线
        actual_ans = pl3.cal_intersection_line3(pl4)

        output_ans(correct_ans, actual_ans, question=question)
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
        output_ans(correct_ans, actual_ans, question=question)

    def test_c8s4e6(self):
        question = "求过点(2, 3, 1)且与直线(x+1)/3 = (y-1)/2 = z/-1垂直相交的直线的方程。"
        """正确答案"""
        correct_ans = Line3(Point3(2, 1, 3), Vector3(2, -1, 4))
        """题目已知量"""
        point = Point3(2, 1, 3)
        line = Line3(Point3(-1, 1, 0), Vector3(3, 2, -1))

        """解"""
        # 先作过点且垂直与已知直线的平面
        s1_correct_ans = Plane3(3, 2, -1, -5)
        pl = Plane3.from_point_and_normal(point, line.direction)

        output_step_ans(s1_correct_ans, pl, question="作过点且垂直与已知直线的平面")

        # 求该平面与已知直线的交点
        s2_correct_ans = Point3(2 / 7, 13 / 7, -3 / 7)
        s2_actual_ans = pl & line

        output_step_ans(s2_correct_ans, s2_actual_ans, s1_correct_ans.approx(s1_correct_ans), question="求该平面与已知直线的交点")

        # 求所求直线的方向向量
        s3_correct_ans = (-6 / 7) * Vector3(2, -1, 4)

        dv = s2_correct_ans - point

        output_step_ans(s3_correct_ans, dv, condition=s3_correct_ans.unit.approx(dv.unit), question="求所求直线的方向向量")

        # 求所求直线的方程
        actual_ans = Line3(point, dv)

        output_ans(correct_ans, actual_ans, correct_ans.approx(actual_ans), question=question)
