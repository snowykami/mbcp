---
title: mbcp.mp_math.plane
---
### **class** `Plane3`
### *method* `__init__(self, a: float, b: float, c: float, d: float)`



**说明**: 平面方程：ax + by + cz + d = 0

**参数**:
> - a: x系数  
> - b: y系数  
> - c: z系数  
> - d: 常数项  


<details>
<summary> <b>源代码</b> </summary>

```python
def __init__(self, a: float, b: float, c: float, d: float):
    """
        平面方程：ax + by + cz + d = 0
        Args:
            a: x系数
            b: y系数
            c: z系数
            d: 常数项
        """
    self.a = a
    self.b = b
    self.c = c
    self.d = d
```
</details>

### *method* `approx(self, other: Plane3) -> bool`



**说明**: 判断两个平面是否近似相等。

**返回**: 是否近似相等

**参数**:
> - other: 另一个平面  


<details>
<summary> <b>源代码</b> </summary>

```python
def approx(self, other: 'Plane3') -> bool:
    """
        判断两个平面是否近似相等。
        Args:
            other: 另一个平面
        Returns:
            是否近似相等
        """
    if self.a != 0:
        k = other.a / self.a
        return approx(other.b, self.b * k) and approx(other.c, self.c * k) and approx(other.d, self.d * k)
    elif self.b != 0:
        k = other.b / self.b
        return approx(other.a, self.a * k) and approx(other.c, self.c * k) and approx(other.d, self.d * k)
    elif self.c != 0:
        k = other.c / self.c
        return approx(other.a, self.a * k) and approx(other.b, self.b * k) and approx(other.d, self.d * k)
    else:
        return False
```
</details>

### *method* `cal_angle(self, other: Line3 | Plane3) -> AnyAngle`



**说明**: 计算平面与平面之间的夹角。

**返回**: 夹角弧度

**参数**:
> - other: 另一个平面  

**引发**:
> - TypeError  不支持的类型


<details>
<summary> <b>源代码</b> </summary>

```python
def cal_angle(self, other: 'Line3 | Plane3') -> 'AnyAngle':
    """
        计算平面与平面之间的夹角。
        Args:
            other: 另一个平面
        Returns:
            夹角弧度
        Raises:
            TypeError: 不支持的类型
        """
    if isinstance(other, Line3):
        return self.normal.cal_angle(other.direction).complementary
    elif isinstance(other, Plane3):
        return AnyAngle(math.acos(self.normal @ other.normal / (self.normal.length * other.normal.length)), is_radian=True)
    else:
        raise TypeError(f'Unsupported type: {type(other)}')
```
</details>

### *method* `cal_distance(self, other: Plane3 | Point3) -> float`



**说明**: 计算平面与平面或点之间的距离。

**返回**: 距离

**参数**:
> - other: 另一个平面或点  

**引发**:
> - TypeError  不支持的类型


<details>
<summary> <b>源代码</b> </summary>

```python
def cal_distance(self, other: 'Plane3 | Point3') -> float:
    """
        计算平面与平面或点之间的距离。
        Args:
            other: 另一个平面或点
        Returns:
            距离
        Raises:
            TypeError: 不支持的类型
        """
    if isinstance(other, Plane3):
        return 0
    elif isinstance(other, Point3):
        return abs(self.a * other.x + self.b * other.y + self.c * other.z + self.d) / (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5
    else:
        raise TypeError(f'Unsupported type: {type(other)}')
```
</details>

### *method* `cal_intersection_line3(self, other: Plane3) -> Line3`



**说明**: 计算两平面的交线。

**返回**: 两平面的交线

**参数**:
> - other: 另一个平面  


<details>
<summary> <b>源代码</b> </summary>

