---
title: mbcp.mp_math.vector
---
### **class** `Vector3`
### *method* `__init__(self, x: float, y: float, z: float)`



**Description**: 3维向量

**Arguments**:
> - x: x轴分量  
> - y: y轴分量  
> - z: z轴分量  


<details>
<summary> <b>Source code</b> </summary>

```python
def __init__(self, x: float, y: float, z: float):
    """
        3维向量
        Args:
            x: x轴分量
            y: y轴分量
            z: z轴分量
        """
    self.x = x
    self.y = y
    self.z = z
```
</details>

### *method* `approx(self, other: Vector3, epsilon: float = APPROX) -> bool`



**Description**: 判断两个向量是否近似相等。

**Arguments**:
> - other:   
> - epsilon:   

**Return**: 是否近似相等


<details>
<summary> <b>Source code</b> </summary>

```python
def approx(self, other: 'Vector3', epsilon: float=APPROX) -> bool:
    """
        判断两个向量是否近似相等。
        Args:
            other:
            epsilon:

        Returns:
            是否近似相等
        """
    return all([abs(self.x - other.x) < epsilon, abs(self.y - other.y) < epsilon, abs(self.z - other.z) < epsilon])
```
</details>

### *method* `cal_angle(self, other: Vector3) -> AnyAngle`



**Description**: 计算两个向量之间的夹角。

**Arguments**:
> - other: 另一个向量  

**Return**: 夹角


<details>
<summary> <b>Source code</b> </summary>

```python
def cal_angle(self, other: 'Vector3') -> 'AnyAngle':
    """
        计算两个向量之间的夹角。
        Args:
            other: 另一个向量
        Returns:
            夹角
        """
    return AnyAngle(math.acos(self @ other / (self.length * other.length)), is_radian=True)
```
</details>

### *method* `cross(self, other: Vector3) -> Vector3`



**Description**: 向量积 叉乘：v1 cross v2 -> v3

叉乘为0，则两向量平行。
其余结果的模为平行四边形的面积。


**Arguments**:
> - other:   

**Return**: 行列式的结果


<details>
<summary> <b>Source code</b> </summary>

```python
def cross(self, other: 'Vector3') -> 'Vector3':
    """
        向量积 叉乘：v1 cross v2 -> v3

        叉乘为0，则两向量平行。
        其余结果的模为平行四边形的面积。

        返回如下行列式的结果：

        ``i  j  k``

        ``x1 y1 z1``

        ``x2 y2 z2``

        Args:
            other:
        Returns:
            行列式的结果
        """
    return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
```
</details>

### *method* `is_approx_parallel(self, other: Vector3, epsilon: float = APPROX) -> bool`



**Description**: 判断两个向量是否近似平行。

**Arguments**:
> - other: 另一个向量  
> - epsilon: 允许的误差  

**Return**: 是否近似平行


<details>
<summary> <b>Source code</b> </summary>

```python
def is_approx_parallel(self, other: 'Vector3', epsilon: float=APPROX) -> bool:
    """
        判断两个向量是否近似平行。
        Args:
            other: 另一个向量
            epsilon: 允许的误差
        Returns:
            是否近似平行
        """
    return self.cross(other).length < epsilon
```
</details>

### *method* `is_parallel(self, other: Vector3) -> bool`



**Description**: 判断两个向量是否平行。

**Arguments**:
> - other: 另一个向量  

**Return**: 是否平行


<details>
<summary> <b>Source code</b> </summary>

```python
def is_parallel(self, other: 'Vector3') -> bool:
    """
        判断两个向量是否平行。
        Args:
            other: 另一个向量
        Returns:
            是否平行
        """
    return self.cross(other).approx(zero_vector3)
```
</details>

### *method* `normalize(self)`



**Description**: 将向量归一化。

自体归一化，不返回值。


<details>
<summary> <b>Source code</b> </summary>

```python
def normalize(self):
    """
        将向量归一化。

        自体归一化，不返回值。
        """
    length = self.length
    self.x /= length
    self.y /= length
    self.z /= length
```
</details>

### `@property`
### *method* `np_array(self) -> np.ndarray`




<details>
<summary> <b>Source code</b> </summary>

```python
@property
def np_array(self) -> 'np.ndarray':
    """
        返回numpy数组
        Returns:
        """
    return np.array([self.x, self.y, self.z])
```
</details>

### `@property`
### *method* `length(self) -> float`



**Description**: 向量的模。

**Return**: 模


<details>
<summary> <b>Source code</b> </summary>

```python
@property
def length(self) -> float:
    """
        向量的模。
        Returns:
            模
        """
    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
```
</details>

### `@property`
### *method* `unit(self) -> Vector3`



**Description**: 获取该向量的单位向量。

**Return**: 单位向量


