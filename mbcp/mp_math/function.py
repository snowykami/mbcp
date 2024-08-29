"""
AAA
"""

from .mp_math_typing import ThreeSingleVarsFunc
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
        func: 三元函数
        p: 点
        epsilon: 偏移量
    Returns:
        梯度
    """
    dx = (func(p.x + epsilon, p.y, p.z) - func(p.x - epsilon, p.y, p.z)) / (2 * epsilon)
    dy = (func(p.x, p.y + epsilon, p.z) - func(p.x, p.y - epsilon, p.z)) / (2 * epsilon)
    dz = (func(p.x, p.y, p.z + epsilon) - func(p.x, p.y, p.z - epsilon)) / (2 * epsilon)
    return Vector3(dx, dy, dz)
