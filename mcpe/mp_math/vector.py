from typing import overload, TYPE_CHECKING

if TYPE_CHECKING:
    from mcpe.mp_math.point import Point3


class Vector3:
    def __init__(self, x, y, z):
        """
        笛卡尔坐标系中的向量。
        :param x:
        :param y:
        :param z:
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    @overload
    def __add__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __add__(self, other: 'Point3') -> 'Point3':
        ...

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Point3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Vector3' and '{type(other)}'")

    def __radd__(self, other: 'Point3') -> 'Point3':
        return Point3(self.x + other.x, self.y + other.y, self.z + other.z)

    @overload
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        ...

    @overload
    def __sub__(self, other: 'Point3') -> 'Point3':
        ...

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Vector3' and '{type(other)}'")

    def __rsub__(self, other: Point3):
        if isinstance(other, Point3):
            return Point3(other.x - self.x, other.y - self.y, other.z - self.z)
        elif isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.y, other.z - self.z)
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other)}' and 'Vector3'")