```python
def cal_intersection_line3(self, other: 'Plane3') -> 'Line3':
    """
        计算两平面的交线。
        Args:
            other: 另一个平面
        Returns:
            两平面的交线
        Raises:
        """
    if self.normal.is_parallel(other.normal):
        raise ValueError('Planes are parallel and have no intersection.')
    direction = self.normal.cross(other.normal)
    x, y, z = (0, 0, 0)
    if self.a != 0 and other.a != 0:
        A = np.array([[self.b, self.c], [other.b, other.c]])
        B = np.array([-self.d, -other.d])
        y, z = np.linalg.solve(A, B)
    elif self.b != 0 and other.b != 0:
        A = np.array([[self.a, self.c], [other.a, other.c]])
        B = np.array([-self.d, -other.d])
        x, z = np.linalg.solve(A, B)
    elif self.c != 0 and other.c != 0:
        A = np.array([[self.a, self.b], [other.a, other.b]])
        B = np.array([-self.d, -other.d])
        x, y = np.linalg.solve(A, B)
    return Line3(Point3(x, y, z), direction)
```
</details>

### *method* `cal_intersection_point3(self, other: Line3) -> Point3`



**说明**: 计算平面与直线的交点。

**返回**: 交点

**参数**:
> - other: 不与平面平行或在平面上的直线  

**引发**:
> - ValueError  平面与直线平行或重合


<details>
<summary> <b>源代码</b> </summary>

```python
def cal_intersection_point3(self, other: 'Line3') -> 'Point3':
    """
        计算平面与直线的交点。
        Args:
            other: 不与平面平行或在平面上的直线
        Returns:
            交点
        Raises:
            ValueError: 平面与直线平行或重合
        """
    if self.normal @ other.direction == 0:
        raise ValueError('The plane and the line are parallel or coincident.')
    x, y, z = other.get_parametric_equations()
    t = -(self.a * other.point.x + self.b * other.point.y + self.c * other.point.z + self.d) / (self.a * other.direction.x + self.b * other.direction.y + self.c * other.direction.z)
    return Point3(x(t), y(t), z(t))
```
</details>

### *method* `cal_parallel_plane3(self, point: Point3) -> Plane3`



**说明**: 计算平行于该平面且过指定点的平面。

**返回**: 所求平面

**参数**:
> - point: 指定点  


<details>
<summary> <b>源代码</b> </summary>

```python
def cal_parallel_plane3(self, point: 'Point3') -> 'Plane3':
    """
        计算平行于该平面且过指定点的平面。
        Args:
            point: 指定点
        Returns:
            所求平面
        """
    return Plane3.from_point_and_normal(point, self.normal)
```
</details>

### *method* `is_parallel(self, other: Plane3) -> bool`



**说明**: 判断两个平面是否平行。

**返回**: 是否平行

**参数**:
> - other: 另一个平面  


<details>
<summary> <b>源代码</b> </summary>

```python
def is_parallel(self, other: 'Plane3') -> bool:
    """
        判断两个平面是否平行。
        Args:
            other: 另一个平面
        Returns:
            是否平行
        """
    return self.normal.is_parallel(other.normal)
```
</details>

### `@property`
### *method* `normal(self) -> Vector3`



**说明**: 平面的法向量。

**返回**: 法向量


<details>
<summary> <b>源代码</b> </summary>

```python
@property
def normal(self) -> 'Vector3':
    """
        平面的法向量。
        Returns:
            法向量
        """
    return Vector3(self.a, self.b, self.c)
```
</details>

### `@classmethod`
### *method* `from_point_and_normal(cls, point: Point3, normal: Vector3) -> Plane3`



**说明**: 工厂函数 由点和法向量构造平面(点法式构造)。

**返回**: 平面

**参数**:
> - point: 平面上的一点  
> - normal: 法向量  


<details>
<summary> <b>源代码</b> </summary>

```python
@classmethod
def from_point_and_normal(cls, point: 'Point3', normal: 'Vector3') -> 'Plane3':
    """
        工厂函数 由点和法向量构造平面(点法式构造)。
        Args:
            point: 平面上的一点
            normal: 法向量
        Returns:
            平面
        """
    a, b, c = (normal.x, normal.y, normal.z)
    d = -a * point.x - b * point.y - c * point.z
    return cls(a, b, c, d)
```
</details>

