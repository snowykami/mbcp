# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/6 下午1:30
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : main.py
@Software: PyCharm
"""
import logging

from mbcp.mp_math.line import Line3
from mbcp.mp_math.plane import Plane3
from mbcp.mp_math.point import Point3

# def ac8s4e4():
#     """
#     第八章第四节例4
#     问题：求与两平面x-4z-3=0和2x-y-5z-1=0的交线平行且过点(-3, 2, 5)的直线方程。
#     """
#     correct_ans = Line3(4, 3, 1, 1)
#
#     pl1 = Plane3(1, 0, -4, -3)
#     pl2 = Plane3(2, -1, -5, -1)
#     p = Point3(-3, 2, 5)
#     """解法1"""
#     # 求直线方向向量s
#     s = pl1.normal @ pl2.normal
#     actual_ans = Line3.from_point_and_direction(p, s)
#
#     logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
#     assert actual_ans == correct_ans
#
#     """解法2"""
#     # 过点p且与pl1平行的平面pl3
#     pl3 = pl1.cal_parallel_plane3(p)
#     # 过点p且与pl2平行的平面pl4
#     pl4 = pl2.cal_parallel_plane3(p)
#     # 求pl3和pl4的交线
#     actual_ans = pl3.cal_intersection_line3(pl4)
#     print(pl3, pl4, actual_ans)
#
#     logging.info(f"正确答案：{correct_ans}    实际答案：{actual_ans}")
#     assert actual_ans == correct_ans
#
#
# ac8s4e4()
import logging

from mbcp.mp_math.mp_math_typing import RealNumber
from mbcp.mp_math.utils import Approx


def three_var_func(x: RealNumber, y: RealNumber) -> RealNumber:
    return x ** 3 * y ** 2 - 3 * x * y ** 3 - x * y + 1


class TestPartialDerivative:
    # 样例来源：同济大学《高等数学》第八版下册 第九章第二节 例6
    def test_2v_1o_1v(self):
        """测试二元函数关于第一个变量(x)的一阶偏导 df/dx"""

        from mbcp.mp_math.utils import Approx
        from mbcp.mp_math.equation import get_partial_derivative_func

        partial_derivative_func = get_partial_derivative_func(three_var_func, 0)

        # assert partial_derivative_func(1, 2, 3) == 4.0
        def df_dx(x, y):
            """原函数关于x的偏导"""
            return 3 * (x ** 2) * (y ** 2) - 3 * (y ** 3) - y

        logging.info(f"Expected: {df_dx(1, 2)}, Actual: {partial_derivative_func(1, 2)}")
        assert Approx(partial_derivative_func(1, 2)) == df_dx(1, 2)

    def test_2v_1o_2v(self):
        """测试二元函数关于第二个变量(y)的一阶偏导 df/dy"""

        from mbcp.mp_math.utils import Approx
        from mbcp.mp_math.equation import get_partial_derivative_func

        partial_derivative_func = get_partial_derivative_func(three_var_func, 1)

        def df_dy(x, y):
            """原函数关于y的偏导"""
            return 2 * (x ** 3) * y - 9 * x * (y ** 2) - x

        logging.info(f"Expected: {df_dy(1, 2)}, Actual: {partial_derivative_func(1, 2)}")
        assert Approx(partial_derivative_func(1, 2)) == df_dy(1, 2)

    def test_2v_2o_12v(self):
        """高阶偏导d^2f/(dxdy)"""

        from mbcp.mp_math.utils import Approx
        from mbcp.mp_math.equation import get_partial_derivative_func

        partial_derivative_func = get_partial_derivative_func(three_var_func, (0, 1))

        def df_dxdy(x, y):
            """原函数关于y和x的偏导"""
            return 6 * x ** 2 * y - 9 * y ** 2 - 1

        logging.info(f"Expected: {df_dxdy(1, 2)}, Actual: {partial_derivative_func(1, 2)}")
        assert Approx(partial_derivative_func(1, 2)) == df_dxdy(1, 2)

    def test_2v_2o_1v2(self):
        """二阶偏导d^2f/(dx^2)"""

        from mbcp.mp_math.utils import Approx
        from mbcp.mp_math.equation import get_partial_derivative_func

        partial_derivative_func = get_partial_derivative_func(three_var_func, (0, 0))

        def df_dydx(x, y):
            """原函数关于x和y的偏导"""
            return 6 * x * y ** 2

        logging.info(f"Expected: {df_dydx(1, 2)}, Actual: {partial_derivative_func(1, 2)}")
        assert Approx(partial_derivative_func(1, 2)) == df_dydx(1, 2)

    def test_2v_3o_1v3(self):
        """高阶偏导d^3f/(dx^3)"""

        from mbcp.mp_math.utils import Approx
        from mbcp.mp_math.equation import get_partial_derivative_func

        partial_derivative_func = get_partial_derivative_func(three_var_func, (0, 0, 0))

        def d3f_dx3(x, y):
            """原函数关于x的三阶偏导"""
            return 6 * (y ** 2)

        logging.info(f"Expected: {d3f_dx3(1, 2)}, Actual: {partial_derivative_func(1, 2)}")
        assert Approx(partial_derivative_func(1, 2)) == d3f_dx3(1, 2)

    def test_possible_error(self):
        from mbcp.mp_math.equation import get_partial_derivative_func
        def two_vars_func(x: RealNumber, y: RealNumber) -> RealNumber:
            return x ** 2 * y ** 2

        partial_func = get_partial_derivative_func(two_vars_func, 0)
        partial_func_2 = get_partial_derivative_func(two_vars_func, (0, 0))
        assert Approx(partial_func_2(1, 2)) == 8


TestPartialDerivative().test_2v_1o_1v()
TestPartialDerivative().test_2v_1o_2v()
TestPartialDerivative().test_2v_2o_12v()
TestPartialDerivative().test_2v_2o_1v2()
TestPartialDerivative().test_2v_3o_1v3()

TestPartialDerivative().test_possible_error()