<details>
<summary> <b>Source code</b> </summary>

```python
@property
def unit(self) -> 'Vector3':
    """
        获取该向量的单位向量。
        Returns:
            单位向量
        """
    return self / self.length
```
</details>

### *method* `__abs__(self)`


<details>
<summary> <b>Source code</b> </summary>

```python
def __abs__(self):
    return self.length
```
</details>

### `@overload`
### *method* `self + other: Vector3 => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __add__(self, other: 'Vector3') -> 'Vector3':
    ...
```
</details>

### `@overload`
### *method* `self + other: Point3 => Point3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __add__(self, other: 'Point3') -> 'Point3':
    ...
```
</details>

### *method* `self + other`



**Description**: V + P -> P

V + V -> V

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __add__(self, other):
    """
        V + P -> P

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
```
</details>

### *method* `__eq__(self, other)`



**Description**: 判断两个向量是否相等。

**Arguments**:
> - other:   

**Return**: 是否相等


<details>
<summary> <b>Source code</b> </summary>

```python
def __eq__(self, other):
    """
        判断两个向量是否相等。
        Args:
            other:
        Returns:
            是否相等
        """
    return approx(self.x, other.x) and approx(self.y, other.y) and approx(self.z, other.z)
```
</details>

### *method* `self + other: Point3 => Point3`



**Description**: P + V -> P

别去点那边实现了。
:param other:
:return:


<details>
<summary> <b>Source code</b> </summary>

```python
def __radd__(self, other: 'Point3') -> 'Point3':
    """
        P + V -> P

        别去点那边实现了。
        :param other:
        :return:
        """
    return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
```
</details>

### `@overload`
### *method* `self - other: Vector3 => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __sub__(self, other: 'Vector3') -> 'Vector3':
    ...
```
</details>

### `@overload`
### *method* `self - other: Point3 => Point3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __sub__(self, other: 'Point3') -> 'Point3':
    ...
```
</details>

### *method* `self - other`



**Description**: V - P -> P

V - V -> V

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __sub__(self, other):
    """
        V - P -> P

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
        raise TypeError(f'unsupported operand type(s) for -: "Vector3" and "{type(other)}"')
```
</details>

### *method* `self - other: Point3`



**Description**: P - V -> P

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __rsub__(self, other: 'Point3'):
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
```
</details>

### `@overload`
### *method* `self * other: Vector3 => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __mul__(self, other: 'Vector3') -> 'Vector3':
    ...
```
</details>

### `@overload`
### *method* `self * other: RealNumber => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
@overload
def __mul__(self, other: RealNumber) -> 'Vector3':
    ...
```
</details>

### *method* `self * other: int | float | Vector3 => Vector3`



**Description**: 数组运算 非点乘。点乘使用@，叉乘使用cross。

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __mul__(self, other: 'int | float | Vector3') -> 'Vector3':
    """
        数组运算 非点乘。点乘使用@，叉乘使用cross。
        Args:
            other:

        Returns:
        """
    if isinstance(other, Vector3):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    elif isinstance(other, (float, int)):
        return Vector3(self.x * other, self.y * other, self.z * other)
    else:
        raise TypeError(f"unsupported operand type(s) for *: 'Vector3' and '{type(other)}'")
```
</details>

### *method* `self * other: RealNumber => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
def __rmul__(self, other: 'RealNumber') -> 'Vector3':
    return self.__mul__(other)
```
</details>

### *method* `self @ other: Vector3 => RealNumber`



**Description**: 点乘。

**Arguments**:
> - other:   


<details>
<summary> <b>Source code</b> </summary>

```python
def __matmul__(self, other: 'Vector3') -> 'RealNumber':
    """
        点乘。
        Args:
            other:
        Returns:
        """
    return self.x * other.x + self.y * other.y + self.z * other.z
```
</details>

### *method* `self / other: RealNumber => Vector3`


<details>
<summary> <b>Source code</b> </summary>

```python
def __truediv__(self, other: RealNumber) -> 'Vector3':
    return Vector3(self.x / other, self.y / other, self.z / other)
```
</details>

### *method* `- self`


<details>
<summary> <b>Source code</b> </summary>

```python
def __neg__(self):
    return Vector3(-self.x, -self.y, -self.z)
```
</details>

### ***var*** `zero_vector3 = Vector3(0, 0, 0)`

- **Type**: `Vector3`

- **Description**: 零向量

### ***var*** `x_axis = Vector3(1, 0, 0)`

- **Type**: `Vector3`

- **Description**: x轴单位向量

### ***var*** `y_axis = Vector3(0, 1, 0)`

- **Type**: `Vector3`

- **Description**: y轴单位向量

### ***var*** `z_axis = Vector3(0, 0, 1)`

- **Type**: `Vector3`

- **Description**: z轴单位向量

