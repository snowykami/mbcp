from typing import overload, TYPE_CHECKING

if TYPE_CHECKING:
    from .point import Point3  # type: ignore


class Vector3:
    def __init__(self, x, y, z):
        """
        笛卡尔坐标系中的向量。
        :param x:
        :param y:
        :param z:
        """
        self._x = x
        self._y = y
        self._z = z
        self._length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        self._normalized = self / self._length

    def __str__(self):
        return f"Vector3({self._x}, {self._y}, {self._z})"

    def _unset_properties(self):
        self._length = None
        self._normalized = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._unset_properties()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._unset_properties()

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        self._unset_properties()

    @property
    def length(self) -> float:
        """
        向量的模。
        :return:
        """
        if self._length is None:
            self._length = (self._x ** 2 + self._y ** 2 + self._z ** 2) ** 0.5
        return self._length

    @property
    def normalized(self) -> 'Vector3':
        """
        返回该向量的单位向量。
        :return:
        """
        if self._normalized is None:
            self._normalized = self / self.length
        return self._normalized

    @overload
    def __add__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __add__(self, other: 'Point3') -> 'Point3':
        ...

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self._x + other._x, self._y + other._y, self._z + other._z)
        elif isinstance(other, Point3):
            return Point3(self._x + other.x, self._y + other.y, self._z + other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Vector3' and '{type(other)}'")

    def __radd__(self, other: 'Point3') -> 'Point3':
        return Point3(self._x + other.x, self._y + other.y, self._z + other.z)

    @overload
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __sub__(self, other: 'Point3') -> 'Point3':
        ...

    def __sub__(self, other):
        """
        V - P -> P
        V - V -> V
        :param other:
        :return:
        """
        if isinstance(other, Vector3):
            return Vector3(self._x - other._x, self._y - other._y, self._z - other._z)
        elif isinstance(other, Point3):
            return Point3(self._x - other.x, self._y - other.y, self._z - other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Vector3' and '{type(other)}'")

    def __rsub__(self, other: Point3):
        """
        P - V -> P
        :param other:
        :return:
        """

        if isinstance(other, Point3):
            return Point3(other.x - self._x, other.y - self._y, other.z - self._z)
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
        乘法。包括点乘和数乘。
        :param other:
        :return:
        """
        if isinstance(other, (int, float)):
            return Vector3(self._x * other, self._y * other, self._z * other)
        elif isinstance(other, Vector3):
            return self._x * other._x + self._y * other._y + self._z * other._z
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Vector3' and '{type(other)}'")

    def __rmul__(self, other: float) -> 'Vector3':
        """
        右乘。
        :param other:
        :return:
        """
        return Vector3(self._x * other, self._y * other, self._z * other)

    def __matmul__(self, other: 'Vector3') -> 'Vector3':
        """
        叉乘。
        :param other: 另一个向量
        :return: 叉乘结果向量
        """
        return Vector3(self._y * other._z - self._z * other._y,
                       self._z * other._x - self._x * other._z,
                       self._x * other._y - self._y * other._x)

    def __truediv__(self, other: float) -> 'Vector3':
        return Vector3(self._x / other, self._y / other, self._z / other)
