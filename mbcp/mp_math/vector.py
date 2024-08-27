import math
from typing import overload, TYPE_CHECKING

from .point import Point3

if TYPE_CHECKING:
    from .angle import AnyAngle


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        """
        笛卡尔坐标系中的向量。
        :param x:
        :param y:
        :param z:
        """
        self.x = x
        self.y = y
        self.z = z

    def cal_angle(self, other: 'Vector3') -> 'AnyAngle':
        """
        计算两个向量之间的夹角。
        Args:
            other: 另一个向量
        Returns:
            夹角
        """
        return AnyAngle(math.acos(self * other / (self.length * other.length)), is_radian=True)

    def is_parallel(self, other: 'Vector3') -> bool:
        """
        判断两个向量是否平行。
        Args:
            other: 另一个向量
        Returns:
            是否平行
        """
        return self @ other == Vector3(0, 0, 0)

    def cross(self, other: 'Vector3') -> 'Vector3':
        """
        向量积 叉乘：V1 @ V2 -> V3
        Args:
            other:
        Returns:
            叉乘结果，为0向量则两向量平行，否则垂直于两向量
        """
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    @property
    def length(self) -> float:
        """
        向量的模。
        Returns:
            模
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @property
    def unit(self) -> 'Vector3':
        """
        获取该向量的单位向量。
        Returns:
            单位向量
        """
        return self / self.length

    @overload
    def __add__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __add__(self, other: 'Point3') -> 'Point3':
        ...

    def __add__(self, other):
        """
        V + P -> P\n
        V + V -> V
        Args:
            other:
        Returns:

        """
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Point3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Vector3' and '{type(other)}'")

    def __eq__(self, other):
        """
        判断两个向量是否相等。
        Args:
            other:
        Returns:
            是否相等
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __radd__(self, other: 'Point3') -> 'Point3':
        """
        P + V -> P\n
        别去点那边实现了。
        :param other:
        :return:
        """
        return Point3(self.x + other.x, self.y + other.y, self.z + other.z)

    @overload
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __sub__(self, other: 'Point3') -> 'Point3':
        ...

    def __sub__(self, other):
        """
        V - P -> P\n
        V - V -> V
        Args:
            other:
        Returns:
        """
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Vector3' and '{type(other)}'")

    def __rsub__(self, other: Point3):
        """
        P - V -> P
        Args:
            other:
        Returns:

        """

        if isinstance(other, Point3):
            return Point3(other.x - self.x, other.y - self.y, other.z - self.z)
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other)}' and 'Vector3'")

    @overload
    def __mul__(self, other: float) -> 'Vector3':
        ...

    @overload
    def __mul__(self, other: 'Vector3') -> float:
        ...

    def __mul__(self, other):
        """
        点乘法。包括点乘和数乘。
        V * V -> float\n
        Args:
            other:
        Returns:
            float
        Raises:
            TypeError: 不支持的类型
        """
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Vector3' and '{type(other)}'")

    def __rmul__(self, other: float) -> 'Vector3':
        """
        右乘。
        Args:
            other:
        Returns:
            乘积
        """
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other: 'Vector3') -> 'Vector3':
        """
        向量积 叉乘：V1 @ V2 -> V3
        Args:
            other:
        Returns:
            叉乘结果，为0向量则两向量平行，否则垂直于两向量
        """
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def __truediv__(self, other: float) -> 'Vector3':
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
