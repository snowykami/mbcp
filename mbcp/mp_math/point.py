from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from .vector import Vector3  # type: ignore


class Point3:
    def __init__(self, x: float, y: float, z: float):
        """
        笛卡尔坐标系中的点。
        :param x:
        :param y:
        :param z:
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point3({self.x}, {self.y}, {self.z})"

    @overload
    def __add__(self, other: "Vector3") -> "Point3":
        ...

    @overload
    def __add__(self, other: "Point3") -> "Point3":
        ...

    def __add__(self, other):
        """
        P + V -> P
        P + P -> P
        :param other:
        :return:
        """
        return Point3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point3") -> "Vector3":
        """
        P - P -> V

        P - V -> P  已在 :class:`Vector3` 中实现
        :param other:
        :return:
        """
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, other: float) -> "Point3":
        """
        P / n -> P
        :param other:
        :return:
        """
        return Point3(self.x / other, self.y / other, self.z / other)
