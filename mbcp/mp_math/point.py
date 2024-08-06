from typing import overload, TYPE_CHECKING

if TYPE_CHECKING:     # type: ignore
    from .vector import Vector3


class Point3:
    def __init__(self, x, y, z):
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

    def __add__(self, other: "Vector3") -> "Point3":
        return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
