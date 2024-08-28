---
title: mbcp.mp\nmath.line
order: 1
icon: laptop-code
category: API
---

### ***class*** `Line3`



### &emsp; ***def*** `__init__(self, point: 'Point3', direction: 'Vector3') -> None`

&emsp;三维空间中的直线。由一个点和一个方向向量确定。

Args:

    point: 直线上的一点

    direction: 直线的方向向量

<details>
<summary>源代码</summary>

```python
def __init__(self, point: 'Point3', direction: 'Vector3'):
    """
        三维空间中的直线。由一个点和一个方向向量确定。
        Args:
            point: 直线上的一点
            direction: 直线的方向向量
        """
    self.point = point
    self.direction = direction
```
</details>

### &emsp; ***def*** `approx(self, other: 'Line3', epsilon: float) -> bool`

&emsp;判断两条直线是否近似相等。

Args:

    other: 另一条直线

    epsilon: 误差

Returns:

    是否近似相等

<details>
<summary>源代码</summary>

```python
def approx(self, other: 'Line3', epsilon: float=APPROX) -> bool:
    """
        判断两条直线是否近似相等。
        Args:
            other: 另一条直线
            epsilon: 误差
        Returns:
            是否近似相等
        """
    return self.is_approx_parallel(other, epsilon) and (self.point - other.point).is_approx_parallel(self.direction, epsilon)
```
</details>

### &emsp; ***def*** `cal_angle(self, other: 'Line3') -> 'AnyAngle'`

&emsp;计算直线和直线之间的夹角。

Args:

    other: 另一条直线

Returns:

    夹角弧度

Raises:

    TypeError: 不支持的类型

<details>
<summary>源代码</summary>

```python
def cal_angle(self, other: 'Line3') -> 'AnyAngle':
    """
        计算直线和直线之间的夹角。
        Args:
            other: 另一条直线
        Returns:
            夹角弧度
        Raises:
            TypeError: 不支持的类型
        """
    return self.direction.cal_angle(other.direction)
```
</details>

### &emsp; ***def*** `cal_distance(self, other: 'Line3 | Point3') -> float`

&emsp;计算直线和直线或点之间的距离。

Args:

    other: 平行直线或点



Returns:

    距离

Raises:

    TypeError: 不支持的类型

<details>
<summary>源代码</summary>

```python
def cal_distance(self, other: 'Line3 | Point3') -> float:
    """
        计算直线和直线或点之间的距离。
        Args:
            other: 平行直线或点

        Returns:
            距离
        Raises:
            TypeError: 不支持的类型
        """
    if isinstance(other, Line3):
        if self == other:
            return 0
        elif self.is_parallel(other):
            return (other.point - self.point).cross(self.direction).length / self.direction.length
        elif not self.is_coplanar(other):
            return abs(self.direction.cross(other.direction) @ (self.point - other.point) / self.direction.cross(other.direction).length)
        else:
            return 0
    elif isinstance(other, Point3):
        return (other - self.point).cross(self.direction).length / self.direction.length
    else:
        raise TypeError('Unsupported type.')
```
</details>

### &emsp; ***def*** `cal_intersection(self, other: 'Line3') -> 'Point3'`

&emsp;计算两条直线的交点。

Args:

    other: 另一条直线

Returns:

    交点

Raises:

    ValueError: 直线平行

    ValueError: 直线不共面

<details>
<summary>源代码</summary>

```python
def cal_intersection(self, other: 'Line3') -> 'Point3':
    """
        计算两条直线的交点。
        Args:
            other: 另一条直线
        Returns:
            交点
        Raises:
            ValueError: 直线平行
            ValueError: 直线不共面
        """
    if self.is_parallel(other):
        raise ValueError('Lines are parallel and do not intersect.')
    if not self.is_coplanar(other):
        raise ValueError('Lines are not coplanar and do not intersect.')
    return self.point + self.direction.cross(other.direction) @ other.direction.cross(self.point - other.point) / self.direction.cross(other.direction).length ** 2 * self.direction
```
</details>

### &emsp; ***def*** `cal_perpendicular(self, point: 'Point3') -> 'Line3'`

&emsp;计算直线经过指定点p的垂线。

Args:

    point: 指定点

Returns:

    垂线

<details>
<summary>源代码</summary>

```python
def cal_perpendicular(self, point: 'Point3') -> 'Line3':
    """
        计算直线经过指定点p的垂线。
        Args:
            point: 指定点
        Returns:
            垂线
        """
    return Line3(point, self.direction.cross(point - self.point))
```
</details>

### &emsp; ***def*** `get_point(self, t: RealNumber) -> 'Point3'`

&emsp;获取直线上的点。同一条直线，但起始点和方向向量不同，则同一个t对应的点不同。

Args:

    t: 参数t

Returns:

    点

<details>
<summary>源代码</summary>

```python
def get_point(self, t: RealNumber) -> 'Point3':
    """
        获取直线上的点。同一条直线，但起始点和方向向量不同，则同一个t对应的点不同。
        Args:
            t: 参数t
        Returns:
            点
        """
    return self.point + t * self.direction
```
</details>

