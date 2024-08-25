# -*- coding: utf-8 -*-
"""
偏导测试

"""
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
