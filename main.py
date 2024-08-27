from typing import overload


class Vector:
    def __init__(self, x: float, y: float, z: float):
        """
        向量
        Args:
            x: x轴分量
            y: y轴分量
            z: z轴分量
        """
        self.x = x
        self.y = y
        self.z = z
    @overload
    def __mul__(self, other: float) -> 'Vector':
        ...

    @overload
    def __mul__(self, other: 'Vector') -> float:
        ...

    def __mul__(self, other):
        """
        点乘和数乘
        Args:
            other:

        Returns:
        """
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Vector' and '{type(other)}'")

    def __rmul__(self, other: float) -> 'Vector':
        return self.__mul__(other)


v: Vector = Vector(1, 2, 3) * 3.0
v2: Vector = 3.0 * Vector(1, 2, 3)

print(v, v2)