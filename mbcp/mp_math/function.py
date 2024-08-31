"""
AAA
"""

from .mp_math_typing import MultiVarsFunc, OneVarFunc, ThreeSingleVarsFunc, Var
from .point import Point3
from .vector import Vector3
from .const import EPSILON


def cal_gradient_3vf(func: ThreeSingleVarsFunc, p: Point3, epsilon: float = EPSILON) -> Vector3:
    r"""
    计算三元函数在某点的梯度向量。
    > [!tip]
    > 已知一个函数$f(x, y, z)$，则其在点$(x_0, y_0, z_0)$处的梯度向量为:
    $\nabla f(x_0, y_0, z_0) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$
    Args:
        func ([`ThreeSingleVarsFunc`](./mp_math_typing#var-threesinglevarsfunc)): 三元函数
        p ([`Point3`](./point#class-point3)): 点
        epsilon: 偏移量
    Returns:
        梯度
    """
    dx = (func(p.x + epsilon, p.y, p.z) - func(p.x - epsilon, p.y, p.z)) / (2 * epsilon)
    dy = (func(p.x, p.y + epsilon, p.z) - func(p.x, p.y - epsilon, p.z)) / (2 * epsilon)
    dz = (func(p.x, p.y, p.z + epsilon) - func(p.x, p.y, p.z - epsilon)) / (2 * epsilon)
    return Vector3(dx, dy, dz)


def curry(func: MultiVarsFunc, *args: Var) -> OneVarFunc:
    r"""
    对多参数函数进行柯里化。
    > [!tip]
    > 有关函数柯里化，可参考[函数式编程--柯理化（Currying）](https://zhuanlan.zhihu.com/p/355859667)
    Args:
        func ([`MultiVarsFunc`](./mp_math_typing#var-multivarsfunc)): 函数
        *args ([`Var`](./mp_math_typing#var-var)): 参数
    Returns:
        柯里化后的函数
    Examples:
        ```python
        def add(a: int, b: int, c: int) -> int:
            return a + b + c
        add_curried = curry(add, 1, 2)
        add_curried(3)  # 6
        ```
    """

    def curried_func(*args2: Var) -> Var:
        """@litedoc-hide"""
        return func(*args, *args2)

    return curried_func