### `@classmethod`
### *method* `from_three_points(cls, p1: Point3, p2: Point3, p3: Point3) -> Plane3`



**说明**: 工厂函数 由三点构造平面。

**返回**: 平面

**参数**:
> - p1: 点1  
> - p2: 点2  
> - p3: 点3  


<details>
<summary> <b>源代码</b> </summary>

```python
@classmethod
def from_three_points(cls, p1: 'Point3', p2: 'Point3', p3: 'Point3') -> 'Plane3':
    """
        工厂函数 由三点构造平面。
        Args:
            p1: 点1
            p2: 点2
            p3: 点3
        Returns:
            平面
        """
    v1 = p2 - p1
    v2 = p3 - p1
    normal = v1.cross(v2)
    return cls.from_point_and_normal(p1, normal)
```
</details>

### `@classmethod`
### *method* `from_two_lines(cls, l1: Line3, l2: Line3) -> Plane3`



**说明**: 工厂函数 由两直线构造平面。

**返回**: 平面

**参数**:
> - l1: 直线1  
> - l2: 直线2  


<details>
<summary> <b>源代码</b> </summary>

```python
@classmethod
def from_two_lines(cls, l1: 'Line3', l2: 'Line3') -> 'Plane3':
    """
        工厂函数 由两直线构造平面。
        Args:
            l1: 直线1
            l2: 直线2
        Returns:
            平面
        """
    v1 = l1.direction
    v2 = l2.point - l1.point
    if v2 == zero_vector3:
        v2 = l2.get_point(1) - l1.point
    return cls.from_point_and_normal(l1.point, v1.cross(v2))
```
</details>

### `@classmethod`
### *method* `from_point_and_line(cls, point: Point3, line: Line3) -> Plane3`



**说明**: 工厂函数 由点和直线构造平面。

**返回**: 平面

**参数**:
> - point: 面上一点  
> - line: 面上直线，不包含点  


<details>
<summary> <b>源代码</b> </summary>

```python
@classmethod
def from_point_and_line(cls, point: 'Point3', line: 'Line3') -> 'Plane3':
    """
        工厂函数 由点和直线构造平面。
        Args:
            point: 面上一点
            line: 面上直线，不包含点
        Returns:
            平面
        """
    return cls.from_point_and_normal(point, line.direction)
```
</details>

### `@overload`
### *method* `__and__(self, other: Line3) -> Point3 | None`


<details>
<summary> <b>源代码</b> </summary>

```python
@overload
def __and__(self, other: 'Line3') -> 'Point3 | None':
    ...
```
</details>

### `@overload`
### *method* `__and__(self, other: Plane3) -> Line3 | None`


<details>
<summary> <b>源代码</b> </summary>

```python
@overload
def __and__(self, other: 'Plane3') -> 'Line3 | None':
    ...
```
</details>

### *method* `__and__(self, other)`



**说明**: 取两平面的交集（人话：交线）

**返回**: 不平行平面的交线，平面平行返回None

**参数**:
> - other:   


<details>
<summary> <b>源代码</b> </summary>

```python
def __and__(self, other):
    """
        取两平面的交集（人话：交线）
        Args:
            other:
        Returns:
            不平行平面的交线，平面平行返回None
        """
    if isinstance(other, Plane3):
        if self.normal.is_parallel(other.normal):
            return None
        return self.cal_intersection_line3(other)
    elif isinstance(other, Line3):
        if self.normal @ other.direction == 0:
            return None
        return self.cal_intersection_point3(other)
    else:
        raise TypeError(f"unsupported operand type(s) for &: 'Plane3' and '{type(other)}'")
```
</details>

### *method* `__eq__(self, other) -> bool`


<details>
<summary> <b>源代码</b> </summary>

```python
def __eq__(self, other) -> bool:
    return self.approx(other)
```
</details>

### *method* `__rand__(self, other: Line3) -> Point3`


<details>
<summary> <b>源代码</b> </summary>

```python
def __rand__(self, other: 'Line3') -> 'Point3':
    return self.cal_intersection_point3(other)
```
</details>