### &emsp; ***def*** `get_parametric_equations(self) -> tuple[OneSingleVarFunc, OneSingleVarFunc, OneSingleVarFunc]`

&emsp;获取直线的参数方程。

Returns:

    x(t), y(t), z(t)

<details>
<summary>源代码</summary>

```python
def get_parametric_equations(self) -> tuple[OneSingleVarFunc, OneSingleVarFunc, OneSingleVarFunc]:
    """
        获取直线的参数方程。
        Returns:
            x(t), y(t), z(t)
        """
    return (lambda t: self.point.x + self.direction.x * t, lambda t: self.point.y + self.direction.y * t, lambda t: self.point.z + self.direction.z * t)
```
</details>

### &emsp; ***def*** `is_approx_parallel(self, other: 'Line3', epsilon: float) -> bool`

&emsp;判断两条直线是否近似平行。

Args:

    other: 另一条直线

    epsilon: 误差

Returns:

    是否近似平行

<details>
<summary>源代码</summary>

```python
def is_approx_parallel(self, other: 'Line3', epsilon: float=1e-06) -> bool:
    """
        判断两条直线是否近似平行。
        Args:
            other: 另一条直线
            epsilon: 误差
        Returns:
            是否近似平行
        """
    return self.direction.is_approx_parallel(other.direction, epsilon)
```
</details>

### &emsp; ***def*** `is_parallel(self, other: 'Line3') -> bool`

&emsp;判断两条直线是否平行。

Args:

    other: 另一条直线

Returns:

    是否平行

<details>
<summary>源代码</summary>

```python
def is_parallel(self, other: 'Line3') -> bool:
    """
        判断两条直线是否平行。
        Args:
            other: 另一条直线
        Returns:
            是否平行
        """
    return self.direction.is_parallel(other.direction)
```
</details>

### &emsp; ***def*** `is_collinear(self, other: 'Line3') -> bool`

&emsp;判断两条直线是否共线。

Args:

    other: 另一条直线

Returns:

    是否共线

<details>
<summary>源代码</summary>

```python
def is_collinear(self, other: 'Line3') -> bool:
    """
        判断两条直线是否共线。
        Args:
            other: 另一条直线
        Returns:
            是否共线
        """
    return self.is_parallel(other) and (self.point - other.point).is_parallel(self.direction)
```
</details>

### &emsp; ***def*** `is_point_on(self, point: 'Point3') -> bool`

&emsp;判断点是否在直线上。

Args:

    point: 点

Returns:

    是否在直线上

<details>
<summary>源代码</summary>

```python
def is_point_on(self, point: 'Point3') -> bool:
    """
        判断点是否在直线上。
        Args:
            point: 点
        Returns:
            是否在直线上
        """
    return (point - self.point).is_parallel(self.direction)
```
</details>

### &emsp; ***def*** `is_coplanar(self, other: 'Line3') -> bool`

&emsp;判断两条直线是否共面。

充要条件：两直线方向向量的叉乘与两直线上任意一点的向量的点积为0。

Args:

    other: 另一条直线

Returns:

    是否共面

<details>
<summary>源代码</summary>

```python
def is_coplanar(self, other: 'Line3') -> bool:
    """
        判断两条直线是否共面。
        充要条件：两直线方向向量的叉乘与两直线上任意一点的向量的点积为0。
        Args:
            other: 另一条直线
        Returns:
            是否共面
        """
    return self.direction.cross(other.direction) @ (self.point - other.point) == 0
```
</details>

### &emsp; ***def*** `simplify(self) -> None`

&emsp;简化直线方程，等价相等。

自体简化，不返回值。



按照可行性一次对x y z 化 0 处理，并对向量单位化

<details>
<summary>源代码</summary>

```python
def simplify(self):
    """
        简化直线方程，等价相等。
        自体简化，不返回值。

        按照可行性一次对x y z 化 0 处理，并对向量单位化
        """
    self.direction.normalize()
    if self.direction.x == 0:
        self.point.x = 0
    if self.direction.y == 0:
        self.point.y = 0
    if self.direction.z == 0:
        self.point.z = 0
```
</details>

### &emsp; ***@classmethod***
### &emsp; ***def*** `from_two_points(cls: Any, p1: 'Point3', p2: 'Point3') -> 'Line3'`

&emsp;工厂函数 由两点构造直线。

Args:

    p1: 点1

    p2: 点2

Returns:

    直线

<details>
<summary>源代码</summary>

```python
@classmethod
def from_two_points(cls, p1: 'Point3', p2: 'Point3') -> 'Line3':
    """
        工厂函数 由两点构造直线。
        Args:
            p1: 点1
            p2: 点2
        Returns:
            直线
        """
    direction = p2 - p1
    return cls(p1, direction)
```
</details>

### ***var*** `direction = p2 - p1`



### ***var*** `s = 'Line3: '`



